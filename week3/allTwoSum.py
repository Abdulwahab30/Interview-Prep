def allTwosum(nums,target):
    result={}
    pairs=set()

    for i in range(len(nums)):
        num = nums[i]
        compliment = target - num

        if compliment in result:
            pair = tuple(sorted((num, compliment)))
            pairs.add(pair)

        result[num] = i
    # Convert our unique pairs back into a list of lists
    return [list(p) for p in pairs]

print(allTwosum([2, 4, 3, 3, 5, 1], 6))