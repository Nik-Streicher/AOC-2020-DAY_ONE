print(
    [int(x) * int(y) * int(z) for x in open('second_input.txt') for y in open('second_input.txt') for z in
     open('second_input.txt') if int(x) + int(y) + int(z) == 2020][0])
