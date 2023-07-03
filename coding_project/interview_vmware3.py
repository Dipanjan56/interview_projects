def open_file():
    with open('text2.txt') as file:
        word_dict = {}
        for line in file:
            print(line, end='')
            word_list = line.split(' ')
            for word in word_list:
                word = word.replace('\n', '')
                word_dict.setdefault(word, 0)
                word_dict[word] += 1
        print(word_dict)
        print(sorted(word_dict.items(), key=lambda x:x[1], reverse=True))

if __name__ == '__main__':
    open_file()
