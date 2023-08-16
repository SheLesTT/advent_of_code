from math import hypot
with open("../task/task1.txt", "r") as f:
    data = f.read()

# print(type(data))

data = data.replace(",","")

data = data
print(data)
turns = data.split()



class imaginaryNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __mul__(self, number):
        if isinstance(number,(int, float)):
            return imaginaryNumber(self.real * number, self.imaginary * number)
        if isinstance(number, imaginaryNumber):
            return imaginaryNumber(self.real * number.real - self.imaginary * number.imaginary, self.real * number.imaginary + self.imaginary * number.real)

    def __add__(self, number):
        return imaginaryNumber(self.real + number.real, self.imaginary + number.imaginary)
    def __repr__(self):
        return f"{self.real} + {self.imaginary}i"

    def __eq__(self, other):
        if isinstance(other, imaginaryNumber):
            return self.real == other.real and self.imaginary == other.imaginary
        return False
    def __hash__(self):
        return hash((self.real, self.imaginary))



move_vector =imaginaryNumber(0,1)
pos = imaginaryNumber(0,0)
position = set([imaginaryNumber(0,0)])
for turn in turns:
    match turn[0]:
        case "R":
            move_vector = move_vector * imaginaryNumber(0,-1)
        case "L":
            move_vector = move_vector * imaginaryNumber(0,1)
        case _: print("some")
    for i in range(int(turn[1:])):
        pos = pos + move_vector
    # pos = pos + move_vector*int(turn[1:])
        if pos not in position:
            position.add(pos)
        else:
            print(pos)
            print("I was there before", abs(pos.real)+abs(pos.imaginary))

print(position)

print(pos.real+pos.imaginary)