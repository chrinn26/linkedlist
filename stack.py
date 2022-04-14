stack = []
   
yes = 'ya'

while yes == 'ya':
    print('===========================================================')
    nama = str(input("Input nama yang ingin anda inginkan: "))
    stack.append(nama)
    print('===========================================================')
    yes = input("tambah data nama yang mau ditambahkan? [ya/tidak] : ")

while stack != []:
    print('===========================================================')
    print(stack.pop())
print('===========================================================')
print("Program Selesai!")      

