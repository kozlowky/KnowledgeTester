import sys
from random import sample
from modules import *

print('Здравствуйте, Я - Тестировщик знаний!\n')


def main():
    question_bank = []
    question_random = sample(question_db, 10)
    for q in question_random:
        question_text = q['question']
        question_answer = q['answer']
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    known_tester = KnownTester(question_bank)

    while known_tester.still_has_question():
        known_tester.next_question()

    print(f'Правильных ответов: {known_tester.score} из {known_tester.question_number}')
    repeat_test = input('Чтобы повторить тест введите "y", или нажмите на любую клавишу: ')
    if repeat_test == 'y':
        return main()
    else:
        print('Тест окончен. Нажмите любую клавишу!')


if __name__ == '__main__':
    exit(main())
    print(sys.stdin.readline())
