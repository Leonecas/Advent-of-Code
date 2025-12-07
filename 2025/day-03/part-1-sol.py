with open('joltage.txt') as f:
    total = 0
    for bank in f:
        bank = bank.strip()
        if bank:
            digs = [int(num) for num in bank]
            max_joltage = 0
            
            for i in range(len(digs)):
                for j in range(i + 1, len(digs)):
                    joltage = digs[i] * 10 + digs[j]
                    if joltage > max_joltage:
                        max_joltage = joltage

            total += max_joltage
    print(total)
