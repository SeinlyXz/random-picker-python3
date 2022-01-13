import random
from time import sleep as s
from os import system as t


#########################################################
#                                                       #
#        THIS PROGRAM WAS CREATED IN WINDOWS            #
# IF YOU USE LINUX, CHANGE THE t('cls') to t('clear')   #
#                                                       #
#########################################################

t('cls')

def main():
    jml = int(input("[*] Masukkan jumlah siswa: "))
    klm = int(input("[*] Jumlah siswa per-kelompok: "))
    hitung(jml, klm) # Untuk next ke fungsi hitung() dengan menginputkan variabel jml dan kml
        
def hitung(jml, klm):
    # Untuk mengecek apakah jumlah siswa lebih sedikit dari orang yang ada di dalam 1 kelompoknya
    if jml < klm: 
        print("\n[*] ERROR: TIDAK MUNGKIN DIBAGI KELOMPOK")
        print("[*] Mengulang Program dalam")
        for i in range(3,-1,-1):
            print("[*] {}".format(i))
            s(1)
            if i == 1:
                t('cls')
                main1()
    else:
        g = [] # Untuk membuat list kosong yang akan terinput saat variabel "jml" sudah diisi
        div = jml/klm
        sisa = jml%klm
        # Untuk memasukkan sejumlah jml angka ke dalam list g
        for i in range(1, jml+1):
            g.append(i)

        kelompok = 1
        print("[*] Jumlah Kelompok: {}".format(div))
        print("[*] Sisa: {}".format(sisa))
        # Untuk menampilkan kelompok beserta anggotanya berdasarkan urut absen yang "telah diacak"
        for i in range(len(g)):
            print("-------------Kelompok {}-------------".format(kelompok))
            kelompok += 1
            s(1)
            # Untuk menampilkan anggota kelompok berdasarkan jumlah orang per kelompoknya
            for j in range(1,klm+1):
                random.shuffle(g)
                print("[*] Nomor Absen-{}".format(g[0]))
                g.remove(g[0])
                if len(g) < 1:
                    print("-------------Program Selesai-------------")
                    exit()

def main1():
    # Fungsi ini berguna untuk mengulang fungsi yang sebelumnya harus diulang
    menu()
    main()

def menu():
    print("-------------------------------------------")
    print("|                                         |")
    print("|  LET'S SHUFFLE AND DETERMINE THE GROUP  |")
    print("|                                         |")
    print("|          BY: XII SCIENCE CLASS A        |")
    print("|                                         |")
    print("-------------------------------------------")

for i in range(3, -1, -1):
    menu()
    print("Tunggu {}-detik lagi".format(i))
    s(1)
    t('cls')

# Memulai program
menu()
main()
