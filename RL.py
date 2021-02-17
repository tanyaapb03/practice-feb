class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # shd have r==l in substring 
        # loop through the s and check .next of string if it is same  as current then dont increment count if 
        count=0
        n=0
        if len(s)>= 1000:
            return False 
        for i in s:
            if i =="R":
                count= count+1
            if i=="L":
                count= count-1
            if count==0:
                print(count)
                n=n+1
        return n 
           
        
s=Solution()
print(s.balancedStringSplit("RLRRRLRLLL"))