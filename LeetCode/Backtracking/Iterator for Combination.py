''' Design an Iterator class, which has:

    A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
    A function next() that returns the next combination of length combinationLength in lexicographical order.
    A function hasNext() that returns True if and only if there exists a next combination.

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false

Constraints:

    1 <= combinationLength <= characters.length <= 15
    There will be at most 10^4 function calls per test.
    It's guaranteed that all calls of the function next are valid. '''


# Using itertools.combinations() 

from itertools import combinations 
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.char = characters
        self.length = combinationLength

        self.string_combinations = list(combinations(self.char, self.length))
        self.string_combinations = [''.join(items) for items in self.string_combinations]   
        self.traverse = -1

    def next(self) -> str:
        if self.hasNext():
            self.traverse += 1
            return self.string_combinations[self.traverse]
        
        
        
        
    def hasNext(self) -> bool:
        return self.traverse + 1 < len(self.string_combinations)
        print()
         
        
# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
######################################################################################################################################################################
----------------------------------------------------------------------------------------------------------------------------------------------------------------------


