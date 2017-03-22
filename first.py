def f1(a = 3 , b = 2,checkForZero = False):
    if checkForZero:
        if b != 0:
            return a<b,a>b,a==b,a!= b
        else:
            return 0,0,0,0,0,0,0,0
    else:
        return a * b, a + b, a / b, a - b, a < b, a > b, a == b, a != b


def compare_a_b(a = 3,b = 2):
    if a > b:
        print ('a is greater than b')
    elif a == b:
        print('a is equal b')
    elif a != b:
        print('a is not equal b')
    elif a >= b:
        pass
    elif a <= b:
        pass
    else:
        print('a is less than b')
compare_a_b()
a,b,c,d,e,f,g,h = f1()
print (a,b,c,d,e,f,g,h)
