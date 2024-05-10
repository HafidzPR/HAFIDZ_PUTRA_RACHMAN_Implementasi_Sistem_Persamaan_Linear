#METODE DEKOMPOSISI CROUT/CROUT DECOMPOSITION
#=======================================================

#HAFIDZ PUTRA RACHMAN ~ (21120120140096)
#METODE NUMERIK (A)
#=======================================================

def crout_decomposition(A): 
    n = len(A) 
    L = [[0] * n for _ in range(n)] 
    U = [[0] * n for _ in range(n)] 
     
    for j in range(n): 
        U[j][j] = 1 
         
        for i in range(j, n): 
            sum_val = sum(L[i][k] * U[k][j] for k in range(i)) 
            L[i][j] = A[i][j] - sum_val 
             
        for i in range(j, n): 
            sum_val = sum(L[j][k] * U[k][i] for k in range(j)) 
            U[j][i] = (A[j][i] - sum_val) / L[j][j] 
             
    return L, U 

def print_croutmatrix(matrix): 
    for row in matrix: 
        print(row) 
         

 
def forward_substitution(L, b): 
    n = len(b) 
    y = [0] * n 
     
    for i in range(n): 
        y[i] = (b[i] - sum(L[i][j] * y[j] for j in range(i))) / L[i][i] 
         
    return y 
 
def backward_substitution(U, y): 
    n = len(y) 
    x = [0] * n 
     
    for i in range(n-1, -1, -1): 
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i+1, n))) / U[i][i] 
         
    return x 
 
def crout_solvermaster(A, b): 
    L, U = crout_decomposition(A) 
    y = forward_substitution(L, b) 
    x = backward_substitution(U, y) 
    return x, L, U 
 
# Contoh
A = [[1, 2, 0], 
     [1, 4, 0], 
     [0, 9, 6]]

b = [7, 7, 7] 
 
 
solusi, L, U = crout_solvermaster(A, b) 
 
#=======================================================

print("Matriks A:") 
print("==========================")
print_croutmatrix(A) 
print("Vektor B:") 
print("==========================")
print(b) 
 
print("Matriks L:") 
print("==========================")
for row in L: 
    print(row) 
print("Matriks U:") 
print("==========================")
for row in U: 
    print(row) 
print("Vektor B:") 
print("==========================")
print(b) 
print("Solusi Crout Decomposition:") 
print("==========================")
print(solusi) 