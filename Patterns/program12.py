'''
1      1
12    21
123  321
12344321
'''

def pattern(n):
    ans = []
    for i in range(n):
        temp = []
        for j in range(n*2):
            if j < n:
                if j < i + 1:
                    temp.append(str(j + 1))
                else:
                    temp.append(" ")
            else:
                if j < (n * 2) - i - 1:
                    temp.append(" ")
                else:
                    temp.append(str((n*2) - j))
        ans.append("".join(temp))

    return ans

if __name__ == '__main__':
    res = pattern(4)
    for row in res:
        print(*row)