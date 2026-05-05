from question_model import Question
from data import question_data

question_bank = []

# Question raw data into Question objects
for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Run the quiz
score = 0

for question in question_bank:
    user_answer = input(f"{question.text} (True/False): ")

    if user_answer.lower() == question.answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    print(f"Current Score: {score}/{len(question_bank)}\n")

print("Quiz complete.")
print(f"Final Score: {score}/{len(question_bank)}")

