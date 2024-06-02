def canConstruct(ransomNote, magazine):
    # create a hash to store magazine letters
    letters = {}    
    for letter in magazine:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    # loop through all letters in the ransom note and if they exist subtract 1
    for letter in ransomNote:
        if letter in letters:
            letters[letter] -= 1
    # if the subtracted letter is less than 0 return false
            if letters[letter] < 0:
                return False
        else:
            return False

    # return true
    return True
