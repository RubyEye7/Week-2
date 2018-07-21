def F(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n*F(n-1)




def F_loop():
    b = 0
    n = int(input("Enter number: "))
    fact = 1
    while n > 0:
        fact = fact * n
        b += 1
        print(b)
        n -= 1
    print(fact)

F_loop()
