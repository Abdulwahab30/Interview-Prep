def lswrc(s):
    left = 0
    seen = set()
    longest_substring = [] # We'll store the actual longest string here

    # Use a standard 'right' pointer to expand our window across the string
    for right in range(len(s)):
        current_char = s[right]

        # If we hit a duplicate, shrink the window from the LEFT
        # until the duplicate character is completely removed from our set
        while current_char in seen:
            seen.remove(s[left])
            left += 1

        # Now that it's safe, add the current character to our set
        seen.add(current_char)

        # Calculate the current window's substring
        current_window_string = s[left : right + 1]

        # If the current window is longer than our record, update our record!
        if len(current_window_string) > len(longest_substring):
            longest_substring = current_window_string

    # Convert the string to an array of characters if that's your preferred output
    return longest_substring

# Test it out!
print(lswrc("abcabcbb"))  # Output: ['a', 'b', 'c']
print(lswrc("pwwkew"))    # Output: ['w', 'k', 'e']
        


def duplicate2(nums,k):
    window=set()

    for i in range(len(nums)):
        if nums[i] in window:
            print(f"Duplicate found {nums[i]} at index {i}")
            return True
        
        window.add(nums[i])

        if len(window)>k:
            window.remove(nums[i-k])
    return False

# Test Cases
print(duplicate2([1, 2, 3, 1], 3))       # Output: True  (1 is at index 0 and 3, distance is 3)
print(duplicate2([1, 0, 1, 1], 1))       # Output: True  (1 is at index 2 and 3, distance is 1)
print(duplicate2([1, 2, 3, 1, 2, 3], 2)) # Output: False (Duplicates exist, but none are close enough)