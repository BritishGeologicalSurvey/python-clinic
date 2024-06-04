# Calculate an estimate pi using the inifinite sum 
# iterative method   (don't actually do this in real code)

def pi(iterations):
    
    pi = 4.0
    k = 3.0
    est = 1.0
    while 1 < iterations:
        est = est - (1/k) + 1/(k+2)
        iterations = iterations - 1
        k += 4

    return pi * est

if __name__=="__main__":
    pi_guess = pi(10000)
    print(pi_guess)