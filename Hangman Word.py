# Write the class HangmanWord which takes a string as an argument, representing a word in the game hangman.
# The class should know which letters are revealed. The class should have the following methods:
# __str__(): shows the word, only displaying the revealed letters, if they are unrevealed, print "_" instead (letters should be printed in lowercase).
# char_in_word(char): returns a boolean value whether the argument character is inside the string (case-insensitive).
# reveal_letter(char): reveals a letter in the word, so next time it is printed, it should be displayed.
# _validate_character(char) : Function that validates that a character is valid
 
# A character is valid if:
# It is only 1 character and is alphabetical
# It is found within the word
# The function reveal_letter(char) should call _validate_character(char)


class HangmanWord:
    def __init__(self,word):
        self.word = word
        self.guessword = "".join(['_' for char in self.word])

    def __str__(self):
        print_str = ""
        for ch in self.guessword:
            print_str += ch + " "
        return print_str.strip()

    def char_in_word(self, char):
        if char.lower() in self.word.lower():
            return True
        else:
            return False

    def reveal_letter(self,char):
        guessword_list = list(self.guessword)
        for index, value in enumerate(self.word):
            if value.lower() == char.lower():
                guessword_list[index] = char
        self.guessword = ''.join(guessword_list)
        
    def _validate_character(self,char):
        if len(char) == 1 and char.isalpha():
            if self.char_in_word(char):
                return True
            else:
                return False
        else:
            return False

word1 = HangmanWord("ball")
word1.reveal_letter("a")
word1.reveal_letter("k")
word1.reveal_letter("l")
print(word1)
