
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain



#list from the question_data
question_var=[]
#A loop to add the from question_data to question_var
for i in question_data:
    question_text=i["text"]
    question_ans=i["answer"]
    new=Question(question_text,question_ans)
    question_var.append(new)
    
quiz= QuizBrain(question_var)

#lop for all questions 
while quiz.still_has_question():
    quiz.next_question()
    

print(f"THe quiz is done!")
print(f"The current score is {quiz.score} / {quiz.questionNum} \n")