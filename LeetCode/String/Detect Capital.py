''' Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:

Input: "USA"
Output: True

 
Example 2:

Input: "FlaG"
Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.'''



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

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
***********************************************************************************************************************************************************************
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

''' The istitle() returns True if the string is a titlecased string otherwise it returns False.

what is titlecased ?

String which has the first character in each word Uppercase and remaining all characters Lowercase alphabets. '''

def detectCapitalUse(self, word):
    return word.isupper() or word.islower() or word.istitle()
        
        
        
