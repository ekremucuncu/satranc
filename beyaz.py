import beyazpiyon
import beyazkale
import beyazfil
import beyazvezir
import beyazsah
import beyazat


def tasa_baglanma(x_secilen,y_secilen,secilen_tas,sheet):
    for x in range(1,11):
        if f"Beyaz Piyon{x}" in secilen_tas:
            a,b=beyazpiyon.beyazpiyon(x_secilen,y_secilen,secilen_tas,sheet)
            break
        if f"Beyaz Kale{x}" in secilen_tas:
            a,b=beyazkale.beyazkale(x_secilen,y_secilen,secilen_tas,sheet)
            break
        if f"Beyaz Fil{x}" in secilen_tas:
            a,b=beyazfil.beyazfil(x_secilen,y_secilen,secilen_tas,sheet)
            break
        if f"Beyaz Vezir{x}" in secilen_tas:
            a,b=beyazvezir.beyazvezir(x_secilen,y_secilen,secilen_tas,sheet)
            break
        if f"Beyaz Sah" in secilen_tas:
            a,b=beyazsah.beyazsah(x_secilen,y_secilen,secilen_tas,sheet)
            break
        if f"Beyaz At{x}" in secilen_tas:
            a,b=beyazat.beyazat(x_secilen,y_secilen,secilen_tas,sheet)
            break
    return(a)


def tas_hareket_ettirme(a,x_bulunan,y_bulunan,sheet,secilen_tas,liste,ekrem):
    for i in range(len(liste)):
        if secilen_tas == liste[i][0]:
            baybay = (liste[i][1], liste[i][2])
            try:
                a.remove(baybay)
            except ValueError:
                pass
    for i in range(len(ekrem)):
        konum=ekrem[i][0]
        eksen=ekrem[i][1]
        isim=ekrem[i][2]
        if (eksen == 0 or eksen == 1) and secilen_tas == isim:
            b = []
            for i in range(len(a)):
                if a[i][eksen] == konum:
                    b.append(a[i])
            c=b
            break
        elif eksen == -2 and secilen_tas == isim:
            b = []
            for i in range(len(a)):
                try:
                    egim = (a[i][1] - y_bulunan) / (a[i][0] - x_bulunan)
                    if egim == konum:
                        b.append(a[i])
                except ZeroDivisionError:
                    pass
            c=b
            break
        else:
            c=a
    if ekrem==[]:
        c=a
    sayac=0
    for i in c:
        x=i[0]
        y=i[1]
        sayac=sayac+1
        print(f"{i} noktasina gitmek icin {sayac}'e basiniz.")
    print("Baska bir tas secmek icin 0'a basiniz.")
    while True:
        try:
            secim=int(input())
            if secim == 0:
               tas_secme(sheet,ekrem,liste)
               break
            else:
                gidilecek_yer = c[secim - 1]
                tas_yok_etme(gidilecek_yer[0],gidilecek_yer[1],sheet)
                for row in sheet.iter_rows(min_row=2,max_row=33,min_col=2,max_col=2):
                    for cell in row:
                        if cell.value==x_bulunan:
                            y=sheet.cell(cell.row,3)
                            if y.value==y_bulunan:
                                isim=sheet.cell(cell.row,1).value
                                sheet.cell(row=cell.row,column=2,value=gidilecek_yer[0])
                                sheet.cell(row=cell.row,column=3,value=gidilecek_yer[1])
                                print(f"{isim}'in yeni konumu ({gidilecek_yer[0]},{gidilecek_yer[1]})")
                                if "Piyon" in isim:
                                    if gidilecek_yer[1]==8:
                                        beyazpiyon.beyazpiyon_degistirme(gidilecek_yer[0],gidilecek_yer[1],isim,sheet)
        except ValueError:
            print("Lutfen bir sayi giriniz!")
        break


def tas_yok_etme(x_olen,y_olen,sheet):
        for row in sheet.iter_rows(min_row=2,max_row=33,min_col=2,max_col=2):
            for cell in row:
                if cell.value==x_olen:
                    y=sheet.cell(cell.row,3)
                    isim=sheet.cell(cell.row,1).value
                    if y.value==y_olen:
                        print(f"Yenilen tas {isim}.")
                        sheet.delete_rows(cell.row)


def tas_secme(sheet,ekrem,liste):
    sayac = 0
    secilen_tas = input("Lutfen Oynamak istediginiz tasi seciniz!\n")
    for row in sheet.iter_rows(min_row=2,min_col=1,max_col=3,max_row=33):
        for cell in row:
            sayac=sayac+1
            if secilen_tas==cell.value:
                x=sheet.cell(cell.row,cell.column+1)
                y=sheet.cell(cell.row,cell.column+2)
                print(f'Oynatmak istediginiz {secilen_tas} ({x.value},{y.value}) konumunda bulunuyor.')
                sayac=sayac-1
                a=tasa_baglanma(x,y,secilen_tas,sheet)
                tas_hareket_ettirme(a,x.value,y.value,sheet,secilen_tas,liste,ekrem)
            elif sayac==96:
                print("Boyle bir tas bulunamadi")
                tas_secme(sheet,ekrem,liste)