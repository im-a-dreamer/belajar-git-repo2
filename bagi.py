import matematika

while True:
    try:
        a = int(input('Masukkan angka pertama: '))
        b = int(input('Masukkan angka kedua:'))
        break
    except ValueError:
        print('Mohon masukkan angka')

try:
    print('Hasil =', matematika.bagi(a, b))
except ZeroDivisionError:
    print('ada pembagian dengan angka 0')
