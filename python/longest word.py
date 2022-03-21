import string 


def find_longest_rec(sentence):
    sentence = sentence.translate(str.maketrans('','',string.punctuation))
    myList = sentence.split()
    maximum = 0
    max_word = ""
    
        if len(word) > maximum:
            maximum = len(word)
            max_word = word

    print(max_word)

print(find_longest_rec("Forgetfulness is by all means powerless!"))
    
    
