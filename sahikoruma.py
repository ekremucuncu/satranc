import beyazkale
import beyazfil
import beyazvezir
import beyazsah
import siyahkale
import siyahfil
import siyahvezir
import siyahsah

def beyaz_sira(sheet):
    ekrem=[]
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=1, max_col=1):
        for cell in row:
            if cell.value != None:
                if "Siyah" in cell.value and not "Siyah At" in cell.value and not "Siyah Piyon" in cell.value and not "Siyah Sah" in cell.value:
                    konum,eksen,isim=main_tasa_baglanma_siyah(sheet.cell(cell.row, 2), sheet.cell(cell.row, 3), cell.value,sheet)
                    ekrem.append((konum,eksen,isim))
    return ekrem

def siyah_sira(sheet):
    ekrem=[]
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=1, max_col=1):
        for cell in row:
            if cell.value != None:
                if "Beyaz" in cell.value and not "Beyaz At" in cell.value and not "Beyaz Piyon" in cell.value and not "Beyaz Sah" in cell.value:
                    konum,eksen,isim=main_tasa_baglanma_beyaz(sheet.cell(cell.row, 2), sheet.cell(cell.row, 3), cell.value,sheet)
                    ekrem.append((konum,eksen,isim))
    return ekrem


def main_tasa_baglanma_beyaz(x_secilen,y_secilen,secilen_tas,sheet):
    for x in range(1,11):
        if f"Beyaz Kale{x}" in secilen_tas:
            a,b=beyazkale.beyazkale(x_secilen,y_secilen,secilen_tas,sheet)
            break
        if f"Beyaz Fil{x}" in secilen_tas:
            a,b=beyazfil.beyazfil(x_secilen,y_secilen,secilen_tas,sheet)
            break
        if f"Beyaz Vezir{x}" in secilen_tas:
            a,b=beyazvezir.beyazvezir(x_secilen,y_secilen,secilen_tas,sheet)
            break
    konum,eksen,isim=sahikoruma_beyaz_1(b,x_secilen.value,y_secilen.value,sheet)
    return konum,eksen,isim


def main_tasa_baglanma_siyah(x_secilen,y_secilen,secilen_tas,sheet):
    for x in range(1,11):
        if f"Siyah Kale{x}" in secilen_tas:
            a,b=siyahkale.siyahkale(x_secilen,y_secilen,secilen_tas,sheet)
            break
        if f"Siyah Fil{x}" in secilen_tas:
            a,b=siyahfil.siyahfil(x_secilen,y_secilen,secilen_tas,sheet)
            break
        if f"Siyah Vezir{x}" in secilen_tas:
            a,b=siyahvezir.siyahvezir(x_secilen,y_secilen,secilen_tas,sheet)
            break
    konum,eksen,isim=sahikoruma_siyah_1(b,x_secilen.value,y_secilen.value,sheet)
    return konum,eksen,isim


def sahikoruma_siyah_1(kullanilan,x_siyah,y_siyah,sheet):
    ileri=[]
    a=0
    for i in range(len(kullanilan)):
        if kullanilan[i]!=[]:
            ileri.append(kullanilan[i])
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=1, max_col=1):
        for cell in row:
            try:
                if "Beyaz Sah" in cell.value:
                    x_sah = sheet.cell(cell.row, 2).value
                    y_sah = sheet.cell(cell.row, 3).value
                    break
            except TypeError:
                pass
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=1, max_col=1):
        for cell in row:
            try:
                if "Beyaz" in cell.value and "Beyaz Sah" not in cell.value:
                    x=sheet.cell(cell.row,2).value
                    y=sheet.cell(cell.row,3).value
                    konum=(x,y)
                    for i in range(len(ileri)):
                        if konum ==ileri[i][0]:
                            if x==x_siyah==x_sah:
                                a=1
                                return x,0,cell.value
                            if y==y_siyah==y_sah:
                                a=1
                                return y,1,cell.value
                            try:
                                egim_1=(y_siyah-y)/(x_siyah-x)
                                egim_2=(y-y_sah)/(x-x_sah)
                                if egim_1==egim_2:
                                    return egim_1,-2,cell.value
                            except ZeroDivisionError:
                                pass
            except TypeError:
                pass
    if a==0:
        return -1,-1,-1



def sahikoruma_beyaz_1(kullanilan,x_beyaz,y_beyaz,sheet):
    ileri = []
    a=0
    for i in range(len(kullanilan)):
        if kullanilan[i] != []:
            ileri.append(kullanilan[i])
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=1, max_col=1):
        for cell in row:
            try:
                if "Siyah Sah" in cell.value:
                    x_sah = sheet.cell(cell.row, 2).value
                    y_sah = sheet.cell(cell.row, 3).value
                    break
            except TypeError:
                pass
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=1, max_col=1):
        for cell in row:
            try:
                if "Siyah" in cell.value and "Siyah Sah" not in cell.value:
                    x = sheet.cell(cell.row, 2).value
                    y = sheet.cell(cell.row, 3).value
                    konum = (x, y)
                    for i in range(len(ileri)):
                        if konum == ileri[i][0]:
                            if x == x_beyaz == x_sah:
                                a=1
                                return x, 0,cell.value
                            if y == y_beyaz == y_sah:
                                a=1
                                return y, 1,cell.value
                            try:
                                egim_1 = (y_beyaz - y) / (x_beyaz - x)
                                egim_2 = (y - y_sah) / (x - x_sah)
                                if egim_1 == egim_2:
                                    return egim_1, -2, cell.value
                            except ZeroDivisionError:
                                pass
            except TypeError:
                pass
    if a ==0:
        return -1,-1,-1