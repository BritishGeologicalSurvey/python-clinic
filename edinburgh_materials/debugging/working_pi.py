# Calculate an estimate of  pi using the Leibnitz method
#  (don't actually do this in real code)

import math

def pi(iterations):
    
    pi = 4.0
    k = 3.0
    est = 1.0
    while 1 < iterations:
        est = est - (1/k) + 1/(k+2)
        iterations = iterations - 1
        k += 4
    try:
        k.isnumeric()    
    except ZeroDivisionError as exc:
        print(exc)
    except AttributeError as exc:
        kay = str(k)
        print(kay.isnumeric())
        
    
    return pi * est

if __name__=="__main__":
    pi_guess = pi(10)
    print(pi_guess)
    good_pi = math.pi
    print(good_pi)