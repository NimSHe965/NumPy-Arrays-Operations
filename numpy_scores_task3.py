import numpy as np

np.random.seed(42)
scores = np.random.randint(50, 101, size=(5, 4))
curve_values = np.array([5, 3, 7, 2])
curved_scores = np.minimum(scores + curve_values, 100)

print("Curved Scores (from Task 2):")
print(curved_scores)
print("-" * 30)

# --- Task 3 Starts Here ---

# Requirement 1: Normalize scores to 0-1 scale per row (Student)
# We need the min and max for EACH student (row).
# Important: We use keepdims=True so the result is shape (5, 1) instead of (5,).
# This allows us to subtract a column vector from the 2D matrix (Broadcasting).
row_min = np.min(curved_scores, axis=1, keepdims=True)
row_max = np.max(curved_scores, axis=1, keepdims=True)

# The Formula: (Score - Min) / (Max - Min)
normalized_scores = (curved_scores - row_min) / (row_max - row_min)

print("Normalized Scores (0 to 1 scale):")
print(np.round(normalized_scores, 2))


# Requirement 2: Find the index of the highest value in the normalized array
# np.argmax gives the index as if the array were a flat line (e.g., index 13).
# np.unravel_index converts that flat number back into (Row, Col).
flat_index_of_max = np.argmax(normalized_scores)
student_idx, subject_idx = np.unravel_index(flat_index_of_max, normalized_scores.shape)

print(f"\nHighest normalized value is at Student index: {student_idx}, Subject index: {subject_idx}")


# Requirement 3: Extract scores strictly above 90
# We create a "mask" (a True/False grid)
mask = curved_scores > 90

# We apply the mask to the array. This flattens the result into a 1D list of only the matching numbers.
scores_above_90 = curved_scores[mask]

print(f"\nScores strictly above 90: {scores_above_90}")