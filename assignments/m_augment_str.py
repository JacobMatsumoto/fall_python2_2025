
class VowelString(str):
    def __init__(self, *args):
        super().__init__()

    def count_vowels(self):
            vowel_count = 0
            for letter in self:
                if letter in 'aeiouyAEIOUY':
                    vowel_count +=1
            return f"{self} has {vowel_count} vowels"
            


my_words = "Lots of vowels in here Ey?"
my_sentance = VowelString(my_words)
hello = "Hello, World!"
example_sentance = VowelString(hello)
print(my_sentance.count_vowels())
print(example_sentance.count_vowels())