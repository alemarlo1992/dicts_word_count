# put your code here.
def counts_word(file):
    """DocString: Function that counts the words in file test.txt"""
    file = open(file)
    words_count = {}

    for line in file:
        line = line.rstrip()
        line = line.split()

        for word in line:
            words_count[word] = words_count.get(word, 0) + 1

    for word, number in words_count.items():
        print('{} : {}'.format(word, number))

counts_word("test.txt")
