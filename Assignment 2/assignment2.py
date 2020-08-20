def readMatrixFile(fileName):
    """ (str) -> str
    파일의 내용을 읽어서 그 내용을 Python String으로 반환함.
    """
    with open(fileName) as file:
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
            M[i].append(int(arr[num]))
    return M




def det_two(arr_two):
    """ (int) -> int
    열과 행의 값이 2인 행렬일 때, determinant 값을 구함
    """
    res = arr_two[0][0]*arr_two[1][1] - arr_two[0][1]*arr_two[1][0]
    return res

def M(arr,size,num):
    """ (2차원 배열) -> 2차원 배열
    Minor를 계산함
    """
    M=[]
    M_tmp=[]
    for i in range(size-1):
        for j in range(num-1):
            M_tmp.append(arr[i+1][j])
        for j in range(size-num):
            M_tmp.append(arr[i+1][j+num])
        M.append(M_tmp)
        M_tmp=[]
    return M

def Big_M(arr, size):
    """ (2차원 배열) -> 2차원 배열
    Minor를 계산함
    """
    B_M=[]
    for i in range(size):
        B_M.append(M(arr,size,i+1))
    return B_M


def det_three(arr_three):
    matrix=Big_M(arr_three, 3)
    
    cofactor=[arr_three[0][0]*det_two(matrix[0]), arr_three[0][1]*det_two(matrix[1]), arr_three[0][2]*det_two(matrix[2])]

    result=0
    for i in range(3):
        if(i%2 == 0):
            result+=cofactor[i]
        else:
            result-=cofactor[i]

    return result 

def det_four(arr_four):
    matrix=Big_M(arr_four, 4)

    cofactor=[arr_four[0][0]*det_three(matrix[0]), arr_four[0][1]*det_three(matrix[1]), arr_four[0][2]*det_three(matrix[2]), arr_four[0][3]*det_three(matrix[3])]

    result=0
    for i in range(4):
        if(i%2 == 0):
            result+=cofactor[i]
        else:
            result-=cofactor[i]
    return result 

def det_five(arr_five):
    matrix=Big_M(arr_five, 5)
    
    cofactor=[arr_five[0][0]*det_four(matrix[0]), arr_five[0][1]*det_four(matrix[1]), arr_five[0][2]*det_four(matrix[2]), arr_five[0][3]*det_four(matrix[3]), arr_five[0][4]*det_four(matrix[4])]

    result=0
    for i in range(5):
        if(i%2 == 0):
            result+=cofactor[i]
        else:
            result-=cofactor[i]

    return result 






print("행렬을 입력하시오. (파일명.확장자)")
matrixA=readMatrixFile(input())
arrA=matrixA.split()
rowA=countrow(arrA) #A의 행 수
colA=countcol(arrA) #A의 열 수
arrAA=divideMatrix(arrA, rowA, colA) #2차원 배열로 정리한 A

if (rowA != colA):
    print("square matrix가 아니므로 계산을 하지 않습니다.")
else:
    print("파일 속 행렬 : ", arrAA)
    print("행렬의 determinant : ", end="")
    
    if colA == 2:
        print(det_two(arrAA))
    elif colA == 3:
        print(det_three(arrAA))
    elif colA == 4:
        print(det_four(arrAA))
    elif colA == 5:
        print(det_five(arrAA))
