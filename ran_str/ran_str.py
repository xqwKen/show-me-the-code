# coding=utf-8

import random


#字符集
L = [chr(i + 65) for i in range(26)] + [chr(i + 97) for i in range(26)] + [chr(i + 48) for i in range(10)]

ans=""
for i in range(4):
    ans += random.choice(L)
print ans
def save(filename, contents):
    fh = open(filename, 'w')
    fh.write(contents)
    fh.close()
save('random.txt', ans)