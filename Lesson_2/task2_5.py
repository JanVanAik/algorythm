counter = 0
for i in range(32, 128):
    if counter == 9:
        counter -= 9
        print((i, chr(i)), end='\n')
    else:
        print((i, chr(i)), end='')
        counter += 1
