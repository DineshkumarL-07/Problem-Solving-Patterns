'''
12345
1234
123
12
1
'''

def pattern(n):
    return [[j + 1 for j in range(n-i)] for i in range(n)]

if __name__ == '__main__':
    for row in pattern(5):
        print(*row)