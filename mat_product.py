import numpy as np

def inputLinier(m,n):
    import numpy as np
    sizeOflinier = n * m
    print('行列の要素を入力してください')
    material = []
    for i in range(sizeOflinier):
        tmp = input()
        tmp = float(tmp)
        material.append(tmp)
    linier = np.array(material).reshape(m,n)
    print('入力された行列は下記\n')
    print(linier)
    return linier
    

def main():
    print('行列サイズを入力してください\n')
    print('何行ですか？')
    n = input()
    n = int(n)
    print('何列ですか？')
    m = input()
    m = int(m)
    lini_1 = inputLinier(n,m)
    print('行列サイズを入力してください\n')
    print('何行ですか？')
    n = input()
    n = int(n)
    print('何列ですか？')
    m = input()
    m = int(m)
    lini_2 = inputLinier(n,m)

    dot = np.dot(lini_1,lini_2)
    print(f'行列積は\n{dot}')

if __name__ == '__main__':
    main()