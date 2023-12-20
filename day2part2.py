filename = 'input.txt'
answer = 0
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        redCount, blueCount, greenCount = 0, 0, 0
        runningRed, runningBlue, runningGreen = 999, 999, 999
        words = line.split()
        for index, word in enumerate(words):
            if "green" in word:
                if int(words[index -1]) > greenCount: greenCount = int(words[index -1])
            if "red" in word:
                if int(words[index -1]) > redCount: redCount = int(words[index -1])
            if "blue" in word:
                if int(words[index -1]) > blueCount: blueCount = int(words[index -1])
        answer += (redCount * greenCount * blueCount)
        line = file.readline()
    print(answer)
