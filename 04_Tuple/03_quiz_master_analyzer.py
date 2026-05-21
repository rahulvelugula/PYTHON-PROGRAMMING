"""
Question:
Analyze quiz answers using tuples.

Correct answer = 4 points
Wrong answer = 0 points

Accuracy Formula:

Accuracy (%) =
(Number of Correct Answers / Total Questions) * 100

Calculate:
1. Total score
2. Accuracy percentage

"""
# Read number of questions
n = int(input())

records = []

# Read quiz records
for i in range(n):

    question_id, correct_option, chosen_option = input().split()
    record = (int(question_id), correct_option, chosen_option)
    records.append(record)

score = 0
correct_answers = 0

# Evaluate answers
for question_id, correct_option, chosen_option in records:
    if correct_option == chosen_option:
        score += 4
        correct_answers += 1

# Calculate accuracy
accuracy = (correct_answers / n) * 100

print("Total Score:", score)
print(f"Accuracy: {accuracy:.2f}%")
