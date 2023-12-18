filename = 'test-input.txt'
answer = 0

with open(filename, 'r') as file:
    line = file.readline()
    while line:
        stack = []
        for char in line.strip():
            if char.isdigit():
                stack.append(char)
        if len(stack) == 1:
            answer += int(stack[0] + stack[0])
        else:
            answer += int(stack[0] + stack[len(stack) - 1])
        line = file.readline()
print(answer)
