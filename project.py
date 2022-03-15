def averageoflist():
    total = 0
    end = False
    count = 0
    names = []
    scores = []
    while end == False:
        name = input("enter name: ")
        score = int(input("enter score: "))
        names.append(name)
        scores.append(score)
        total += score
        count += 1
        cont = input("Do you want to add another score Y/N: ")
        if cont == 'N':
            end = True
        highest = max(scores)
        lowest = min(scores)
        studentHighest = scores.index(highest)
        studentLowest = scores.index(lowest)
    avg = total / count
    print(names[studentHighest], highest, names[studentLowest], lowest)
    searched = int(input("Which score do you want to search for: "))
    for i in range(len(scores)):
        if searched == scores[i]:
            print("Found", names[i], scores[i])
            
    
    return avg

print(averageoflist())





 





