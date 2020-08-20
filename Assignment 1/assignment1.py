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

def scalarmult(matrix,row,col,sca):
    result=[]
    result_tmp=[]

    for i in range(row):
        for j in range(col):
            result_tmp.append(matrix[i][j] * sca)
        result.append(result_tmp)
        result_tmp = []
    return result




print("행렬 A를 입력하시오. (파일명.확장자)")
matrixA=readMatrixFile(input())
arrA=matrixA.split()
rowA=countrow(arrA) #A의 행 수
colA=countcol(arrA) #A의 열 수
arrAA=divideMatrix(arrA, rowA, colA) #2차원 배열로 정리한 A

print("행렬 B를 입력하시오. (파일명.확장자)")
matrixB=readMatrixFile(input())
arrB=matrixB.split()
rowB=countrow(arrB) #B의 행 수
colB=countcol(arrB) #B의 열 수
arrBB=divideMatrix(arrB, rowB, colB) #2차원 배열로 정리한 B

print("행렬 C를 입력하시오. (파일명.확장자)")
matrixC=readMatrixFile(input())
arrC=matrixC.split()
rowC=countrow(arrC) #C의 행 수
colC=countcol(arrC) #C의 열 수
arrCC=divideMatrix(arrC, rowC, colC) #2차원 배열로 정리한 C

"""
print(arrAA)
print(arrBB)
print(arrCC)
"""

# 1) 2A + 3B + 5C
# 2) 2A + ABC
# 3) 5C + AB + BC

while True:

    print("실행할 연산을 입력하시오. (종료를 원할 시 quit)")
    fomula=list(input())
    #print(fomula)

    tmp = 0
    result1=[]
    result1_tmp=[]
    result1_tmp1 = []
    result2=[]
    result3=[]
    

    if (fomula[0] == 'q') and (fomula[1] == 'u') and (fomula[2] == 'i') and (fomula[3] == 't') : #종료메세지
        break
    else :
        #첫연산
        if (fomula[0] != 'A' and 'B' and 'C') : #ex.2A 3B 5C
            sca1=int(fomula[0])
            if (fomula[1] == 'A') :
                result1 = scalarmult(arrAA,rowA,colA,sca1)
            elif (fomula[1] == 'B') :
                result1 = scalarmult(arrBB,rowB,colB,sca1)
            elif (fomula[1] == 'C') :
                result1 = scalarmult(arrCC,rowC,colC,sca1)
            del fomula[0:2]
            print("첫번째 연산 결과",result1)
            print("남은 연산",fomula)
        elif (fomula[0] == 'A' or 'B' or 'C'):
            if (fomula[1] == '+') or (fomula[1] == '-') : #ex. A B C
                if (fomula[0] == 'A') :
                    result1=arrAA
                elif (fomula[0] == 'B') :
                    result1=arrBB
                elif (fomula[0] == 'C') :
                    result1=arrCC
                del fomula[0]
                print("첫번째 연산 결과",result1)
                print("남은 연산",fomula)
            else : #ex. AB BC AC 
                if (fomula[0] == 'A') :
                    if (fomula[1] == 'B') :
                        if (colA == rowB) :
                            for i in range(rowA):
                                for j in range(colB):
                                    for k in range(colA):
                                        tmp += arrAA[i][k] * arrBB[k][j]
                                    result1_tmp.append(tmp)
                                    tmp = 0
                                result1.append(result1_tmp)
                                result1_tmp = []    
                        else :
                            print("할 수 없는 연산입니다.")
                            break
                    elif (fomula[1] == 'C') :
                        if (colA == rowC) :
                            for i in range(rowA):
                                for j in range(colC):
                                    for k in range(colA):
                                        tmp += arrAA[i][k] * arrCC[k][j]
                                    result1_tmp.append(tmp)
                                    tmp = 0
                                result1.append(result1_tmp)
                                result1_tmp = []
                        else :
                            print("할 수 없는 연산입니다.")
                            break
                elif (fomula[0] == 'B') :
                    if (fomula[1] == 'A') :
                        if (colB == rowA) :
                            for i in range(rowB):
                                for j in range(colA):
                                    for k in range(colB):
                                        tmp += arrBB[i][k] * arrAA[k][j]
                                    result1_tmp.append(tmp)
                                    tmp = 0
                                result1.append(result1_tmp)
                                result1_tmp = []
                        else :
                            print("할 수 없는 연산입니다.")
                            break
                    elif (fomula[1] == 'C') :
                        if (colB == rowC) :
                            for i in range(rowB):
                                for j in range(colC):
                                    for k in range(colB):
                                        tmp += arrBB[i][k] * arrCC[k][j]
                                    result1_tmp.append(tmp)
                                    tmp = 0
                                result1.append(result1_tmp)
                                result1_tmp = []
                        else :
                            print("할 수 없는 연산입니다.")
                            break
                elif (fomula[0] == 'C') :
                    if (fomula[1] == 'A') :
                        if (colB == rowA) :
                            for i in range(rowC):
                                for j in range(colA):
                                    for k in range(colC):
                                        tmp += arrCC[i][k] * arrAA[k][j]
                                    result1_tmp.append(tmp)
                                    tmp = 0
                                result1.append(result1_tmp)
                                result1_tmp = []
                        else :
                            print("할 수 없는 연산입니다.")
                            break
                    elif (fomula[1] == 'C') :
                        if (colC == rowA) :
                            for i in range(rowC):
                                for j in range(colA):
                                    for k in range(colC):
                                        tmp += arrCC[i][k] * arrBB[k][j]
                                    result1_tmp.append(tmp)
                                    tmp = 0
                                result1.append(result1_tmp)
                                result1_tmp = [] 
                        else :
                            print("할 수 없는 연산입니다.")
                            break
                del fomula[0:2]
                print("첫번째 연산 결과",result1)
                print("남은 연산",fomula)
