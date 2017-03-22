__author__ = 'student'

def f1(a, b):

    return a*b, a+b, a-b, a/b, a>b, a<b, a %  b





def compare_a_b(a=1, b=1, checkForZero=True):
    if checkForZero:
            if b!=0:
                return a*b, a+b, a-b, a/b, a>b, a<b, a %  b
            else:
                return 0, 0, 0, 0, 0, 0
    else:
        return a*b, a+b, a-b, a/b, a>b, a<b, a %  b

print f1(3,2) * 5

