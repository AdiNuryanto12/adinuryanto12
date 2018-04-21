def tanya():
	pilih = input('kembali ke menu kalkulator [y/n] :')
	if pilih == 'y':
		calculator()
		
def calculator():
    print('================================================================')
    print('\tprogram kalkulator sederhana')
    print('================================================================')
    print('\t---pilih---\n\t1. penjumlahan\n\t2. pengurangan\n\t3. pembagian\n\t4. perkalian')
    pilih = input('\tmasukan pilihan :')
    if (pilih == '1'):
        jumlah()
    elif(pilih == '2'):
        kurang()
    elif(pilih == '3'):
        bagi()
    elif(pilih == '4'):
        kali()
    else:
        exit()

def jumlah():
    print('\tpenjumlahan')
    a = int(input('masukan nilai a :'))
    b = int(input('masukan nilai b :'))
    print('nilai a :{} ditambah nilai b :{} hasilnya = {}'.format(a, b, a + b))
    tanya()

def kurang():
    print('\tpengurangan')
    a = int(input('masukan nilai a :'))
    b = int(input('masukan nilai b :'))
    print('nilai a :{} dikurang nilai b :{} hasilnya = {}'.format(a, b, a - b))
    tanya()


def bagi():
    print('\tpembagian')
    a = int(input('masukan nilai a :'))
    b = int(input('masukan nilai b :'))
    print('nilai a :{} dibagi nilai b :{} hasilnya = {}'.format(a, b, a / b))
    tanya()


def kali():
    print('\tperkalian')
    a = int(input('masukan nilai a :'))
    b = int(input('masukan nilai b :'))
    print('nilai a :{} dikali nilai b :{} hasilnya = {}'.format(a, b, a * b))
    tanya()
