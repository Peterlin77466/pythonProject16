print("MATH EXAM")

import random

g = 0
q = 0

while True:
    q += 1
    # Two random numbers
    x = random.randint(1, 12)
    y = random.randint(1, 12)
    # Ask the question
    print("question", q, ") Calculate", x,"*", y)
    answer= x*y
    YA = int(input("put your answer"))
    if answer == YA:
        print("you are right")
        g += 10
    else:
        print("wrong")
    if q == 10:
        break


# show the result
RATE = g/10
if RATE >= 0.4:
    print("pass")
else:
    print("fail")

quit()