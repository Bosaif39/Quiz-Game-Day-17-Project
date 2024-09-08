from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a list to hold question objects created from question_data
question_var = []

# Loop through each dictionary in question_data to extract text and answer
for i in question_data:
    question_text = i["text"]
    question_ans = i["answer"]
    # Create a new Question object and append it to the question_var list
    new = Question(question_text, question_ans)
    question_var.append(new)

# Create an instance of the QuizBrain class with the list of questions
quiz = QuizBrain(question_var)

# Loop to continue the quiz until all questions are answered
while quiz.still_has_question():
    quiz.next_question()

# Print the final result once the quiz is over
print(f"The quiz is done!")
print(f"The current score is {quiz.score} / {quiz.questionNum} \n")
