def solution(S):
    # Step 1: Initialize an empty dictionary to count frequencies
    frequency = {}

    # Step 2: Count the frequency of each character in the string
    for char in S:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Step 3: Calculate the number of deletions needed
    deletions = 0
    for count in frequency.values():
        if count % 2 != 0:
            deletions += 1  # Each odd occurrence needs one deletion to make it even

    return deletions

# Trials
print(solution("acbcbba"))  # Output: 1

