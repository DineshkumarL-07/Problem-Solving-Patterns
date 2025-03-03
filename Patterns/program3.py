'''
1
12
123
1234
12345
'''

def pattern(n):
    ans = [[i + 1 for i in range(j+1)] for j in range(n)]
    return ans


if __name__ == '__main__':
    res = pattern(5)
    for row in res:
        print(*row)