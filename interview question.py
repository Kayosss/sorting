
def longestSubstring(str1, str2):
    # Create a set from the second string for quick O(1) lookups 
    s = set(str2)
    # Initialise the dp array with all 0s
    dp = [0] * len(str1)

    # Base case, whether the first letter is in the second string or not
    dp[0] = 1 if str1[0] in s else 0
    # dp[i] = longest substring we can build by including this index, ending with that index
    # dp[x] = dp[x] + 1 if str1[x] is in str2 otherwise it is 0

    # Final solution will be the max of dp, i.e the longest substring 
    # if dp[x] is the max of dp, then x is the end index of the substring and dp[x] is the length
    
    for i in range(1, len(str1)):
        if str1[i] in s:
            # If the character is in the second string
            # 'Extend' The substring by including the current character
            dp[i] = dp[i - 1] + 1
        else: 
            # The longest string we can build by including this character is 0
            dp[i] = 0
    length = max(dp)
    end_index = dp.index(length)

    # Calculate and extract the substring using the length and end_index 
    start_index = max(0, end_index - length + 1)
    
    # Extract and return the sublist
    return str1[start_index:end_index + 1]
        
# Test case 1: Basic test case with a simple match
print(longestSubstring("noobnkjkoob", "obn"))  # Expected output: "noobn"

# Test case 2: No characters from str2 in str1
print(longestSubstring("abcdefg", "xyz"))  # Expected output: ""

# Test case 3: All characters from str1 in str2
print(longestSubstring("abababab", "ab"))  # Expected output: "abababab"

# Test case 4: Repeated characters with some interruptions
print(longestSubstring("aabbccddeeaabbccdd", "abcd"))  # Expected output: "aabbccdd"

# Test case 5: Substring at the beginning
print(longestSubstring("xyzabcdefg", "abc"))  # Expected output: "abc"

# Test case 6: Substring at the end
print(longestSubstring("mnopqrstuabc", "abc"))  # Expected output: "abc"

# Test case 11: Substring in the middle
print(longestSubstring("xxxxabcyyyyz", "abc"))  # Expected output: "abc"

# Test case 12: Noobn
print(longestSubstring("noobnkjkoob", "obn"))