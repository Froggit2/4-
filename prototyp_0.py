a = range(1,21)
for n in range(3, 21):
    for x in a:
        for y in a:
            if n % (x + y) == 0:
                if x != y and y != x:
                    print(n, x, y)