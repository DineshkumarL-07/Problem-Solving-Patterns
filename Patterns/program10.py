'''
*
**
***
****
*****
****
***
**
*
'''

def pattern(n):
    ans = []
    for i in range((n * 2) - 1):
        temp = []
        if i < n:
            temp = ["*" * (i + 1)]
            ans.append(temp)
        else:
            temp = ["*" * ((n * 2) - i - 1)]
            ans.append(temp)
    
    return ans
            

if __name__ == '__main__':
    res = pattern(7)
    for row in res:
        print(*row)