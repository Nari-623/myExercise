import numpy as np

print('逆行列を求めたい行列のサイズを入力してください。')
print('行列は何行ですか？')
p = int(input())
print('行列は何列ですか？')
q = int(input())
List_lin = []
for i in range(p):
    for j in range(q):
        print(f'{i+1}行{j+1}列目の要素を入力してください\n')
        tmp = float(input())
        List_lin.append(tmp)

lini_1 = np.reshape(List_lin,(p,-1))
print(f'入力された行列は\n{lini_1}')

Det = np.linalg.det(lini_1)
lini_inv = np.linalg.inv(lini_1)

print(f'行列式は{Det}\n逆行列は\n{lini_inv}')