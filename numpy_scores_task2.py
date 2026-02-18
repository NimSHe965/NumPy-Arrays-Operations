import numpy as np

np.random.seed(42)
scores = np.random.randint(50, 101, size=(5, 4))
print("Original Scores:\n", scores)
print("-" * 30)

#Task 2 Starts From Here

# Requirement 1: Compute column-wise mean (average per subject)
# axis=0 means "collapse the rows" (look down each column)
subject_means = np.mean(scores, axis=0)
subject_means = np.round(subject_means, 2)

print("Average per subject:", subject_means)

# Requirement 2: Add a curve and cap at 100
# We want to add [5, 3, 7, 2] to every row.
# NumPy "Broadcasting" stretches this small array to match the size of the big array automatically.
curve_values = np.array([5, 3, 7, 2])

# Perform the addition
scores_with_curve = scores + curve_values
# Cap the scores at 100 (if a score is 105, make it 100)
# np.minimum compares the calculated score vs 100 and takes the smaller one
curved_scores = np.minimum(scores_with_curve, 100)

print("\nCurved Scores (capped at 100):\n", curved_scores)


# Requirement 3: Row-wise max (best score per student)
# axis=1 means "collapse the columns" (look across each row)
best_scores = np.max(curved_scores, axis=1)

print("\nBest score for each student:", best_scores)