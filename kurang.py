import matematika

while True:
    try:
        a = int(input('Masukkan angka pertama: '))
        b = int(input('Masukkan angka kedua: '))
        break
    except ValueError:
        print('Mohon masukkan angka')

print('Hasil =', matematika.kurang(a, b))