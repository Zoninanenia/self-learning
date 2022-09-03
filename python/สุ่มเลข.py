#สุ่มเลข 0-9 โดย ให้ 9 ได้ยากสุด
import random
x = random.randint(0,9)
if x >= 0 :
    print(x)
elif (x == 9):
    print(random.randint(0,9))
