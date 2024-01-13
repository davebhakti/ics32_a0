num = int(input())
space = '  '
for i in range(num):
    print("+-+")
    print(space * i + "| |")
    print(space * i + "+-", end='')
print("+")
