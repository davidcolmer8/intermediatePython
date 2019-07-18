import string

sonnets = open("../data/sonnets.txt").readlines()
word_set= set(elt.strip() for elt in open("../data/sowpods.txt"))
sonnetWords = set()

def stripPunctuation(word):
    #remove surrounding punctionation 
    word.replace("-"," ")
    apostropheIndex= word.find("'")
    if apostropheIndex != -1:
        return None
    return word.strip(string.punctuation)

for line in sonnets:
    lineWords = line.replace("-", " ").strip().split()

    if len(lineWords) <= 1:
        continue
    for word in lineWords:
        stripped = stripPunctuation(word)
        if stripped and len(stripped)>1:
            sonnetWords.add(stripped.upper())
sonnetWords = list(sonnetWords)
sonnetWords.sort()


f = open("../data/sonnetWords.txt","w")
for word in sonnetWords:
    f.write(word +"\n")
f.close()

print([word for word in sonnetWords if word == word[::-1]])