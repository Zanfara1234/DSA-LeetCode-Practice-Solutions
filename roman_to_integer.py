class Solution(object):
    def romanToInt(self, s):
            values={
                "I" :1,
                "V" :5,
                "X" :10,
                "L" :50,
                "C" :100,
                "D" :500,
                "M" :1000
                }
            
            total_sum=0

            for i in range(len(s)):
                current_value=values[s[i]]
                if i< len(s)-1:
                  next_value=values[s[i+1]]
                  
                  if current_value < next_value:
                    total_sum= total_sum - current_value 
                
                  else:
                    total_sum=total_sum + current_value 

                else:
                    total_sum=total_sum + current_value  
                
            return total_sum

        


        
