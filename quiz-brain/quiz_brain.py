from main import question_bank
class QuizBrain():
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"q.{self.question_number}:{current_question.text} (TRUE/FALSE)")
        self.check_answer(user_answer,current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"Your current score is {self.score}")
        else:
            print("That's wrong!")
            self.score += 0
            print(f"Your current score is {self.score}/{self.question_number}")
        print(f"the correct answer is {correct_answer}")
        print("\n")

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
else:
    print("You've completed the quiz")
    print(f"Your final score was {quiz.score}/{quiz.question_number}")




