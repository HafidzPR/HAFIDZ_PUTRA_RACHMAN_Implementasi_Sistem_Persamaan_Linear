#METODE DEKOMPOSISI LU GAUSS/LU GAUSS DECOMPOSITION
#=======================================================

#HAFIDZ PUTRA RACHMAN ~ (21120120140096)
#METODE NUMERIK (A)
#=======================================================

# Nilai Matrix A 
print("Nilai Matrix A ")
print("==========================")
A = [[1, 2, 0], 
     [1, 4, 0], 
     [0, 9, 6]] 
# Vector B 
B = [2, 1, -2] 
 
# buat fungsi untuk menampilkan elemen matriks
def show(matrix): 
    n = len(matrix) 
    for row in range(n): 
      for col in range(n): 
        print('%.2f' % matrix[row][col], end="\t") 
      print("") 
show(A) 
 
# dapatkan jumlah baris dari A
n = len(A) 

# buat matriks nol dari L dan U
L = [[0 for row in range(n)] 
   for col in range(n)] 
U = [[0 for row in range(n)] 
   for col in range(n)] 
 
for p in range(n): 
  # upper matrix 
  for j in range(p,n): 
    # penjumlahan L(p,k)*U(k,j) 
    sum = 0 
    for k in range(p): 
      sum = sum + L[p][k]*U[k][j] 
    U[p][j] = A[p][j] - sum 
 
# matriks rendah
q = p 
for i in range (q,n): 
  if (i==q): 
    # diagonal L 
    L[i][q]=1 
  else: 
    # penjumlahan L(i,k)*U(k,q) 
    sum = 0 
    for k in range(q): 
      sum = sum + L[i][k]*U[k][q] 
    L[i][q] = (A[i][q] - sum)/U[q][q] 
 
def decomposition(A): 
  # dapatkan jumlah baris dari A
  n = len(A) 
  # buat matriks nol dari L dan U
  L = [[0 for row in range(n)] 
       for col in range(n)] 
  U = [[0 for row in range(n)] 
       for col in range(n)] 
   
  for p in range(n): 
    # matriks atas
    for j in range(p,n): 
      # penjumlahan L(p,k)*U(k,j) 
      sum = 0 
      for k in range(p): 
        sum = sum + L[p][k]*U[k][j] 
      U[p][j] = A[p][j] - sum 
  # matriks rendah
    q = p 
    for i in range (q,n): 
      if (i==q): 
        # diagonal L
        L[i][q]=1 
      else: 
        # penjumlahan L(i,k)*U(k,q) 
        sum = 0 
        for k in range(q): 
          sum = sum + L[i][k]*U[k][q] 
        L[i][q] = (A[i][q] - sum)/U[q][q] 
  return L, U 
 
#=======================================================

# Penyelesaian Solusi ~ Inverse Matrix:
# Nilai Matrix A 
A = [[1, 2, 0], 
     [1, 4, 0], 
     [0, 9, 6]] 
# Hitung LOWER (L) & UPPER (U)    
L, U = decomposition(A) 
# show LOWER (L) & UPPER (U)  
print("Matrix LOWER (L) :") 
print("==========================")
show(L) 
print("\nMatrix UPPER (U) :") 
print("==========================")
show(U)