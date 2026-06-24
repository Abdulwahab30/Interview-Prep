def mps(nums):
    globalmax= nums[0]
    currentmax=nums[0]
    currentmin=nums[0]

    for i in range(1,len(nums)):
        num = nums[i]
        if num < 0:
           currentmax,currentmin=currentmin,currentmax

        currentmax = max(num,currentmax * num)
        currentmin= min(num,currentmin * num)

        globalmax = max(globalmax,currentmax)
    
    return globalmax

print(mps(nums = [2, 3, -2, 4])) #-> Output: 6 (from [2,3])
print(mps(nums = [-2, 3, -4]))   #-> Output: 24 (from [-2, 3, -4] -> -2 * 3 * -4)


def subarraySum(nums, k):
    count = 0
    current_running_sum = 0
    
    # Hash Map to store: [Prefix Sum : Number of times seen]
    # CRITICAL: We initialize it with {0: 1} because a running sum of 0 
    # has technically occurred once before we even look at the first element.
    prefix_map = {0: 1}

    for num in nums:

        current_running_sum += num

        match_needed = current_running_sum - k
        if match_needed in prefix_map:
            count+=prefix_map[match_needed]

        prefix_map[current_running_sum] = prefix_map.get(current_running_sum,0)+1

    return count

print(subarraySum(nums = [1, 1, 1], k = 2))
