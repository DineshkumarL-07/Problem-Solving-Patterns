'''
        *
       ***
      *****
     *******
    *********
    *********
     *******
      *****
       ***
        *
'''

def pattern(n):
    ans = []
    for i in range(n * 2):
        row = []
        if i < n:
            for j in range(1):
                val = n - i - 1
                star = (i * 2) + 1
                row.append(" " * val)
                row.append("*" * star)
            ans.append(row)
        else:
            for j in range(1):
                row.append(" " * val)
                row.append("*" * (star))
                star -= 2
                val += 1
            ans.append(row)
    return ans

if __name__ == '__main__':
    res = pattern(7)
    for row in res:
        print(*row)