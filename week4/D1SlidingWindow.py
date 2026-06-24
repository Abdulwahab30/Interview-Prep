def maximum_sum_subarray(nums, k):
    window_sum= sum(nums[:k])
    result=0
    for i in range(k,len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i-k]
        if result<window_sum:
            result = window_sum
    print(result)

maximum_sum_subarray([2,1,5,1,3,2],3)



def running_sum(nums):
    size = len(nums)
    result = []
    current_sum = 0
    
    for num in nums:
        current_sum += num      # Add the current number to our total accumulator
        result.append(current_sum)  # Push it into our results list

    print(result)

running_sum([1,2,3,4])