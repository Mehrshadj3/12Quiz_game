from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_text = i['text']
    question_answer = i['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz!")
print(f"Nice job! Your total score is {quiz.user_score} from possible 12.")

