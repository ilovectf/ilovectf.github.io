import xlrd
import numpy as np

workbook = xlrd.open_workbook('VolgaCTF_excel_crackme.xlsm')
worksheet = workbook.sheet_by_name('Лист1')

for length in range(10, 50):
    A = []
    C = []

    for i in range(length):
        a = []
        for j in range(length):
            a.append(int(worksheet.cell(99 + i, 99 + j).value))
        A.append(a)
        C.append([int(worksheet.cell(99 + i, 99 + length).value)])

    A = np.array(A)
    C = np.array(C)
    B = np.linalg.inv(A).dot(C)
    B = [int(round(e)) for b in B.tolist() for e in b]
    if B[0] == 86:
        print(''.join(chr(e) for e in B))
        break
