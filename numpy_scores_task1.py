import numpy as np

np.random.seed(42)
# We use 101 as the upper limit because randint stops *before* the last number.
# So (50, 101) generates numbers from 50 to 100.
scores = np.random.randint(50, 101, size=(5, 4))

print("--- Full Class Scores (Rows=Students, Cols=Subjects) ---")
print(scores)
print("-" * 50)
# Python counts from 0. So:
# Student 3 = Index 2
# Subject 2 = Index 1
single_score = scores[2, 1]
print("Score of 3rd student in 2nd subject:", single_score)
# We use -2: to mean "start from the 2nd to last and go to the end"
# The : after the comma means "include all columns (subjects)"
last_two_students = scores[-2:, :] 
print("\nScores of last 2 students:")
print(last_two_students)
# Rows (Students): :3 means indices 0, 1, 2
# Cols (Subjects): 1:3 means indices 1 (Subject 2) and 2 (Subject 3). It stops before 3.
specific_subset = scores[:3, 1:3]
print("\nFirst 3 students, subjects 2 & 3 only:")
print(specific_subset)