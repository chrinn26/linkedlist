print("Selamat Datang di Rinn ATM")
print("Plih Option : ")
print("1. Check Saldo")
print("2. Tarik Saldo")
print("3. Tabung Saldo")
option=int(input("Silahkan Pilih Option : "))
if option==1:
    print("Saldo Anda Berjumlah Rp.100.000")
elif option==2:
    print("Saldo Anda Berjumlah Rp.100.000, Mau ditarik berapa?")
    print("1. Rp. 50.000")
    print("2. Rp. 40.000")
    uang_kamu=100000
    option2=int(input("Option : "))
    if option2==1:
        hasil=uang_kamu-50000
        print("Saldo Anda Sekarang Berjumlah : ",hasil)
    elif option2==2:
        hasil2=uang_kamu-40000
        print("Saldo Anda Sekarang Berjumlah : ",hasil2)
    else:
        print("Keyword Anda Salah!")
elif option==3:
    uang_kamu=100000
    print("Saldo Berjumlah Rp. 100.000, Mau Nabung Berapa?")
    option3=int(input("Masukkan Jumlah Saldo Yang Ingin Ditabung"))
    hasil3=uang_kamu+option3
    print("Jumlah Saldo Anda Sekarang Adalah ",hasil3)
else:
    print("Keyword Anda Salah, Silahkan Coba Lagi") 
