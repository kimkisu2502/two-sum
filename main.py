
def twoSum(nums, target)
    result = []
    for i in range(0,len(nums))
        for j in range(i,len(nums))
            if(nums[i]+nums[j]==target and i!=j)
                result.append(i)
                result.append(j)
            
    return result
