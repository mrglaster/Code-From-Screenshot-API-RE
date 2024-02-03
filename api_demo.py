import os
import tarfile
import requests


def get_api_urls():
    api_getting_url = 'https://code-from-screenshot-lmuw6mcn3q-uc.a.run.app/assets/env/.env'
    result = requests.get(api_getting_url).text.split('\n')[:-1]
    result = [i[i.find('=') + 1:] for i in result]
    return result[0], result[1]


def create_tar_gz_archive(archive_name, image_path):
    with tarfile.open(archive_name, "w:gz") as tar:
        tar.add(image_path)


def read_tar_gz_as_array(file_path):
    with tarfile.open(file_path, 'r:gz') as tar:
        file_info = tar.getmembers()[0]
        file_content = tar.extractfile(file_info).read()
    integer_array = [int(byte) for byte in file_content]
    return integer_array


def recognize_code(url, archive_data):
    json_data = {"iterable": [{"value": archive_data}]}
    response = requests.post(url, json=json_data).json()
    return response["iterable"][0]["ocr"]["text"]


def process_ocr(image_path):
    ocr, tlp = get_api_urls()
    array_path = 'temp.tar.gz'
    create_tar_gz_archive(array_path, image_path)
    image_data = read_tar_gz_as_array(array_path)
    result = recognize_code(ocr, image_data)
    os.remove(array_path)
    return result


def main():
    print(process_ocr('test_images/1K2c79l6ZM9zvG5vKvO1ROg.png'))


if __name__ == '__main__':
    main()
