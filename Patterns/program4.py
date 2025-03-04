'''
1
22
333
4444
55555
'''

def pattern(n):
    return [[i + 1 for j in range(i + 1)] for i in range(n)]

if __name__ == '__main__':
    for row in pattern(5):
        print(*row)