with open('greet.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print("\033[H\033[J", end="")
    print()
    for line in lines:
        print("\033[35m",line.strip('\n').strip('\r'))
    print("\033[36m","human director actor")
    print()
    print("\033[37m" , "blutgruppe digital 2024")
    print("\033[37m")
    print()
    print()