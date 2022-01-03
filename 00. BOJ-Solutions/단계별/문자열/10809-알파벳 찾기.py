word = input()
for i in range(0, 26):
    try:
        print (word.index(chr(97+i)), end = ' ')
    except:
        print (-1, end = ' ')