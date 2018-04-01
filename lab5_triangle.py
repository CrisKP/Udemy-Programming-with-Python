# Create an incrementing triangle of hashes

x = ''
for i in range(7):
    x += '#'
    print(x)


x = '#'
for i in range(7):
    x = i * '#'
    print(x)
