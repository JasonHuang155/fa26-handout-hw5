"""HW5 Question 1: Using split() and join()

Please read the WordPair class below.

Please write a function called replace_word() that takes a sentence and returns a version of 
the sentence with all occurrences of specified words replaced with new specified words.

replace_word() should take a sentence and any number of WordPairs.
Its first argument should always be required (the sentence to modify).
The remaining arguments should be WordPairs. The client can pass any number of WordPairs.

Example usage:
replace_word("drums drums guitar drums", WordPair("drums", "piano")) -> "piano piano guitar piano"
replace_word(
        "drums drums guitar drums", WordPair("drums", "piano"), WordPair("guitar", "violin")) -> 
        "piano piano violin piano"
replace_word("drums drums guitar drums", WordPair("drums", "piano"), WordPair("piano", "violin")) -> 
        "violin violin guitar violin"
replace_word("drums drums guitar drums") -> "drums drums guitar drums"

Notice: Replacements are done left to right. The order of replacements matters.
For example, in the third usage example above, "drums" is replaced with "piano" first, and then 
"piano" is replaced with "violin".
"""

class WordPair:
    """Class representing a pair of words for replacement.
    """
    def __init__(self, old_word: str, new_word: str):
        """Initialize a WordPair with an old word and a new word.

        Args:
            old_word : str
                The word to be replaced.
            new_word : str
                The word to replace with.
        """
        self.old_word = old_word
        self.new_word = new_word

def replace_word(sentence: str, *word_pairs: WordPair) -> str:
    words = sentence.split()

    for pair in word_pairs:
        words = [pair.new_word if word == pair.old_word else word for word in words]

    return ' '.join(words)

if __name__ == "__main__":
    # Example usage
    print(replace_word("drums drums guitar drums", WordPair("drums", "piano")))
    print(replace_word(
        "drums drums guitar drums", WordPair("drums", "piano"), WordPair("guitar", "violin")))
    print(replace_word(
        "drums drums guitar drums", WordPair("drums", "piano"), WordPair("piano", "violin")))
    print(replace_word("drums drums guitar drums"))
