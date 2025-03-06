'''
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
'''

def pattern(n):
    ans = []
    start = 1
    for i in range(n):
        temp = []
        start = 1 if i % 2 == 0 else 0
        for j in range(i + 1):
            temp.append(f'{start} ')
            start = 0 if start == 1 else 1
        ans.append(temp)
    return ans

if __name__ == '__main__':
    res = pattern(5)
    for row in res:
        print(*row)