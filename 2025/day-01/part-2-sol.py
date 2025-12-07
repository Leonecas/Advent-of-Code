# Day 1, Part 2:

with open('input.txt') as f:
    position = 50
    count = 0

    for line in f:
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'L':
            for x in range(distance):
                position = (position - 1) % 100
                if position == 0:  
                    count += 1
        else:  
            for y in range(distance):
                position = (position + 1) % 100
                if position == 0:  
                    count += 1
    print(count)
