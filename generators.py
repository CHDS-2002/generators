import os

os.system('COLOR B')


def all_variants(text):
    sub = ''
    i = j = 0
    k = 1

    while sub != text:
        sub = text[i:j + k]
        i += 1
        j += 1

        if j + k - 1 == len(text):
            k += 1
            i = j = 0

        yield sub


a = all_variants("abc")

for i in a:
    print(i)

try:
    os.system('PAUSE')
except:
    os.system('CLS')
