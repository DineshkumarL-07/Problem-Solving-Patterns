# TakeUForward Pattern Problems

'''
*****
*****
*****
*****
*****
'''

# Program

def pattern(n):
    return ["*"*n for i in range(n)]

if __name__ == '__main__':
    res = pattern(7)
    print("\n".join(res))