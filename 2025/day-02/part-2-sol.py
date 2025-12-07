with open('id.txt') as f:
    ids = [s.strip() for s in f.read().split(',') if s.strip() and '-' in s]

    count = 0
    for one_id_str in ids:
        start, end = one_id_str.split('-')
        
        for number in range(int(start), int(end) + 1):
            num_str = str(number)
            for pattern_len in range(1, len(num_str) // 2 + 1):
                if len(num_str) % pattern_len == 0:
                    pattern = num_str[:pattern_len]
                    repeats = len(num_str) // pattern_len

                    if pattern * repeats == num_str:
                        count += number
                        break

    print(count)
