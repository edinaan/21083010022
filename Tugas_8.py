from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

#Input angka batasan yang diinginkan
x = int(input("Masukkan angka batasan: "))

#Inisiasi fungsi yang akan digunakan
def cetak(i):
    print("Cetak angka", i+1,"- punya ID proses", getpid())
    sleep(1)

#Pemrosesan sekuensial
print("Sekuensial")
sekuensial_awal = time()

for i in range(x):
    cetak(i)

sekuensial_akhir = time()

#Multiprocessing dengan kelas Process
print("multiprocessing.Process")
kumpulan_proses = []

process_awal = time()

for i in range(x):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()

for i in kumpulan_proses:
    p.join()


process_akhir = time()

#Multiprocessing dengan kelas Pool
print("multiprocessing.Pool")
pool_awal = time()

pool = Pool()
pool.map(cetak, range(0,x))
pool.close()

pool_akhir = time()

#Bandingkan waktu eksekusi
print("Waktu eksekusi sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.Process :", process_akhir - process_awal, "detik")
print("Waktu eksekusi multiprocessing.Pool :", pool_akhir - pool_awal, "detik")

