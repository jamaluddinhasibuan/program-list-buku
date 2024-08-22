#membuat program list buku
list_buku = []
while True:
    print('Masukkan Data Buku')
    judul = input('Masukkan judul buku\t: ')
    penulis = input('Masukkan nama penulis\t: ')
    
    baru = [judul,penulis]
    list_buku.append(baru)
    print(list_buku)
    
    print('No.\t | judul\t\t\t | Penulis') #arti t = tab atau membuat jarak

    for index,buku in enumerate (list_buku):
        print(f'{index+1}\t | {buku[0]}\t\t | {buku[1]}')
        
    Lanjut = input('Apakah Anda ingin melanjutkan( y / n) : ')
    if Lanjut == 'n':
        break
    
print('PROGRAM SELESAI')    
            