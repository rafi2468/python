replacers = { "a": 0, "e":1, "i":2, "o":2, "u": 3 }  
def encrypt(word):
    word = word[::-1]
    return word

def replace(word):  
    result = ''   
    for item in word:
        if item in replacers.keys():
            result += replacers[item]

print(encrypt("apple"))
 