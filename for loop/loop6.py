M =int(input('Width? '))
N =int(input('Height? '))
print('*' * M)

for i in range(N - 2):
    print('*' + ' ' * (M - 2) + '*')

print('*'*M)