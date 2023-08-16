with open("../task/task2.txt", "r") as f:
    data = f.read()


paths = data.split("\n")
paths = paths[:-1]
pos = [1, 3]
code=[]

field = [[0, 0, 0, 0,0, 0,0],[0, 0, 0, 1, 0, 0,0], [0, 0, 2, 3, 4, 0,0], [0, 5, 6, 7, 8, 9,0], [0,0, "A", "B", "C", 0, 0], [0, 0, 0, "D", 0, 0,0],[0, 0, 0, 0, 0, 0,0]]
def in_bounds(pos):
    if field[pos[1]][pos[0]] != 0:

        return True
    return False


for path in paths:

    for letter in path:
        print(pos, letter, "pos letter")
        # print(cur)
        match letter:
            case "R":
                pos[0] += 1
                if not in_bounds(pos):
                    pos[0] -= 1

            case "L":
                pos[0] -= 1
                if not in_bounds(pos):
                    pos[0] += 1

            case "U":
                pos[1] -= 1
                if not in_bounds(pos):
                    pos[1] += 1

            case "D":
                pos[1] += 1
                if not in_bounds(pos):
                    pos[1] -= 1
    print("pos", pos,letter)
    code.append(field[pos[1]][pos[0]])

print(code)