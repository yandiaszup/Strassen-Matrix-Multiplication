from math import ceil, log
import time
import random
import numpy as np
from statistics import mean, pstdev

def add(A, B):
    A = np.asarray(A)
    B = np.asarray(B)
    return A + B

def subtract(A, B):
    A = np.asarray(A)
    B = np.asarray(B)
    return A - B
  
def product(A, B):
    A = np.asarray(A)
    B = np.asarray(B)
    return np.matmul(A, B)

def joinQuadrants(q11,q12,q21,q22):
    top = np.concatenate((q11, q12), axis=1)
    bottom = np.concatenate((q21, q22), axis=1)
    joinedMatrix = np.concatenate((top, bottom), axis=0)

    return joinedMatrix


def strassenR(A, B):
    n = len(A)

    if n <= 2:
        return product(A, B)
    else:
        mid = n // 2
        
        a11 = A[0:mid, 0:mid]
        a12 = A[mid:n, 0:mid]
        a21 = A[0:mid, mid:n]
        a22 = A[mid:n, mid:n]

        b11 = B[0:mid, 0:mid]
        b12 = B[mid:n, 0:mid]
        b21 = B[0:mid, mid:n]
        b22 = B[mid:n, mid:n]

        m1 = strassenR(add(a11, a22), add(b11, b22)) 
        m2 = strassenR(add(a21, a22), b11) 
        m3 = strassenR(a11, subtract(b12, b22))
        m4 = strassenR(a22, subtract(b21, b11)) 
        m5 = strassenR(add(a11, a12), b22) 
        m6 = strassenR(subtract(a21, a11), add(b11, b12))
        m7 = strassenR(subtract(a12, a22), add(b21, b22)) 

        c12 = add(m3, m5) 
        c21 = add(m2, m4)
        c11 = subtract(add(add(m1, m4), m7), m5) 
        c22 = subtract(add(add(m1, m3), m6), m2)

        C = joinQuadrants(c11,c12,c21,c22)

        return C

def classicProduct(A, B):
    C = [[0 for row in range(len(A))] for col in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][i]
    return C

def randomMatrix(n):
    return np.random.randint(100, size=(n, n))

def normalizeMatrix(A):
    nextPowerOfTwo = lambda n: 2 ** int(ceil(log(n, 2)))
    n = len(A)
    m = nextPowerOfTwo(n)
    diference = m - n

    normalizedMatrix = np.pad(A, [(0, diference), (0, diference)], mode='constant')

    return normalizedMatrix

def strassen(A, B):
    return strassenR(A, B)

print("\n\n****************************STRASSEN****************************\n\n")

for i in [2,4,8,16,32,64,128,256,1024]:
    matrix1 = normalizeMatrix(randomMatrix(i))
    matrix2 = normalizeMatrix(randomMatrix(i))

    results = []

    repetitions = 30
    if i > 256:
        repetitions = 5
    
    if i > 512:
        repetitions = 3
    

    for _ in range(repetitions):
        start = time.time()
        strassen(matrix1, matrix2)
        end = time.time()
        result = end - start
        results.append(result)

    print("size: ",i)
    print("times: ",results)
    media = mean(results)
    desvio = pstdev(results)
    print("media: ", media, "seconds")
    print("desvio: ", desvio, "seconds")
    print("***************************************************")

print("\n\n****************************CLASSIC****************************\n\n")

for i in [2,4,8,16,32,64,128,256,512,1024]:
    matrix1 = normalizeMatrix(randomMatrix(i))
    matrix2 = normalizeMatrix(randomMatrix(i))

    results = []

    repetitions = 30
    if i > 256:
        repetitions = 5
    
    if i > 512:
        repetitions = 3
    

    for _ in range(repetitions):
        start = time.time()
        classicProduct(matrix1, matrix2)
        end = time.time()
        result = end - start
        results.append(result)

    print("size: ",i)
    print("times: ",results)
    media = mean(results)
    desvio = pstdev(results)
    print("media: ", media, "seconds")
    print("desvio: ", desvio, "seconds")
    print("***************************************************")
