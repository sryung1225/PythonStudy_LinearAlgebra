def readMatrixFile(fileName):
    """ (str) -> str
    파일의 내용을 읽어서 그 내용을 Python String으로 반환함.
    """
    with open(fileName, encoding="UTF8") as file:
        """matrix=file.read().split() => ['A','3','3',...]"""
        """matrix=file.read() => 원본"""
        matrix=file.read()
    return matrix

def countrow(arr):
    """ (1차원 배열) -> int
    배열의 행 수 구함.
    """
    row=int(arr[1])
    return row

def countcol(arr):
    """ (1차원 배열) -> int
    배열의 열 수 구함.
    """
    col=int(arr[2])
    return col

def divideMatrix(arr, row, col):
    """ (1차원 배열, int, int) -> 2차원 배열
    1차원 배열과 행의 수, 열의 수를 받아 2차원 배열로 정렬함.
    """
    M=[]
    for i in range(row):
        M.append([])
        for j in range(col):
            num=3+(i*col)+(j%col)
            M[i].append(float(arr[num]))
    return M
    

def det(arr, mul=1):
    """ (1차원 배열, int) -> int
    1차원 배열을 받아 det값을 구하고 반환함.
    """
    n=len(arr)
    if (n==1):
        return mul*arr[0][0]
    else:
        num=-1
        result=0
        for i in range(n):
            m=[]
            for j in range(1, n):
                temp=[]
                for k in range(n):
                    if k!=i:
                        temp.append(arr[j][k])
                m.append(temp)
            num*=-1
            result+=mul*det(m, num*arr[0][i])
        return result

def Cramer(arr):
    """ (1차원 배열) -> int
    1차원 배열을 받아 Cramer's Rule을 적용하여 해를 반환함.
    """
    n=len(arr)
    M=[]
    for i in range(n):
        M.append([])
        for j in range(n):
            M[i].append(arr[i][j])
    D=det(M)

    if (D==0):
        print("구할 수 없습니다\n")
    else:
        for r in range(n):
            MM=[]
            for i in range(n):
                MM.append([])
                for j in range(n):
                    if (j==r):
                        MM[i].append(arr[i][n])
                    else:
                        MM[i].append(arr[i][j])
            print("x", r+1, "=", det(MM)/D)
        print("\n")


print("3개의 linear system을 한번에 실행합니다.")
print("행렬을 입력하시오. (차례로 matrixA.py /n matrixB.py /n matrixC.py /n)")
matrixA=readMatrixFile(input())
matrixB=readMatrixFile(input())
matrixC=readMatrixFile(input())
print("")

arrA=matrixA.split()
rowA=countrow(arrA) #A의 행 수
colA=countcol(arrA)+1 #A의 열 수+1(b))
arrAA=divideMatrix(arrA, rowA, colA) #2차원 배열로 정리한 A

arrB=matrixB.split()
rowB=countrow(arrB) #B의 행 수
colB=countcol(arrB)+1 #B의 열 수+1(b))
arrBB=divideMatrix(arrB, rowB, colB) #2차원 배열로 정리한 B

arrC=matrixC.split()
rowC=countrow(arrC) #C의 행 수
colC=countcol(arrC)+1 #C의 열 수+1(b))
arrCC=divideMatrix(arrC, rowC, colC) #2차원 배열로 정리한 C

#print("행렬 A : ", arrAA)
#print("A의 determinant : ", det(arrAA))
print("A의 해 : ")
Cramer(arrAA)

print("B의 해 : ")
Cramer(arrBB)

print("C의 해 : ")
Cramer(arrCC)