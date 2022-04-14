import os


class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node
    
    #Mengambil data dari node
    def get_data(self):
        return self.data

    #Mengambil node berikutnya
    def get_next(self):
        return self.next_data

    #Menentukan node berikutnya
    def get_next(self, new_text):
        self.next_node = new_text

#Membuat class baru untuk menampung linkedlist
class linklist(object):
    def __init__(self, head = None):
        self.next_node = head 

    #Menambah node baru
    def insert(self,data):
        #inisialisasi dari node yang baru
        new_node = Node(data)
        #Menunjuk ke Node berikutnya
        new_node.get_next(self.head)

    #Menghitung panjang list
    def size(self):
        #membuat pointer baru
        current = self.head
        count = 0
        while current :
            count +=1
            current = current.get_next(1)
        return count

    #Mencari sebuah data pada list
    def search(self,data):
        #Membuat pointer baru
        current = self.head
        found = False
        #Perulangan untuk mencari node
        while current and found is False :
            if current.get_data() == data:
                found=True
            else:
                current = current.get_next()
            return found

    #Menghapus dari node
    def delete(self,data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
            if current is None:
                raise ValueError("Data tidak ada")
            if previous is None:
                self.head = current.get_next()
            else:
                previous.get_next(current.get_next())
    
    #Menampilkan isi dari list
    def showData(self):
        os.system("cls")
        print("Tampilkan list data : ")
        print("Node -> Next Node")
        current_node = self.head
        while current_node is not None:
            print(current_node.data),
            print("         ->"),
            if current_node.next_node == self.data:
                current_node.next_node ==  self.data
            
            else: 
               current_node.next_node == self.next_node

            current_node=self.next_node
            

    #main menu aplikasi
    def mainmenu(self):
        pilih = "y"
        while(pilih == "y"):
            os.system("cls")
            print("==================================")
            print("  Menu dari aplikasi linked list  ")
            print("==================================")
            print("1. Insert data")
            print("2. Delete data")
            print("3. Cari data")
            print("4. Panjang data")
            print("5. Tampilkan data")
            print("==================================")
            print=str(input(("Silahkan masukan pilihan anda : ")))
            if(pilihan=="1"):
                os.system("cls")
                obj = str(input("Masukan data yang ingin anda tambah : "))
                self.insert(obj)
            elif(pilihan=="2"):
                os.system("cls")
                obj = str(input("Masukan data yang ingin anda hapus : "))
                self.delete(obj)
                x = input("")
            elif(pilihan=="3"):
                os.system("cls")
                obj = str(input("masukan data yang ingin anda cari : "))
                status = self.search(obj)
                if status == True:
                    print("Data ditemukan")
                else:
                    print("Data tidak ditemukan")
                x = input("")
            elif(pilihan=="4"):
                os.system("cls")
                print("Panjang data adalah "+str(self.size()))
            elif(pilihan=="5"):
                os.system("cls1 ")
                self.showData()
                x = input("")
            else:
                pilihan = "n"

if __name__ == "__main__":
    l = linklist()
    l.mainmenu()

