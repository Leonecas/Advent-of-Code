Day 1, Part 1: Secret Entrance

with open('input.txt') as f:
    position = 50 
    count = 0
    
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'L':
            position = (position - distance) % 100
        elif direction == 'R':
            position = (position + distance) % 100
        
        # Count if position is 0 after this move
        if position == 0:
            count += 1
    
    print(count)
