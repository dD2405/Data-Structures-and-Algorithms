class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if word.isupper() == True:
            return True
        if word.islower() == True:
            return True
        
        first_word = word[0]
        rest_of_the_word = word[1:]
        
        
        if first_word.isupper() == True and rest_of_the_word.islower() == True:
            return True
        else:
            return False
            
        
        
        
