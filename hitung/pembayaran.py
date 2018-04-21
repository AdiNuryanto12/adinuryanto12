
def spp():
    bulan = float(input('jumlah bulan yang akan di bayar :'))
    jumlah = 350000 * bulan
    print('spp yang akan di bayar Rp {} \n + biaya server 5000 \n total yang harus dibayar Rp {}'.format(jumlah, jumlah + 5000))

def uas_uts():
    mat = float(input('jumlah matakuliah yang akan di bayar :'))
    jumlah = 25000 * mat
    print('biaya yang akan dibayar Rp {}\n+ biaya server 5000\n total yang harus dibayar Rp {}'.format(jumlah, jumlah + 5000))

def sppdan():
    bulan =float(input('jummlah bulan yang akan dibayar :'))
    mat = int(input('jummlah matakuliah yang akan dibayar :'))
    jubulan = bulan * 350000
    jumat = mat *25000
    ser = 5000
    print('spp yang dibayar Rp {}\nujian yang dibayar Rp {}\n biaya server {} total yang harus dibayar Rp {}'.format(jubulan, jumat, ser, jubulan + jumat +ser))



def pembayaran():
    print('==============================================')
    nama = input('Nama : ')
    nim = input('NIM : ')
    smt = input('semester saat ini : ')
    print('\n\t---pilihan pembayaran---')
    print('\t1. spp\n\t2. uts \n\t3. uas \n\t4. spp dan uts\n\t5. spp dan uas')
    pilih = input('pilih :')
    if(pilih == '1'):
        spp()
    elif(pilih == '2'):
        uas_uts()
    elif(pilih == '3'):
        uas_uts()
    elif(pilih == '4'):
        sppdan()
    elif(pilih == '5'):
        sppdan()
    else:
        print('input salah')
    print('==============================================')
