#https://github.com/sanzking/
#ini module
import time
import os
os.system('clear')
#ini warna
grey = '\x1b[90m'
red = '\x1b[91m'
green = '\x1b[92m'
yellow = '\x1b[93m'
blue = '\x1b[94m'
purple = '\x1b[95m'
cyan = '\x1b[96m'
white = '\x1b[37m'
flag = '\x1b[47;30m'
off = '\x1b[m'
flag = '\x1b[47;30m'
logo = f"{flag} NimGenerate | sanzking {off}"
fwrite = open('hasilulang.txt', 'w')

#main menu
print(logo + '\n')
uid = int(input(f"{green}> {off}masukan patokan : "))
password = input(f"{green}> {off}masukan passwordnya : ")
max = int(input(f"{green}> {off}akhiran : "))
sav = input(f"{green}> {off}File save : ")
os.system('clear')
for i in range(max):
    cuk = i + uid
    print(f"{green}[{off}+{green}]{purple}"+str(cuk)+':'+f"{blue}"+password+f"{off}")
    time.sleep(0.001)
    with open(f'{sav}.txt', 'a') as _f:
    	_f.write(str(cuk)+':'+password+'\n')
#akhiran
print(f"\n{white}> {green}generate selesai, hasilnya tersimpan di {off}\n{white}> {cyan}{sav}.txt{off}")
#jangan lupa join vpnkacang:)