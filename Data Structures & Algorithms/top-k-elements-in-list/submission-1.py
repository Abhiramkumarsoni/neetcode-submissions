class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict={}
        for i in nums:
            if i in count_dict:
                count_dict[i]+=1
            else:
                count_dict[i]=0
        
        sorted_dict=dict(sorted(count_dict.items(),key=lambda x:x[1],reverse=True))
        result=[]
        for key,values in sorted_dict.items():
            result.append(key)
        return result[:k]