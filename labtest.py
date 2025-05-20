# import json
# import time
# import random
# from logging import exception
#
#
# class Question:
#     def __init__(self, text, options, answer, category):
#         self.text = text
#         self.options = options
#         self.answer = answer
#         self.category = category
#
#     def check_answer(self, user_answer):
#         return user_answer == self.answer
#
#     class Quiz:
#         def __init__(self):
#             self.questions = []
#             self.score = 0
#             self.time_taken = 0
#
#         def start_quiz(self):
#             ...
#
#         def load_questins(self, filename):
#             try:
#                 with open(filename, 'r') as file:
#                     data = json.load(file)
#                     for item in data:
#                         question = Question(item['question'], item['options'], item['answer'], item['category'])
#                         self.questions.append(question)
#             except Exception as e:
#                 print(f"Error Loading Questions{e}")
#
#         def add_question(self, question):
#             self.questions.append(question)
#
#
#
#
#
#
#
#
#
#
# # class Question:
# #     def __init__(self, question_text, options, correct_answer):
# #         self.question_text = question_text
# #         self.options = options
# #         self.correct_answer = correct_answer
# #
# #     def is_correct(self, answer):
# #         return answer == self.correct_answer
# #
# #
# # class Quiz:
# #     def __init__(self, questions):
# #         self.questions = questions
# #         self.score = 0
# #
# #
# #     def run(self):
# #         for question in self.questions:
# #             print("\n" + question.question_text)
# #             for idx, option in enumerate(question.options):
# #                 print(f"{idx + 1}. {option}")
# #             answer = int(input("Choose option number: "))
# #             if question.is_correct(answer):
# #                 print("Correct!")
# #                 self.score += 1
# #             else:
# #                 print("Wrong!")
# #         print(f"\nQuiz finished! Your score: {self.score}/{len(self.questions)}")
# #
# #
# # import json
# #
# # def load_questions(filename):
# #     with open(filename, 'r') as file:
# #         data = json.load(file)
# #         questions = ['QuizSampleQuestions.json']
# #         for item in data:
# #             question = Question(
# #                 item['question'],
# #                 item['options'],
# #                 item['answer']
# #             )
# #             questions.append(question)
# #         return questions
# #
# #
# # import time
# #
# # start_time = time.time()
# #
# #
# # end_time = time.time()
# # total_time = end_time - start_time
# # print(f"Time taken: {total_time:.2f} seconds")
# #
# #
# # def save_results(username, score, total_questions, time_taken):
# #     result = {
# #         "name": username,
# #         "score": score,
# #         "total": total_questions,
# #         "time": round(time_taken, 2)
# #     }
# #     with open('results.json', 'a') as f:
# #         json.dump(result, f)
# #         f.write("\n")
#


import json
import time

class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return answer == self.correct_answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        for question in self.questions:
            print("\n" + question.question_text)
            for idx, option in enumerate(question.options, start=1):
                print(f"{idx}. {option}")
            try:
                answer = int(input("Choose option number: "))
                if answer == question.correct_answer:
                    print("Correct!")
                    self.score += 1
                else:
                    print("Wrong!")
            except ValueError:
                print("Invalid input. Please enter a number.")

def load_questions(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        questions = []
        for item in data:
            try:
                question = Question(
                    item['question'],
                    item['options'],
                    item['answer']
                )
                questions.append(question)
            except KeyError as e:
                print(f"Warning: Missing key {e} in question: {item}")
                continue
        return questions

def save_results(username, score, total_questions, time_taken):
    result = {
        "name": username,
        "score": score,
        "total": total_questions,
        "time": round(time_taken, 2)
    }
    with open('results.json', 'a') as f:
        json.dump(result, f)
        f.write("\n")

user_name = input("Enter your name: ")
questions = load_questions('QuizSampleQuestions.json')

quiz = Quiz(questions)

start_time = time.time()
quiz.run()
end_time = time.time()

total_time = end_time - start_time

print(f"\n{user_name}, your final score is {quiz.score}/{len(questions)}")
print(f"Time taken: {total_time:.2f} seconds")

save_results(user_name, quiz.score, len(questions), total_time)















