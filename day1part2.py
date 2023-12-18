filename = 'input.txt'
answer = 0

with open(filename, 'r') as file:
    line = file.readline()
    while line:
        occurances = []
        l = line.strip()

        occurances.append([l.find('one'), 1]) if l.find('one') != -1 else None
        occurances.append([l.find('two'), 2]) if l.find('two') != -1 else None
        occurances.append([l.find('three'), 3]) if l.find('three') != -1 else None
        occurances.append([l.find('four'), 4]) if l.find('four') != -1 else None
        occurances.append([l.find('five'), 5]) if l.find('five') != -1 else None
        occurances.append([l.find('six'), 6]) if l.find('six') != -1 else None
        occurances.append([l.find('seven'), 7]) if l.find('seven') != -1 else None
        occurances.append([l.find('eight'), 8]) if l.find('eight') != -1 else None
        occurances.append([l.find('nine'), 9]) if l.find('nine') != -1 else None


        occurances.append([l.rfind('one'), 1]) if l.rfind('one') != -1 else None
        occurances.append([l.rfind('two'), 2]) if l.rfind('two') != -1 else None
        occurances.append([l.rfind('three'), 3]) if l.rfind('three') != -1 else None
        occurances.append([l.rfind('four'), 4]) if l.rfind('four') != -1 else None
        occurances.append([l.rfind('five'), 5]) if l.rfind('five') != -1 else None
        occurances.append([l.rfind('six'), 6]) if l.rfind('six') != -1 else None
        occurances.append([l.rfind('seven'), 7]) if l.rfind('seven') != -1 else None
        occurances.append([l.rfind('eight'), 8]) if l.rfind('eight') != -1 else None
        occurances.append([l.rfind('nine'), 9]) if l.rfind('nine') != -1 else None

        occurances = [list(t) for t in set(tuple(row) for row in occurances)]

        for i, c in enumerate(l):
            if c.isdigit():
                occurances.append([i, int(c)])
        if (len(occurances) == 1):
            answer += occurances[0][1] + (occurances[0][1] * 10)
        else:
            answer += max(occurances)[1] + (10 * min(occurances)[1])

        line = file.readline()

print(answer)
