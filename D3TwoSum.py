def twosum(nums, target):
    size = len(nums)
    nums.sort()  # Sorting is mandatory for the two-pointer technique to work
    result = []
    
    # Initialize our two pointers at opposite ends of the sorted list
    left = 0
    right = size - 1
    
    # Keep searching as long as the pointers haven't crossed each other
    while left < right:
        current_sum = nums[left] + nums[right]
        
        # Case 1: We found the target!
        if current_sum == target:
            result = [nums[left], nums[right]]
            break  # CRITICAL: Stop the loop immediately so it doesn't run forever!
            
        # Case 2: The sum is too small, move left pointer rightward to get a bigger number
        elif current_sum < target:
            left += 1
            
        # Case 3: The sum is too big, move right pointer leftward to get a smaller number
        else:
            right -= 1
            
    print(result)

# Test Case
twosum([2, 7, 11, 15], 9)  # Output: [2, 7]