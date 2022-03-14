### goal: to create page that allows students to find GPA for the trimester
#### Requirements: one list, an input, an algorithm, one procedure, instructions for output, and calls to your student-developed procedure.
### Brainstorm
![](https://i.postimg.cc/sxmg01LN/Screen-Shot-2022-02-28-at-11-50-48-AM.png)
### [Overview of the CB “Create Performance Task”](https://apcentral.collegeboard.org/pdf/ap-csp-student-task-directions.pdf?course=ap-computer-science-principles)
### [Create Task Code](https://github.com/nadirahaddach/4Gs/blob/main/templates/gpa.html)
![](https://i.postimg.cc/y6vk3t2h/Screen-Shot-2022-02-27-at-10-49-59-AM.png)
### 1. PROGRAM CODE
#### □ Instructions for input from one of the following:
“Enter your grade in the form of a letter grade for each class:”
![](https://i.postimg.cc/nhQWD8SC/Screen-Shot-2022-02-27-at-11-10-31-AM.png)
##### User will enter letter grades for each class
#### □ Use of at least one list (or other collection type) to represent a collection of data that is stored and used to manage program complexity and help fulfill the program’s purpose
![](https://i.postimg.cc/WpYJRHm4/Screen-Shot-2022-02-27-at-11-30-49-AM.png)
##### Uses inputs provided by user to then store them as lower case only. This allows the function to work weather the input is put in uppercase or lowercase. 
#### □ At least one procedure that contributes to the program’s intended purpose, where you have defined: 
Using the list as a parameter the grade calculator will act as a procedure and return the value of the GPA after being calculated. 
#### □ An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure 
![](https://i.postimg.cc/F1XrXb7Z/Screen-Shot-2022-02-27-at-11-03-54-AM.png)
##### Sequencing: First the algorithm checks if what was inputted was an a, if it would that would be stored as a 4 if not then it would move to the next variable that could be inputted. 
##### Selection: The code is only run if the user inputs their grades, also the grades are within the correct grading system. 
##### Iteration: Continues to run through the function for each input repeating steps. 
#### □ Calls to your student-developed procedure 
![](https://i.postimg.cc/bN0DNdpJ/Screen-Shot-2022-02-27-at-11-05-42-AM.png)
##### Calculate GPA button calls to the function
#### □ Instructions for output (tactile, audible, visual, or textual) based on input and program functionality
![](https://i.postimg.cc/pXK8hqYP/Screen-Shot-2022-02-27-at-11-04-02-AM.png)
![](https://i.postimg.cc/sXvKyZLQ/Screen-Shot-2022-02-27-at-11-45-39-AM.png)
### 2. VIDEO: Create Task runtime

https://user-images.githubusercontent.com/89223526/155920572-8e050eb1-896e-4da6-9df7-2a973132640f.mov

### 3. Written Response
#### a) The overall purpose of the program is for students to be able to calculate their GPA for the trimester. It allows students to be able to see how their grade reflects on their GPA. GPA is the grade point average of a student's grades they get. Making a easy way for students to find theres will help them in the future. The video, it shows a user inputting their grades. I had them all lower case but the function would still work if some were uppercase. After typing in a letter grade the function takes it in then releases an output. That output, as seen, is the GPA of the five classes. The inputs provided in the video is A, B, and C. Other inputs include D and F but it is not shown in the video. The output in the video was the GPA of the five grades imputed, 3.2. The output can be anywhere between zero and four. 

#### b) 
![](https://i.postimg.cc/1twTHJTy/Screen-Shot-2022-02-27-at-8-06-30-PM.png)
![](https://i.postimg.cc/WpYJRHm4/Screen-Shot-2022-02-27-at-11-30-49-AM.png)
#### These two code segments are both lists that help to run the program. Each list stores the values that were inputted by the user but they are in different forms. The two lists work with each other to store the inputs. The second list takes the data provided by the input then changes the values to lowercase so that the data is coherent. The first list changes the input into a new variable. The two lists are gpaList2 and gpaList1. These lists contain data of the inputs given by the user. So the grade the user got in each class is stored in the list. This allows for the program to calculate the GPA. Without the lists the program's code would be a lot more lines. Lists also help so there aren’t individual variables to work with. If I didn’t have this list I would have to add in more statements showing the lowercase letters and what they would equal. That would cause the program to go throught more steps going through each if statements. Another thing I would probably have to do for the code is make a function for each input. This would cause the code to be over 300 lines of code because I would have to put in a function with ten if statements. For the uppercase and lowercase letter grades. Theses lists allow for the code to be less complex. It creates a more organized way of storing the values. 

#### c)
![](https://i.postimg.cc/F1XrXb7Z/Screen-Shot-2022-02-27-at-11-03-54-AM.png)
![](https://i.postimg.cc/bN0DNdpJ/Screen-Shot-2022-02-27-at-11-05-42-AM.png)
#### The first program code changes the value that was originally from the input into an integer. This allows the program to calculate the GPA. The second is the button the user click to receive the output. This button calls to the function and gets the output then displays it. The first function takes the values in the lists and uses if statements to figure out what integer should be replaced by it. This makes it easier and faster to find what the integral matches with the input. First, it gets the value from where the user inputs their answer. Then, it creates an if statement stating that if the input is a certain letter then it equals a certain number. If it isn’t that letter it moves on to the next letter. This continues unil the input is the same as the letter in the if statement. 

#### d)
#### First Call
![](https://i.postimg.cc/y6vk3t2h/Screen-Shot-2022-02-27-at-10-49-59-AM.png)
#### Second Call
![](https://i.postimg.cc/ZKmQZGsm/Screen-Shot-2022-02-27-at-9-14-23-PM.png)
#### The conditions tested in the first call are the inputs the user puts in; a, b, b, c, and a. The conditions tested in the second call are the inputs; b, b, b, c, and a. The result of the first call is the GPA of the inputs. This comes out to be 3.2. The result of the second call is the GPA of the inputs. This comes out to be 3. 
