def test_result(word):
    word = word[::-1]
    return word

def replace(word): 
    replacers = { "a": 0, "e":1, "i":2, "o":2, "u": 3 }      
    result = ''   
    for item in word:
        if item in replacers.keys():
            result = result + str(replacers[item])
        else:
            result = result + item
    return result + "aca"
 
word = test_result("apple")
print(replace(word))