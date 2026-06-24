def arrayIntersection(nums1, nums2):
    set1 = nums1
    result=set()
    for i in nums2:
        if i in set1:
            result.add(nums2[i])
    fin=[result]
    print(fin)

arrayIntersection([1,2,2,1],[2,2])