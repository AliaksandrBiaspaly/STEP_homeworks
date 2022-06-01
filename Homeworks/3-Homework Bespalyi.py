# Factorial
n = int(input('Enter factorial number : '))
result = 1
for i in range(n):
    result *= i+1
print('Factorial ', n, ' is ', result)