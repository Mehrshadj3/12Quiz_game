class QuizBrain:
    def __init__(self, question_list,):
        self.question_list = question_list
        self.question_number = 0
        self.user_score = 0

    def still_has_questions(self):
         return self.question_number < 12


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.user_score += 1
            print(f"You got it right! The answer is {correct_answer}")
            print(f"Your score is {self.user_score}/{self.question_number}")
            print('\n')

        else:
            print(f"Sorry you got it wrong. The answer is {correct_answer}")
            print(f"Yor score is {self.user_score}/{self.question_number}")
            print('\n')









