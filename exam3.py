count = 0
total = 0

while count < 5:
    total += count
    count += 1
    if count == 3:
        continue
    total += count
    print(total)
