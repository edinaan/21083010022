#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def estimasi():
    from datetime import date, time, datetime, timedelta
    
    #KOTA
    kota_awal = []
    kota_tujuan = []
    kota_awal = input("Darimana kota asal keberangkatan anda?                         ")
    kota_tujuan = input("Darimana kota tujuan anda?                                     ")
    
    #DATE & TIME
    date_components = input("Tanggal berapa keberangkatan anda? (YYYY-MM-DD)                ").split('-')
    year, month, day = [int(item) for item in date_components]
    tanggal = date(year, month, day)

    time_components = input("Jam berapa keberangkatan anda? (HH:MM)                         ").split(':')
    hour, minute = [int(item) for item in time_components]
    jam = time(hour, minute)

    berangkat = datetime.combine(tanggal, jam)
    
    #HITUNG
    jarak = int(input("Berapa jarak yang akan anda tempuh?                            "))
    kec_min = int(input("Berapa kecapatan minimum kendaraan yang anda naiki?            "))
    kec_max = int(input("Berapa kecapatan maksimum kendaraan yang anda naiki?           "))
    kecepatan = (kec_min + kec_max) / 2
    waktu_tempuh = (jarak / kecepatan) * 60
    a = waktu_tempuh
    print('\033[94m' + ("="*90))
    print((" "*40),'\033[94m'+"HASIL PERHITUNGAN")
    print((" "*36),'\033[94m'+"ESTIMASI WAKTU PERJALANAN")
    print('\033[94m' + ("="*90))
    print("Kecepatan rata-rata kendaraan yang anda naiki adalah "+str(kecepatan)+" km/jam.")
    print("Estimasi waktu perjalanan yang anda tempuh dari " +str(kota_awal)+ "-" +str(kota_tujuan)+" adalah " +str(waktu_tempuh)+ " menit.")
    sampai = berangkat + timedelta(minutes=a)
    print("Anda akan sampai di " +str(kota_tujuan)+ " pada", sampai)
    
    
#HEADER
import time

print('\033[91m' + ("="*90))
print((" "*35),'\033[91m' + "SELAMAT DATANG DI PROGRAM")
print((" "*30),'\033[91m' + "PENGHITUNG ESTIMASI WAKTU PERJALANAN")
print('\033[91m' + ("_"*90))
print((" "*35),'\033[91m' + "By : Edina Alana Nabila")
print('\033[91m' + ("="*90))

time.sleep(1)

nama = input("Masukkan nama Anda:                                            ")
print('\033[95m' + ("="*90))
print((" "*45),'\033[95m' + "HELLO")
print((" "*45),'\033[95m' + str(nama) + "!")
print('\033[95m' + ("="*90))


while True:
    start = str(input("Apakah anda ingin memulai program ini? (Ya/Tidak):             "))
    if start == 'Ya':
       print('\033[92m' + ("="*90))
       print((" "*45),'\033[92m' + "SIAP?")
       time.sleep(1)
       print((" "*45),'\033[92m' + "MULAI!")
       print('\033[92m' + ("="*90))
       estimasi()
       time.sleep(5)
       repeat = str(input("Apakah anda ingin mencoba kembali program ini? (Ya/Tidak):     "))
       if repeat == "Ya":
          continue
       else:
          print(" ")
          print((" "*35), '\033[1m' + "SILAHKAN KEMBALI LAIN KALI!" + '\033[0m')
          print((" "*42), '\033[1m' + "TERIMA KASIH!" + '\033[0m')
    else:
       print(" ")
       print((" "*35),'\033[1m' + "SAYA TUNGGU PERCOBAAN ANDA!" + '\033[0m')
    break
