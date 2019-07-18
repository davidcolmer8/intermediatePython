import time

myWords = [elt.strip() for elt in open('../data/sonnet_words.txt', "r").readlines()]
wordList = [elt.strip() for elt in open('../data/sowpods.txt', "r").readlines()]
wordDict = dict((elt,1) for elt in wordList)
wordSet = set(wordDict)

counter = 0
start = time.time()
for word in myWords:   
    if word not in wordSet:
        print(word)
        counter += 1
stop = time.time()

print(f"Total new words {counter}")
print(f"Time elapsed {stop - start}")


