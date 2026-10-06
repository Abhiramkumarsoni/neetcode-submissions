class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictionary={}
        for index,number in enumerate(numbers):
            need=target-number
            if need in dictionary:
                return [dictionary[need]+1,index+1]
            else:
                dictionary[number]=index
