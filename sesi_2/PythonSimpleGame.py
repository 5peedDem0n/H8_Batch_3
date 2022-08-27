import random

number = [0,1,2,3,4,5,6,7,8,9]
com = random.choice(number)
me = 10
trying = 0
while me != com:
    me = input('Pick any number! (0~9)\n')
    me = int(me)
    if me > com:
        print("Pilihan anda terlalu besar!")
    elif me < com:
        print("Pilihan anda terlalu kecil")
    else:
        print("Tebakan anda benar")
    trying += 1
    print(f"Percobaan {trying} gagal!")
    if trying == 3:
        print("GAME OVER")
        break
    
