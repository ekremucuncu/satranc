def siyahkale(x_secilen,y_secilen,secilen_tas,sheet):
    h1=siyahkale_arka(x_secilen,y_secilen,secilen_tas,sheet)
    h2=siyahkale_on(x_secilen,y_secilen,secilen_tas,sheet)
    h3=siyahkale_sol(x_secilen,y_secilen,secilen_tas,sheet)
    h4=siyahkale_sag(x_secilen,y_secilen,secilen_tas,sheet)
    geri=h1+h2+h3+h4
    h2.sort(reverse=True, key=takefirst)
    h4.sort(reverse=True, key=takezero)
    ileri = (h1, h2, h3, h4)
    return geri, ileri


def takeSecond(elem):
    return elem[2]


def takefirst(elem):
    return elem[1]


def takezero(elem):
    return elem[0]


def siyahkale_on(x_secilen,y_secilen,secilen_tas,sheet):
    liste = []
    konum = []
    for row in sheet.iter_rows(min_row=2,max_row=33,min_col=2,max_col=2):
        for cell in row:
            if cell.value==x_secilen.value:
                y=sheet.cell(cell.row,3).value
                if y_secilen.value<y:
                    liste.append((sheet.cell(cell.row,1).value,x_secilen.value,y))
    liste.sort(key=takeSecond)
    if liste==[]:
        liste.append((x_secilen.value,8))
        gidilecek_max=liste[0][1]
        j=-1
        for i in range(y_secilen.value+1,gidilecek_max+1):
            j=j+1
            konum.append((x_secilen.value,i))
    else:
        if "Beyaz" in liste[0][0]:
            gidilecek_max=liste[0][2]
            olen_tas=liste[0][0]
            j=-1
            for i in range(y_secilen.value+1,gidilecek_max+1):
                j=j+1
                konum.append((x_secilen.value,i))
        else:
            gidilecek_max=liste[0][2]-1
            j=-1
            for i in range(y_secilen.value+1,gidilecek_max+1):
                j=j+1
                konum.append((x_secilen.value,i))
    return konum


def siyahkale_arka(x_secilen,y_secilen,secilen_tas,sheet):
    liste = []
    konum = []
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=2, max_col=2):
        for cell in row:
            if cell.value == x_secilen.value:
                y = sheet.cell(cell.row, 3).value
                if y_secilen.value > y:
                    liste.append((sheet.cell(cell.row,1).value,x_secilen.value,y))
    liste.sort(reverse=True,key=takeSecond)
    if liste==[]:
        liste.append((x_secilen.value, 1))
        gidilecek_max = liste[0][1]
        j = -1
        for i in range(gidilecek_max,y_secilen.value):
            j = j + 1
            konum.append((x_secilen.value, i))
    else:
        if "Beyaz" in liste[0][0]:
            gidilecek_max=liste[0][2]
            olen_tas=liste[0][0]
            j=-1
            for i in range(gidilecek_max,y_secilen.value):
                j=j+1
                konum.append((x_secilen.value,i))
        else:
            gidilecek_max=liste[0][2]+1
            j=-1
            for i in range(gidilecek_max,y_secilen.value):
                j=j+1
                konum.append((x_secilen.value,i))
    return konum


def siyahkale_sag(x_secilen,y_secilen,secilen_tas,sheet):
    liste=[]
    konum=[]
    for row in sheet.iter_rows(min_row=2,max_row=33,min_col=3,max_col=3):
        for cell in row:
            if cell.value==y_secilen.value:
                x=sheet.cell(cell.row,2).value
                if x>x_secilen.value:
                    liste.append((sheet.cell(cell.row,1).value,x,y_secilen.value))
    liste.sort(key=takefirst)
    if liste==[]:
        liste.append((8,y_secilen.value))
        gidilecek_max=liste[0][0]
        j=-1
        for i in range(x_secilen.value+1,gidilecek_max+1):
            j=j+1
            konum.append((i,y_secilen.value))

    else:
        if "Beyaz" in liste[0][0]:
            gidilecek_max=liste[0][1]
            olen_tas=liste[0][0]
            j=-1
            for i in range(x_secilen.value+1,gidilecek_max+1):
                j=j+1
                konum.append((i,y_secilen.value))
        else:
            gidilecek_max=liste[0][1]
            j=-1
            for i in range(x_secilen.value+1,gidilecek_max):
                j=j+1
                konum.append((i,y_secilen.value))
    return konum


def siyahkale_sol(x_secilen,y_secilen,secilen_tas,sheet):
    liste = []
    konum = []
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=3, max_col=3):
        for cell in row:
            if cell.value == y_secilen.value:
                x = sheet.cell(cell.row, 2).value
                if x < x_secilen.value:
                    liste.append((sheet.cell(cell.row, 1).value, x, y_secilen.value))
    liste.sort(reverse=True,key=takefirst)
    if liste==[]:
        liste.append((1,y_secilen.value))
        gidilecek_max=liste[0][0]
        j=-1
        for i in range(gidilecek_max,x_secilen.value):
            j=j+1
            konum.append((i,y_secilen.value))
    else:
        if "Beyaz" in liste[0][0]:
            gidilecek_max = liste[0][1]
            olen_tas = liste[0][0]
            for i in range(gidilecek_max,x_secilen.value):
                konum.append((i, y_secilen.value))
        else:
            gidilecek_max=liste[0][1]+1
            j=-1
            for i in range(gidilecek_max,x_secilen.value):
                j=j+1
                konum.append((i,y_secilen.value))
    return konum
