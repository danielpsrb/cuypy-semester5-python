import main

def start():
    while True:
        print("ini toko apps!")
        play_again_option = input("Apakah ingin kembali ke menu utama? [yes/no]: ")
        
        if play_again_option == "no":
            main.menu()

if __name__ == "__main__":
    start()