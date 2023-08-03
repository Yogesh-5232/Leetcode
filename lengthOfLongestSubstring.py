class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        continues=[];count,temp=0,0
        for i in s:
            while(i in continues):
                continues.pop(0)
                temp-=1
            else:
                continues.append(i)
                temp+=1
                count=max(count,temp)
        return count
