'''
*
**
***
****
*****
'''

def pattern(n):
    return ["*" * (i+1) for i in range(n)]

if __name__ == '__main__':
    print("\n".join(pattern(5)))