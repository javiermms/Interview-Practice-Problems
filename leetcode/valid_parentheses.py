class Solution:
    def isValid(self, s: str) -> bool:
        
        left = 0
        right = len(s)-1
        matching_left = 0
        matching_right = 0
        times_num_changed = 0
        num = 0
        
        while left < right:
            if ord(s[left])+1 == ord(s[right]):
                print('{} {}'.format(left, right))
                left += 1
                right -= 1
                num = ord(s[right])
            
            matching_left += 1
            
            if num != s[right]:
                matching_right += 1
                times_num_changed += 1
                if matching_right != matching_left and times_num_changed > 2:
                    return False
                
            
            right += 1
        return True
            
        