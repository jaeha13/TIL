import random
while True:
    pairNum1 = random.randint(1, 6)
    pairNum2 = random.randint(1, 6)
    if pairNum1 == pairNum2:
        print("게임 끝")
        break
    elif pairNum1 < pairNum2:
        print("pairNum1이 pariNum2 보다 작다.")
    else:
        print("pairNum1이 pariNum2 보다 크다.")
