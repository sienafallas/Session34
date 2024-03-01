def find_pattern_occurrences(text):
    # Initialize the count of matches found
    match_count = 0

    # Iterate over the text character by character
    for i in range(len(text)):
        # Check if the current character is 'u' and the next character is 'n'
        if text[i:i + 2] == 'un':
            # Initialize the potential pattern starting from 'un'
            pattern = 'un'
            j = i + 2

            # Continue adding characters to the pattern until we reach 'an' at the end
            while j < len(text) and text[j:j + 2] != 'an':
                pattern += text[j]
                j += 1

            # If we find a pattern that matches the desired format, increment the match count
            if j < len(text) and text[j:j + 2] == 'an':
                match_count += 1

    # Return the total count of matches found
    return match_count


# Test the function with a sample text
sample_text = "unruly and unusual pandas under the panda umbrella"
matches = find_pattern_occurrences(sample_text)
print("Number of matches found:", matches)


