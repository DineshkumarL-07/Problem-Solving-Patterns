'''
*
**
***
****
*****
'''

def pattern(n):
    return ["*" * (i + 1) for i in range(n)]

if __name__ == '__main__':
    res = pattern(5)
    print("\n".join(res))