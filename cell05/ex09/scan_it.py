import sys
item_list = sys.argv
item_list.pop(0)
i = len(item_list)
if i <= 1:
    print("none")
else:
    word = sys.argv[0]
    sentence = sys.argv[1:]
    word_count = sentence.count(word)
    print(word_count)