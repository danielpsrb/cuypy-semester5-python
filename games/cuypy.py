import random
import main

def start():
    while True:
        bentuk_goa = "|__|"
        goa_kosong = [bentuk_goa] * 4 # INI HARUS TETAP KOSONG

        cuypy_position = random.randint(1, 4)

        goa = goa_kosong.copy() # INI ADALAH TEMPAT BARU UNTUK SI CUYP
        goa[cuypy_position - 1] = "|0_0|" 

        goa_kosong = ' '.join(goa_kosong)
        goa = ' '.join(goa)
        
        print(f'Coba Perhatikan gambar dibawah ini \n\n {goa_kosong}\n')  

        user_choices = 0

        while user_choices < 1 or user_choices > 4:
            user_choices = int(input("Menurut Kamu, di gambar nomor berapa CuyPy berada? [1 / 2 / 3/ 4]: " ))
            if user_choices < 1 or user_choices > 4:
                print("Hey Pilihan Anda tidak valid, hanya tersedia Pilihan 1, 2, 3 dan 4 \n")


        if user_choices == cuypy_position:
            print(f"{goa} \n Selamat Kamu Menang 🏆️ dan berhasil menebak CuyPy 💯 Posisi CuyPy berada di {cuypy_position}")
        else:
            print(f"{goa} \n MAAF KAMU KALAH 😔 Posisi CuyPy yang benar berada di gambar nomor {cuypy_position}, sedangkan Pilihan Kamu adalah {user_choices}")
            
        play_again = input("\n \n Apakah anda ingin melanjutkan games ini lagi ? [Yes/No]: ")
        if play_again == "No":
            main.menu()
        
if __name__ == "__main__":
    start();