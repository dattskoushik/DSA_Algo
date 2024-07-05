def length_of_longest_substring_k_distinct(s, k):
    left, right = 0, 0
    max_length = 0
    char_count = {}

    while right < len(s):
        char_count[s[right]] = right
        if len(char_count) > k:
            min_left = min(char_count.values())
            del char_count[s[min_left]]
            left = min_left + 1

        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length

# Example usage
str_input = "eceba"
k_input = 2
result = length_of_longest_substring_k_distinct(str_input, k_input)
print(result)  # Output: 3

