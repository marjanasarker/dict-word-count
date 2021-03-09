# put your code here.
print(__name__)
def count_words(filename):
    unique_words_count = {}
    all_words = []

    text_body = open(filename)
    for line in text_body:
        line = line.rstrip()
        words = line.split(' ')
        all_words.extend(words)
    #print (all_words)

    for word in all_words:
        unique_words_count[word] = unique_words_count.get(word, 0) + 1
    for unique_word, count in unique_words_count.items():
        print(f'{unique_word} {count}')
    return unique_words_count
    

count_words('test.txt')

