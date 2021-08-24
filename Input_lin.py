

# n次の行列を入力から受け取るアルゴリズム
def main():
    import numpy as np
    print('何行ですか？')
    p = int(input())
    print('何列ですか？')
    q = int(input())
    List_lin = []

    for i in range(p):
        for j in range(q):
            print(f'{i+1}行{j+1}列目の要素を入力してください\n')
            tmp = float(input())
            List_lin.append(tmp)

    ans = np.array(List_lin).reshape(p,q)
    print(f'入力された行列は\n{ans}')
    return ans


if __name__ == '__main__':
    main()