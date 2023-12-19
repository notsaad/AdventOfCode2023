filename = 'input.txt'
answer = 0
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        validGame = True
        redCount, blueCount, greenCount = 0, 0, 0
        words = line.split()
        gameNum = words[1][:-1]
        for index, word in enumerate(words):
            if ("green" in word):
                if int(words[index - 1]) > greenCount: greenCount = int(words[index - 1])
                #print(f"Green Number: {words[index - 1]}, Count: {greenCount}")
            if ("red" in word):
                if int(words[index - 1]) > redCount: redCount = int(words[index - 1])
                #print(f"Red Number: {words[index - 1]}, Count: {redCount}")
            if ("blue" in word):
                if int(words[index - 1]) > blueCount: blueCount = int(words[index - 1])
                #print(f"Blue Number: {words[index - 1]}, Count: {blueCount}")
        if redCount <= 12 and greenCount <= 13 and blueCount <= 14: answer += int(gameNum)
        #print(f"Game Number: {gameNum}")
        line = file.readline()
    print(answer)
