# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

lines = []
def read_file_content(filename):
    # [assignment] Add your code here
    with open('story.txt') as file:
        lines = file.readlines()
        return lines
   
    


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    word_count = 0
    for line in text: 
        print(line)       
        for word in line:
            print (word)
            word_count = word.count(word) 
        print({word: word_count})         
        return { word: word_count}    

    # return {"as": 10, "would": 20}

count_words()