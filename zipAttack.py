import zipfile

def open_zip(expectKey):
    with zipfile.ZipFile('sample.zip','r') as zip_file:
        try:
            zip_file.extractall(path='.',pwd=expectKey)
            print('succeeded\n')
            exit()
        except:
            print('failed\n')

def main():
    numbers = list(range(10))
    print(f'I will try with this list: {numbers}')
    my_pass = []

    for i in numbers:
        for j in numbers:
            for k in numbers:
                for l in numbers:
                    key = str(i) + str(j) + str(k) + str(l)
                    print(f'trying with {key}: ')
                    open_zip(key)


        
        


if __name__ == '__main__':
    main()