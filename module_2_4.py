numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = {}
for i in range(len(numbers)):
    count = 0
    if numbers[i] == 1:
        continue
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            break
        elif numbers[i] % numbers[j] == 0:
            count += 1
            if count > 2:
                break
        else:
            continue
    if count > 1:
        is_prime.update({
            numbers[i]: False
        })
    else:
        is_prime.update({
            numbers[i]: True
        })
        
for i in is_prime:
    if is_prime[i] == True:
        primes.append(i)
    else:
        not_primes.append(i)

print(f'Primes: {primes}')
print(f'Not primes: {not_primes}')

