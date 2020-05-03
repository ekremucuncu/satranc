def siyahvezir(x_secilen,y_secilen,secilen_tas,sheet):
    h1=siyahvezir_arka(x_secilen,y_secilen,secilen_tas,sheet)
    h2=siyahvezir_on(x_secilen,y_secilen,secilen_tas,sheet)
    h3=siyahvezir_sol(x_secilen,y_secilen,secilen_tas,sheet)
    h4=siyahvezir_sag(x_secilen,y_secilen,secilen_tas,sheet)
    h5=siyahvezir_sag_yukari(x_secilen,y_secilen,secilen_tas,sheet)
    h6=siyahvezir_sol_yukari(x_secilen,y_secilen,secilen_tas,sheet)
    h7=siyahvezir_sag_asagi(x_secilen,y_secilen,secilen_tas,sheet)
    h8=siyahvezir_sol_asagi(x_secilen,y_secilen,secilen_tas,sheet)
    geri=h1+h2+h3+h4+h5+h6+h7+h8
    h2.sort(reverse=True, key=takefirst)
    h4.sort(reverse=True, key=takezero)
    h5.sort(reverse=True,key=takezero)
    h7.sort(reverse=True,key=takezero)
    h8.sort(reverse=False, key=takezero)
    ileri = (h1, h2, h3, h4, h5, h6, h7, h8)
    return geri,ileri


def takeSecond(elem):
    return elem[2]


def takefirst(elem):
    return elem[1]


def takezero(elem):
    return elem[0]

def siyahvezir_on(x_secilen,y_secilen,secilen_tas,sheet):
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


def siyahvezir_arka(x_secilen,y_secilen,secilen_tas,sheet):
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


def siyahvezir_sag(x_secilen,y_secilen,secilen_tas,sheet):
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
                konum.append((i,x_secilen.value))
    return konum


def siyahvezir_sol(x_secilen,y_secilen,secilen_tas,sheet):
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


def siyahvezir_sag_yukari(x_secilen,y_secilen,secilen_tas,sheet):
    liste=[]
    konum=[]
    for row in sheet.iter_rows(min_row=2,max_row=33,min_col=2,max_col=2):
        for cell in row:
            for i in range (1,8):
                if cell.value==x_secilen.value+i:
                    y=sheet.cell(cell.row,3).value
                    if y==y_secilen.value+i:
                        liste.append((sheet.cell(cell.row,1).value,cell.value,y))
    liste.sort(key=takeSecond)
    if liste==[]:
        if x_secilen.value>=y_secilen.value:
            gidilecek_max_x=8
            j=-1
            for i in range(x_secilen.value+1,gidilecek_max_x+1):
                j=j+1
                konum.append((i,y_secilen.value+j+1))
        else:
            gidilecek_max_y=8
            j=-1
            for i in range(y_secilen.value+1,gidilecek_max_y+1):
                j=j+1
                konum.append((x_secilen.value+j+1,i))
    else:
        if "Beyaz" in liste[0][0]:
            olen_tas=liste[0][0]
            gidilecek_max_x=liste[0][1]
            j=-1
            for i in range(x_secilen.value+1,gidilecek_max_x+1):
                j=j+1
                konum.append((i,y_secilen.value+j+1))
        else:
            gidilecek_max_x=liste[0][1]-1
            j=-1
            for i in range(x_secilen.value+1,gidilecek_max_x+1):
                j=j+1
                konum.append((i,y_secilen.value+j+1))
    return konum


