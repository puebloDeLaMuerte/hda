import time

with open('greet.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print("\033[H\033[J", end="")
    print()
    for line in lines:
        time.sleep(0.06)
        print("\033[35m",line.strip('\n').strip('\r'))
    time.sleep(0.4)
    print("\033[36m","human director actor")
    print()
    time.sleep(1)    
    print("\033[37m" , "blutgruppe digital 2024")
    print("\033[37m")
    print()
    print()