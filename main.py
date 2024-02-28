from libs import welcome_message, exit_program
from games import cuypy
from tools import toko

def menu():
    users_option = int(input(f'Silahkan pilih menu program:\n1. Games CuyPy\n2. Toko Mini\n3.Keluar Semua Program\n\nSilahkan pilih: '))
    
    if users_option == 1:
        cuypy.start()
    elif users_option == 2:
        toko.start()
    elif users_option == 3:
        exit_program()
    else: 
        print('Pilihan yang anda masukkan tidak valid, hanya boleh pilih yang tersedia di menu')

def main():
    welcome_message()
    menu()

if __name__ == "__main__":
    main()

