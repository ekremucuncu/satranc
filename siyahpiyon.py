def siyahpiyon(x_secilen, y_secilen, secilen_tas,sheet):
    h1=siyahpiyon_sol_capraz(x_secilen, y_secilen, secilen_tas,sheet)
    h2=siyahpiyon_on(x_secilen, y_secilen, secilen_tas,sheet)
    h3=siyahpiyon_sag_capraz(x_secilen, y_secilen, secilen_tas,sheet)
    h4=siyahpiyon_ilk_sefer(x_secilen,y_secilen,secilen_tas,sheet)
    gecici=[h1,h2,h3,h4]
    geri=[]
    for x in gecici:
        if x !=None:
            geri.append(x)
    return geri,geri


def siyahpiyon_on(x_secilen, y_secilen, secilen_tas,sheet):
    sayac_1 = 0
    sayac_2 = 0
    for row in sheet.iter_rows(min_row=2, min_col=2, max_row=33, max_col=2):
        for cell in row:
            if cell.value == x_secilen.value:
                sayac_1 = sayac_1 + 1
                y = sheet.cell(cell.row, 3)
                if y.value != y_secilen.value - 1:
                    sayac_2 = sayac_2 + 1
    if sayac_2 == sayac_1:
        return(x_secilen.value,y_secilen.value-1)


def siyahpiyon_ilk_sefer(x_secilen, y_secilen, secilen_tas,sheet):
    sayac_1 = 0
    sayac_2 = 0
    sayac_3=0
    sayac_4=0
    for row in sheet.iter_rows(min_row=2, min_col=2, max_row=33, max_col=2):
        for cell in row:
            if cell.value == x_secilen.value:
                sayac_1 = sayac_1 + 1
                y = sheet.cell(cell.row, 3)
                if y.value != y_secilen.value - 1:
                    sayac_2 = sayac_2 + 1
    if sayac_2 == sayac_1:
        for row in sheet.iter_rows(min_row=2,max_row=33,min_col=2,max_col=2):
            for cell in row:
                if cell.value==x_secilen.value:
                    sayac_3=sayac_3+1
                    y=sheet.cell(cell.row,3)
                    if y.value!=y_secilen.value-2:
                        sayac_4=sayac_4+1
        if sayac_3==sayac_4 and y_secilen.value==7:
            return (x_secilen.value,y_secilen.value-2)


def siyahpiyon_sag_capraz(x_secilen, y_secilen, secilen_tas,sheet):
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=2, max_col=2):
        for cell in row:
            if cell.value == x_secilen.value + 1:
                y = sheet.cell(cell.row, 3)
                olen_tas = sheet.cell(cell.row, 1).value
                if y.value == y_secilen.value - 1:
                    if "Beyaz" in olen_tas:
                        return(x_secilen.value+1,y_secilen.value-1)


def siyahpiyon_sol_capraz(x_secilen, y_secilen, secilen_tas,sheet):
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=2, max_col=2):
        for cell in row:
            if cell.value == x_secilen.value - 1:
                y = sheet.cell(cell.row, 3)
                olen_tas = sheet.cell(cell.row, 1).value
                if y.value == y_secilen.value - 1:
                    if "Beyaz" in olen_tas:
                        return(x_secilen.value-1,y_secilen.value-1)


def siyahpiyon_degistirme(x_yeni,y_yeni,isim,sheet):
    liste=[]
    x=int(input("Piyonun Vezir olmasi icin 1'e\nKale olmasi icin 2'ye\nFil olmasi icin 3'e\nAt olmasi icin 4'e basiniz.\n"))
    for row in sheet.iter_rows(min_row=2,max_row=33,min_col=1,max_col=1):
        for cell in row:
            if cell.value==isim:
                if x==1:
                    for row1 in sheet.iter_rows(min_row=2, max_row=33, min_col=1, max_col=1):
                        for cell1 in row1:
                            try:
                                if "Siyah Vezir" in cell1.value:
                                    liste.append(cell1.value)
                            except TypeError:
                                a=1
                    liste.sort(reverse=True)
                    if liste!=[]:
                        deger=int(liste[0][-1])+1
                    else:
                        deger=1
                    sheet.cell(cell.row,cell.column,value=f"Siyah Vezir{deger}")
                    print(f"Siyah Vezir{deger}'in yeni konumu ({x_yeni},{y_yeni}).")
                if x==2:
                    for row1 in sheet.iter_rows(min_row=2, max_row=33, min_col=1, max_col=1):
                        for cell1 in row1:
                            try:
                                if "Siyah Kale" in cell1.value:
                                    liste.append(cell1.value)
                            except TypeError:
                                a=1
                    liste.sort(reverse=True)
                    if liste != []:
                        deger = int(liste[0][-1]) + 1
                    else:
                        deger = 1
                    sheet.cell(cell.row,cell.column,value=f"Siyah Kale{deger}")
                    print(f"Siyah Kale{deger}'in yeni konumu ({x_yeni},{y_yeni}).")
                if x==3:
                    for row1 in sheet.iter_rows(min_row=2, max_row=33, min_col=1, max_col=1):
                        for cell1 in row1:
                            try:
                                if "Siyah Fil" in cell1.value:
                                    liste.append(cell1.value)
                            except TypeError:
                                a=1
                    liste.sort(reverse=True)
                    if liste != []:
                        deger = int(liste[0][-1]) + 1
                    else:
                        deger = 1
                    sheet.cell(cell.row,cell.column,value=f"Siyah Fil{deger}")
                    print(f"Siyah Fil{deger}'in yeni konumu ({x_yeni},{y_yeni}).")
                if x==4:
                    for row1 in sheet.iter_rows(min_row=2, max_row=33, min_col=1, max_col=1):
                        for cell1 in row1:
                            try:
                                if "Siyah At" in cell1.value:
                                    liste.append(cell1.value)
                            except TypeError:
                                a=1
                    liste.sort(reverse=True)
                    if liste != []:
                        deger = int(liste[0][-1]) + 1
                    else:
                        deger = 1
                    sheet.cell(cell.row,cell.column,value=f"Siyah At{deger}")
                    print(f"Siyah At{deger}'in yeni konumu ({x_yeni},{y_yeni}).")