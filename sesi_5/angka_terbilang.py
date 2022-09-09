#Challenge membuat program angka terbilang
#Masukkan angka (0-99): 13
#Output : Tiga Belas

def terbilang(bil):
    angka = ['','Satu','Dua','Tiga','Empat','Lima',
             'Enam','Tujuh','Delapan','Sembilan','Sepuluh','Sebelas']
    hasil = ''
    n = int(bil)
    if n >= 0 and n <= 11:
        hasil = angka[bil]
    elif n < 20:
        hasil = terbilang(n % 10) + ' Belas'
    elif n < 100:
        hasil = terbilang(n // 10) + ' Puluh ' + terbilang(n % 10)
    return hasil

while True:
    print('Masukkan angka (0-99): ')
    x = input()
    print(terbilang(int(x)))