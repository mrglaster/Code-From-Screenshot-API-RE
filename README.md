## Code From Screenshot: Reverse Engineered API 

### Description 

This project is the result of [Code From Screenshot](https://www.codefromscreenshot.com/) service API reverse engineering. In api_demo.py you will find the implementation of the API as well as an usage example 

![изображение](https://github.com/mrglaster/Code-From-Screenshot-API-RE/assets/50916604/9665dfe4-c2ce-4f99-8fa4-f3ad27adddfa)


### Results demo 

#### Source Image 

![изображение](https://github.com/mrglaster/Code-From-Screenshot-API-RE/assets/50916604/e2fa0c0c-ab76-4c63-b40c-72d3c472fd08)


#### Recognized Code 

```
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("How old are you?: ");
        int age = in.nextInt();

        if (age < 16) {
            System.out.println("Sorry, you are not quite old enough to drive!");
        } else {
            System.out.println("Yeah! Happy driving!");
        }
    }
}
```

#### Source Image 


![изображение](https://github.com/mrglaster/Code-From-Screenshot-API-RE/assets/50916604/f7b1b746-fc76-4d02-99ff-8fefeb7502c6)


#### Recognized Code 


```
@Controller
@RequestMapping("student/registration")
public class StudentRegistrationController {

    @InitBinder
    public void initBinder(WebDataBinder dataBinder) {

        StringTrimmerEditor stringTrimmerEditor = new StringTrimmerEditor(true);
        dataBinder.registerCustomEditor(String.class, stringTrimmerEditor);
    }

    @RequestMapping("/registrationForm")
    public String showForm(Model theModel) {
        Student theStudent = new Student();
        theModel.addAttribute("student", theStudent);

        return "student-registration-form";
    }
}
```

