from . import operasi

def delete_console():
    read_console()
    while(True):
        print("Silahkan masukkan nomor buku yang akan didelete : ")
        no_buku = int(input("Nomor Buku : "))
        data_buku = operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(",")
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4] [:-1]

        

    
        # data yang akan didelete
            print("\n"+"="*100)
            print("Silahkan pilih data yang akan didelete")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")
            isDone = input("Yakin akan dihapus? (y/n) : ")
            if isDone == "y" or isDone == "Y":
                operasi.delete(no_buku)
                break
        else:
            print("Data buku tidak terdeteksi, silahkan masukkan lagi")

    print("Data berhasil dihapus")
    
    


def update_console():
    read_console()
    while(True):
        print("Silahkan masukkan nomor buku yang akan diupdate : ")
        no_buku = int(input("Nomor Buku : "))
        data_buku = operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("Data buku tidak terdeteksi, silahkan masukkan lagi")

    data_break = data_buku.split(",")
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4] [:-1]

    while(True):
        # data yang akan diupdate
        print("\n"+"="*100)
        print("Silahkan pilih data yang akan diubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        # memilih data yang akan diupdate
        user_option = input("Pilh data (1,2,3) : ")
        print("\n"+"="*100)
        match user_option:
            case "1": judul = input("judul\t:")
            case "2": penulis = input("penulis\t:")
            case "3":
                while True:
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun harus angka, silahkan masukkan tahun (yyyy)")

                    except :
                        print("Tahun harus angka, Silahkan masukan tahun (yyyy)")
            case _: print("Index tidak ditemukan")

        print("Data Baru Anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        isDone = input("Apakah data sudah seusai (y/n) : ")
        if isDone == "y" or isDone == "Y":
            break
    
    operasi.update(no_buku,pk,data_add,penulis,judul,tahun)
def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data Buku\n")
    judul = input("judul\t: ")
    penulis = input("Penulis\t: ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus angka, silahkan masukkan tahun (yyyy)")

        except :
            print("Tahun harus angka, Silahkan masukan tahun (yyyy)")
        
    operasi.create(tahun, judul, penulis)
    print("\nBerikut adalah data baru anda")
    read_console()

def read_console():
    data_file = operasi.read()
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

# header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)

# data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        data_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}", end="")

# footer
    print("="*100+"\n")