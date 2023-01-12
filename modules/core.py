class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class KnownTester:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question_option = [1, 2, 3, 4]
        current_question = self.question_list[self.question_number]
        user_answer = int(input(f'Q.{self.question_number}: {current_question.question}> '))
        if user_answer not in question_option:
            print('Некорректное значение!!!')
            return current_question
        else:
            self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, answer):
        if user_answer == answer:
            self.score += 1

