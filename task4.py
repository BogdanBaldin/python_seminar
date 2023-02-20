n = int(input('Введите 1-ю сторону: '))
m = int(input('Введите 2-ю сторону: '))
k = int(input('Введите кол-во долек: '))
if k < n*m and (k % n == 0 or k % m == 0):
    print('Yes')
else: 
    print('No')