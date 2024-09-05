
class QuizBrain:
    def __init__(self,qList):
        self.questionNum=0
        self.questionList=qList
        self.score=0
    #Method  to check is there still more question 
    def still_has_question(self):
        return self.questionNum<len(self.questionList)
    
    #Method for next question
    def next_question(self):
        current_question=self.questionList[self.questionNum]
        self.questionNum +=1
	    
        user_ans=input(f"Q.{self.questionNum}: {current_question.text} (True/False):")
        self.checker(user_ans,current_question.answer)
    
    #Method to check correct answer
    def checker(self,user_ans,correct_ans):
        if(user_ans.lower() ==correct_ans.lower()):
            self.score+=1
            print("Correct ans")
        else:
            print("Incorrect ans")
        
	#Feedback for the user
        print(f"The correct ans is {correct_ans}")
        print(f"The current score is {self.score} / {self.questionNum} \n")

