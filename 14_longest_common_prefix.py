class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        for sg in range(len(strs[0])) :
            char=strs[0][sg]

            for words in strs[1:]:
        
                if sg >= len(words) or words[sg] != char:
                 return strs[0][:sg]

        return strs[0]
             

                

        
