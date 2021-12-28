# This code accompanies Julia's Deep Dive into Elementary Long Division

# Takes in int A and outputs list a of digits of A
def listify(A):
    strA = str(A)
    n = len(strA) - 1
    a = [int(strA[i]) for i in range(0, n+1)]
    return a

def long_div(A, d):

    if A < d:
        return (0, A)

    a = listify(A)
    n = len(a) - 1
    
    Q = 0
    
    # Find earliest # k such that a0...ak-1 >= d. 
    k = 1 
    X = a[0] # X is used to represent the fancy A in the paper
    while X < d: 
        X = int( str(X) + str(a[k]) ) 
        k += 1

    # Loop
    for i in range(k-1, n+1):
         # How many times does d go into X?
        q = 0
        while (q+1) * d <= int(X): 
            q += 1
        
        # Set Q
        Q = Q*10 + q
        
        # Set X
        X = X - d*q
        if i < n:
            X = X*10 + a[i+1]
    
    # Set rem
    R = X
    
    # Ret answers
    return (Q, R)

# For testing
"""
import math
for A in range(0, 1000):
    for d in range(1, 1000):
        if math.floor(A / d) != long_div(A, d)[0]:
            print("ERROR WITH", "A =", A, ", d =", d)
            print("EXPECTED Q:", math.floor(A / d), "; GOT:", long_div(A,d))
            quit()

print("Tests done.")
"""
        
    