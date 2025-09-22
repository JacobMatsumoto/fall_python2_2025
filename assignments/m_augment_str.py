
class VowelString(str): 
    """
    vowel string class, it gives anything that has it's class string properties along with being able to count the
    vowels in a given string.
    """
    def __init__(self, *args):
        super().__init__()

    def count_vowels(self):
            """
            Counts vowels in a given string and returns the result and original string
            """
            vowel_count = 0
            for letter in self:
                if letter in 'aeiouyAEIOUY': #checks to see if its in the vowels 
                    vowel_count +=1 
            return f"{self} has {vowel_count} vowels"
            

#innitializing what i need to test the class and function
my_words = "Lots of vowels in here Ey?"
my_sentance = VowelString(my_words)

hello = "Hello, World!"
example_sentance = VowelString(hello)

print(my_sentance.count_vowels())
print(example_sentance.count_vowels())