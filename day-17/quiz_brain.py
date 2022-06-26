class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.score = 0
        self.question_list=question_list
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        position=self.question_number
        current_question=(self.question_list)[position]
        user_answer=input(f'Q.{position +1} :{current_question.text}.(True/False):')
        self.question_number+=1
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() ==correct_answer.lower():
            self.score+=1
            print(f'You got it right')
        else:
            print(f'You got it wrong')
        print(f'The current answer was {correct_answer}\nYour current score is :{self.score}/{self.question_number}')
        print("\n")
    def quiz_ended(self):
        if self.still_has_questions():
            pass
        else:
            print(f'You\'ve completed the quiz')
            print(f'Your final score was {self.score}/{len(self.question_list)}')