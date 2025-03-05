'''
        *
       ***
      *****
     *******
    *********
'''

def pattern(n):
    ans = []
    star_count = 1
    for i in range(n):
        row = []
        for j in range(1):
            row.append(" " * (n-i-1))
            row.append("*" * star_count)
            star_count += 2
        ans.append(row)
    
    return ans

if __name__ == '__main__':
    res = pattern(7)
    for row in res:
        print(*row)