def siyahvezir_sol_yukari(x_secilen,y_secilen,secilen_tas,sheet):
    liste = []
    konum = []
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=2, max_col=2):
        for cell in row:
            for i in range(1, 8):
                if cell.value == x_secilen.value - i:
                    y = sheet.cell(cell.row, 3).value
                    if y == y_secilen.value + i:
                        liste.append((sheet.cell(cell.row, 1).value, cell.value, y))
    liste.sort(key=takeSecond)
    if liste == []:
        gidilecek_max_x=1
        gidilecek_max_y=8
        yakinlik_x=x_secilen.value-gidilecek_max_x
        yakinlik_y=gidilecek_max_y-y_secilen.value
        if yakinlik_x<=yakinlik_y:
            j=-1
            for i in range(gidilecek_max_x,x_secilen.value):
                j=j+1
                konum.append((i,y_secilen.value+x_secilen.value-i))
        if yakinlik_y<yakinlik_x:
            j=-1
            for i in range(y_secilen.value+1,gidilecek_max_y+1):
                j=j+1
                konum.append((x_secilen.value+y_secilen.value-i,i))
    else:
        if "Beyaz" in liste[0][0]:
            olen_tas = liste[0][0]
            gidilecek_max_x = liste[0][1]
            j = -1
            for i in range(gidilecek_max_x, x_secilen.value):
                j = j + 1
                konum.append((x_secilen.value-j-1, y_secilen.value + j + 1))
        else:
            gidilecek_max_x = liste[0][1]+1
            j = -1
            for i in range(gidilecek_max_x, x_secilen.value):
                j = j + 1
                konum.append((x_secilen.value - j - 1, y_secilen.value + j + 1))
    return konum


def siyahvezir_sag_asagi(x_secilen,y_secilen,secilen_tas,sheet):
    liste = []
    konum = []
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=2, max_col=2):
        for cell in row:
            for i in range(1, 8):
                if cell.value == x_secilen.value +i:
                    y = sheet.cell(cell.row, 3).value
                    if y == y_secilen.value - i:
                        liste.append((sheet.cell(cell.row, 1).value, cell.value, y))
    liste.sort(key=takeSecond,reverse=True)
    if liste == []:
        gidilecek_max_x=8
        gidilecek_max_y=1
        yakinlik_x=gidilecek_max_x-x_secilen.value
        yakinlik_y=y_secilen.value-gidilecek_max_y
        if yakinlik_x<=yakinlik_y:
            j=-1
            for i in range(x_secilen.value+1,gidilecek_max_x+1):
                j=j+1
                konum.append((i,y_secilen.value+x_secilen.value-i))
        if yakinlik_y<yakinlik_x:
            j=-1
            for i in range(gidilecek_max_y,y_secilen.value):
                j=j+1
                konum.append((x_secilen.value+i,y_secilen.value-i))
    else:
        if "Beyaz" in liste[0][0]:
            olen_tas = liste[0][0]
            gidilecek_max_x = liste[0][1]
            j = -1
            for i in range(x_secilen.value+1,gidilecek_max_x+1):
                j = j + 1
                konum.append((i, y_secilen.value -j-1))
        else:
            gidilecek_max_x = liste[0][1]
            j = -1
            for i in range(x_secilen.value+1,gidilecek_max_x):
                j = j + 1
                konum.append((i,y_secilen.value-j-1))
    return konum


def siyahvezir_sol_asagi(x_secilen,y_secilen,secilen_tas,sheet):
    liste = []
    konum = []
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=2, max_col=2):
        for cell in row:
            for i in range(1, 8):
                if cell.value == x_secilen.value - i:
                    y = sheet.cell(cell.row, 3).value
                    if y == y_secilen.value - i:
                        liste.append((sheet.cell(cell.row, 1).value, cell.value, y))
    liste.sort(key=takeSecond,reverse=True)
    if liste == []:
        if x_secilen.value <= y_secilen.value:
            gidilecek_max_x = 1
            j = -1
            for i in range(gidilecek_max_x,x_secilen.value):
                j = j + 1
                konum.append((x_secilen.value-j-1, y_secilen.value - j - 1))
        else:
            gidilecek_max_y = 1
            j = -1
            for i in range(gidilecek_max_y,y_secilen.value):
                j = j + 1
                konum.append((x_secilen.value-j-1,y_secilen.value-j-1))
    else:
        if "Beyaz" in liste[0][0]:
            olen_tas = liste[0][0]
            gidilecek_max_x = liste[0][1]
            j = -1
            for i in range(gidilecek_max_x,x_secilen.value):
                j = j + 1
                konum.append((x_secilen.value-j-1, y_secilen.value - j - 1))
        else:
            gidilecek_max_x = liste[0][1]+1
            j = -1
            for i in range(gidilecek_max_x,x_secilen.value):
                j = j + 1
                konum.append((x_secilen.value-j-1,y_secilen.value-j-1))

    return konum
