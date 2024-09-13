# I Run this sc with Python 3.11.9
# Created / up [ 13-09-2024 ] 14.00 🕑
# Github : github.com/x7cyber
# @cyberm._


'''
This Tools is for educational purposes only. SD/SMP/SMA/S1/S2/S3+++

Dan.. Tools ini hanya bisa melakukan serangan ke file .zip
melakukan serangan ke ekstensi selain itu, ya gak bisa cik 😹
install modul secara manual 'pip install zipfile'
dah itu aja!
'''

import_rempah_rempah='masako'
import_ikn=''
import_satelit=''
import_nasa=''

import_aset_negara='☠️'
import_dpr=''
import_kominfo=''
import_password='Admin#1234'
singkat_padat_kominfo_bjir='💀'

import_bumbu_dapur='laperbjir'
import_cabai=''
import_tomat=''
import_lengkuas=''
import_laos=''
import_bawang=''
import_lada=''
import_kunyit=''
import_jahe=''
import_serai=''
import_jintan=''
import_ketumbar=''
import_daun_jeruk=''
import_daun_salam=''
import_asam_jawa=''
import_gula_merah=''
import_daun_bawang=''
import_kluwak=''
import_bon_cabe=''


try:
    import zipfile
except ImportError:
    print('Bentar, lagi install nih...')
    import pip
    pip.main(['install', 'zipfile'])
    import zipfile

import time, os, sys
from zipfile import ZipFile
from datetime import datetime

manusia_itu_tempatnya_salah_dan_dosa=print
tapi_sebaik_baik_manusia_adalah_yang_mau_bertaubat=print

def x7cyber_cyberm_zracking_wuihh_afaantuh():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

x7cyber_cyberm_zracking_wuihh_afaantuh()
manusia_itu_tempatnya_salah_dan_dosa("\n[\033[1m\033[32m•\033[0m] Author : \033[30;42mx7cyber\033[0m \n[\033[1m\033[32m•\033[0m] Tools  : zip-cracking [0.12.0]\n")

def pecah(waduh, nabrak):
    global count, password_ditemukan, found_password
    try:
        with ZipFile(nabrak, 'r') as zipObj:
            zipObj.extractall(pwd=bytes(waduh, 'utf-8'))
            istirahatkan_dirimu_kawan = datetime.now().strftime("%H:%M:%S")
            manusia_itu_tempatnya_salah_dan_dosa(f'\n\a\033[1m[\033[31m{istirahatkan_dirimu_kawan}\033[0m] cracking password › \033[32m{waduh} \033[0m\n')
            password_ditemukan = True
            found_password = waduh
            return True
    except Exception:
        count += 1
        if count % 100000 == 0:
            manusia_itu_tempatnya_salah_dan_dosa(f'\n\n[\033[1m\033[33m⚠\033[0m] Upaya tercapai › \033[32m{str(count)}\033[0m')
        istirahatkan_dirimu_kawan = datetime.now().strftime("%H:%M:%S")
        manusia_itu_tempatnya_salah_dan_dosa(f'\n\033[1m[\033[32m{istirahatkan_dirimu_kawan}\033[0m] cracking password › {waduh}\033[0m', end="", flush=True)
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    count = 0
    password_ditemukan = False
    found_password = None

    mulai_input_file_nih_ceritanya = input("Input file .zip\n\033[1m\033[32m>\033[0m ")
    if mulai_input_file_nih_ceritanya == '':
        exit()

    nah_kalau_ini_masukin_pw_cik = input("\nInput wordlist password\n\033[1m\033[32m>\033[0m ")
    if nah_kalau_ini_masukin_pw_cik == '':
        exit()

    istirahatkan_dirimu_kawan = datetime.now().strftime("%H:%M:%S")
    manusia_itu_tempatnya_salah_dan_dosa(f'\n[\033[1m\033[32m*\033[0m] starting at \033[1m[\033[32m{istirahatkan_dirimu_kawan}\033[0m]')
    manusia_itu_tempatnya_salah_dan_dosa(f"[\033[1m\033[32m*\033[0m] cracking {mulai_input_file_nih_ceritanya} dengan daftar password {nah_kalau_ini_masukin_pw_cik}")

    if os.path.exists(nah_kalau_ini_masukin_pw_cik):
        if mulai_input_file_nih_ceritanya.split('.')[-1] == 'zip':
            print()
            li = open(nah_kalau_ini_masukin_pw_cik, 'r').readlines()
            total_attempts = len(li)
            start = time.perf_counter()

            for x in li:
                if pecah(x.strip(), mulai_input_file_nih_ceritanya):
                    break

            end = time.perf_counter()
            elapsed_time = end - start
            elapsed_seconds = int(elapsed_time)
            elapsed_milliseconds = int((elapsed_time - elapsed_seconds) * 1000)

            if not password_ditemukan:
                istirahatkan_dirimu_kawan = datetime.now().strftime("%H:%M:%S")
                manusia_itu_tempatnya_salah_dan_dosa(f"\n\n[\033[1m\033[33m⚠\033[0m] Opss 😑")
                manusia_itu_tempatnya_salah_dan_dosa(f"[\033[1m\033[33m⚠\033[0m] Password tidak ditemukan dalam wordlist!")
                tapi_sebaik_baik_manusia_adalah_yang_mau_bertaubat(f"[\033[1m\033[33m⚠\033[0m] Jumlah percobaan: {count}\n")
            else:
                istirahatkan_dirimu_kawan = datetime.now().strftime("%H:%M:%S")
                manusia_itu_tempatnya_salah_dan_dosa(f"[\033[1m\033[31m☠\033[0m] Password ditemukan: \033[0m\033[1m\033[1;43m{found_password}\033[0m")
                manusia_itu_tempatnya_salah_dan_dosa(f"[\033[1m\033[31m☠\033[0m] Jumlah percobaan: {count}")
                manusia_itu_tempatnya_salah_dan_dosa(f"[\033[1m\033[31m☠\033[0m] Dalam waktu: {elapsed_seconds} detik {elapsed_milliseconds} ms\n")

        else:
            tapi_sebaik_baik_manusia_adalah_yang_mau_bertaubat('[\033[1m\033[31m⚠\033[0m] File tidak jelas!')
    else:
        manusia_itu_tempatnya_salah_dan_dosa('[\033[1m\033[31m⚠\033[0m] Wordlist password tidak ditemukan!')
