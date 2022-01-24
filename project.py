#task 1

sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
sentence = sentence.split()
word = "COUNTRY"
positions = []

for i in range(len(sentence)):
    if sentence[i] == word:
        positions.append(i+1)

print(positions)

sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
sentence = sentence.split()
word = "YOUR"
positions = []

for i in range(len(sentence)):
    if sentence[i] == word:
        positions.append(i+1)

        print(positions)