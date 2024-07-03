class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vowel = 'aeiou'

        vowel_check = False
        consonant_check = False
        for char in word: #make sure to convert char to lower()
            if char.lower().isalpha() and char.lower() in vowel:
                vowel_check = True
            elif char.lower().isalpha() and not char.lower() in vowel:
                consonant_check = True
            elif char.isdigit():
                continue
            else: 
                return False
        return vowel_check and consonant_check

        #Time: O(n), since our variable is constant size the lookup in the 'in' key is just O(1)
        #Space: O(1)
