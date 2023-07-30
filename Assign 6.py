def can_swap_strings(s, goal):
    if len(s) != len(goal):
        return False

    # Find the indices where s and goal differ
    diff_indices = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diff_indices.append(i)

    # If there are more than two differing indices, return false
    if len(diff_indices) != 2:
        return False

    # Check if characters at the differing indices are exchangeable
    i, j = diff_indices
    return s[i] == goal[j] and s[j] == goal[i]

# Test example
s = "ab"
goal = "ba"
print(can_swap_strings(s, goal))  # Output: True
