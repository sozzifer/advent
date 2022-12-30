class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


my_sentence_class = Sentence("This is a sentence")

for word in my_sentence_class:
    print(word)

def sentence(sentence: str):
    for word in sentence.split():
        yield word

my_sentence_gen = sentence("This is a sentence")

for word in my_sentence_gen:
    print(word)

# print(next(my_sentence_gen))
# print(next(my_sentence_gen))
# print(next(my_sentence_gen))
# print(next(my_sentence_gen))