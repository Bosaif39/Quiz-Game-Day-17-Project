class QuizBrain:
    def __init__(self, qList):
        self.questionNum = 0  # Tracks the current question number
        self.questionList = qList  # A list of questions passed to the quiz
        self.score = 0  # Tracks the user's score

    def still_has_question(self):
        return self.questionNum < len(self.questionList)

    def next_question(self):
        current_question = self.questionList[self.questionNum]
        self.questionNum += 1

        user_ans = input(f"Q.{self.questionNum}: {current_question.text} (True/False): ")
        self.checker(user_ans, current_question.answer)

    def checker(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("Correct answer!")
        else:
            print("Incorrect answer.")

        # Provide feedback on the correct answer and current score
        print(f"The correct answer is: {correct_ans}")
        print(f"Your current score is {self.score} / {self.questionNum}\n")
