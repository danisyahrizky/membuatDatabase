import os
import CRUD as CRUD

if __name__ == "__main__":
    sistemOperasi = os.name 

    match sistemOperasi:
        case "posix": os.system("clear")
        case "nt" : os.system("cls")

    print("Selamat Datang di Program")
    print("Database Perpustakaan")
    print("===========================")

    # check database ada atau tidak
    CRUD.init_console()

    while(True):
        match sistemOperasi:
            case "posix": os.system("clear")
            case "nt" : os.system("cls")

        print("Selamat Datang di Program")
        print("Database Perpustakaan")
        print("===========================")

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        userOption = input("Masukkan Opsi : ")

        match userOption:
            case "1" : CRUD.read_console()
            case "2" : CRUD.create_console()
            case "3" : CRUD.update_console()
            case "4" : CRUD.delete_console()


        isDone = input("Apakah Selesai (y/n) : ")
        if isDone == "y" or isDone == "Y":
            break

    print("Terimakasih")