def password_generation(n):
    result = None
    medl = None
    count = 0
    if n % 2 != 0:
        medl = (n // 2) + 1
    else:
        medl = n
    for i in range(1,medl):
        for j in range(i+1,n):
            if count == 0:
                if n % (i + j) == 0:
                    result = (str(i) + str(j))
                    count += 1
            else:
                if n % (i + j) == 0:
                    result += (str(i) + str(j))

    print(result)
    return
password_generation(int(input('Введите число из камня: ')))
