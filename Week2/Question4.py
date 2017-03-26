def harmonic_list(n):
    h = 0
    for i in range(1, n + 1):
        h += 1 / i
    yield h

for each in harmonic_list(5):
    print(each)