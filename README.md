### **Quiz Game**

**Overview:**

This is the day 17 project of the course 100 Days of Code: The Complete Python Pro Bootcamp. It is a simple quiz game that asks the player a series of True/False questions. The quiz game tests the player's general knowledge and provides immediate feedback on their answers.


**How It Works:**

The game consists of a predefined set of questions stored in a list of dictionaries. Each question has a text and a corresponding correct answer (`True` or `False`). The user is prompted to answer each question, and after each response, the game will provide feedback on whether the answer was correct and display the current score.

The game continues until all questions are answered, and at the end, the total score is displayed.

**Example**

![alt text]()

**Features**
- A set of True/False questions.
- Immediate feedback for each answer.
- The player's score is tracked and displayed after each question.
- Final score displayed at the end of the quiz.

**Requirements**

Python 3.x

**Code Structure**
The project is composed of multiple Python files:

- **`data.py`**: Contains the list of quiz questions and answers.
- **`question_model.py`**: Defines the `Question` class to structure the questions.
- **`quiz_brain.py`**: Handles the quiz flow, including question prompts, answer checking, and score tracking.
- **`main.py`**: The entry point that initializes the quiz and starts the game.




