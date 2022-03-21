def number_length(num):
    counter = 0
    while num > 1:
        counter += 1
        num = num/10
    return counter

print(number_length(500000))