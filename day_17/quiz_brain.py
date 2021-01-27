class QuizBrain:
    def __init__(self, question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0
    
    def still_has_questions(self):
        num_of_questions=len(self.question_list)
        return self.question_number < num_of_questions
    
    def next_question(self):
        question=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(user_answer,question.answer)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")