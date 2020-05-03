def beyazsah(x_secilen, y_secilen, secilen_tas,sheet):
    h1=beyazsah_arka(x_secilen,y_secilen,secilen_tas,sheet)
    h2=beyazsah_on(x_secilen,y_secilen,secilen_tas,sheet)
    h3=beyazsah_sol(x_secilen,y_secilen,secilen_tas,sheet)
    h4=beyazsah_sag(x_secilen,y_secilen,secilen_tas,sheet)
    h5=beyazsah_sag_yukari(x_secilen,y_secilen,secilen_tas,sheet)
    h6=beyazsah_sol_yukari(x_secilen,y_secilen,secilen_tas,sheet)
    h7=beyazsah_sag_asagi(x_secilen,y_secilen,secilen_tas,sheet)
    h8=beyazsah_sol_asagi(x_secilen,y_secilen,secilen_tas,sheet)
    geri=h1+h2+h3+h4+h5+h6+h7+h8
    ileri = (h1, h2, h3, h4, h5, h6, h7, h8)
    return geri,ileri

def beyazsah_arka(x_secilen,y_secilen,secilen_tas,sheet):
    liste=[]
    konum=[]
    for row in sheet.iter_rows(min_row=2,max_row=33,min_col=2,max_col=2):
        for cell in row:
            if cell.value==x_secilen.value:
                y=sheet.cell(cell.row,3).value
                if y==y_secilen.value-1:
                    liste.append((sheet.cell(cell.row,1).value,cell.value,y))
    if liste==[]:
        if y_secilen.value==1:
            konum=[]
        else:
            liste.append((x_secilen.value,y_secilen.value-1))
            konum.append((liste[0][0],liste[0][1]))
    else:
        olen_tas=liste[0][0]
        if "Siyah" in liste[0][0]:
            konum.append((liste[0][1],liste[0][2]))
    return konum


def beyazsah_on(x_secilen,y_secilen,secilen_tas,sheet):
    liste=[]
    konum=[]
    for row in sheet.iter_rows(min_row=2,max_row=33,min_col=2,max_col=2):
        for cell in row:
            if cell.value==x_secilen.value:
                y=sheet.cell(cell.row,3).value
                if y==y_secilen.value+1:
                    liste.append((sheet.cell(cell.row,1).value,cell.value,y))
    if liste==[]:
        if y_secilen==8:
            konum=[]
        else:
            liste.append((x_secilen.value,y_secilen.value+1))
            konum.append((liste[0][0],liste[0][1]))
    else:
        olen_tas=liste[0][0]
        if "Siyah" in liste[0][0]:
            konum.append((liste[0][1],liste[0][2]))
    return konum


def beyazsah_sol(x_secilen,y_secilen,secilen_tas,sheet):
    liste = []
    konum = []
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=2, max_col=2):
        for cell in row:
            if cell.value == x_secilen.value-1:
                y = sheet.cell(cell.row, 3).value
                if y == y_secilen.value:
                    liste.append((sheet.cell(cell.row, 1).value, cell.value, y))
    if liste == []:
        if x_secilen.value==1:
            konum=[]
        else:
            liste.append((x_secilen.value-1, y_secilen.value))
            konum.append((liste[0][0], liste[0][1]))
    else:
        olen_tas = liste[0][0]
        if "Siyah" in liste[0][0]:
            konum.append((liste[0][1], liste[0][2]))
    return konum


def beyazsah_sag(x_secilen,y_secilen,secilen_tas,sheet):
    liste = []
    konum = []
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=2, max_col=2):
        for cell in row:
            if cell.value == x_secilen.value+1:
                y = sheet.cell(cell.row, 3).value
                if y == y_secilen.value:
                    liste.append((sheet.cell(cell.row, 1).value, cell.value, y))
    if liste == []:
        if x_secilen.value==8:
            konum=[]
        else:
            liste.append((x_secilen.value+1, y_secilen.value))
            konum.append((liste[0][0], liste[0][1]))
    else:
        olen_tas = liste[0][0]
        if "Siyah" in liste[0][0]:
            konum.append((liste[0][1], liste[0][2]))
    return konum


def beyazsah_sag_yukari(x_secilen,y_secilen,secilen_tas,sheet):
    liste = []
    konum = []
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=2, max_col=2):
        for cell in row:
            if cell.value == x_secilen.value+1:
                y = sheet.cell(cell.row, 3).value
                if y == y_secilen.value + 1:
                    liste.append((sheet.cell(cell.row, 1).value, cell.value, y))
    if liste == []:
        if x_secilen.value==8 or y_secilen.value==8:
            konum=[]
        else:
            liste.append((x_secilen.value+1, y_secilen.value + 1))
            konum.append((liste[0][0], liste[0][1]))
    else:
        olen_tas = liste[0][0]
        if "Siyah" in liste[0][0]:
            konum.append((liste[0][1], liste[0][2]))
    return konum


def beyazsah_sol_yukari(x_secilen,y_secilen,secilen_tas,sheet):
    liste = []
    konum = []
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=2, max_col=2):
        for cell in row:
            if cell.value == x_secilen.value-1:
                y = sheet.cell(cell.row, 3).value
                if y == y_secilen.value + 1:
                    liste.append((sheet.cell(cell.row, 1).value, cell.value, y))
    if liste == []:
        if x_secilen.value==1 or y_secilen.value==8:
            konum=[]
        else:
            liste.append((x_secilen.value-1, y_secilen.value + 1))
            konum.append((liste[0][0], liste[0][1]))
    else:
        olen_tas = liste[0][0]
        if "Siyah" in liste[0][0]:
            konum.append((liste[0][1], liste[0][2]))
    return konum


def beyazsah_sag_asagi(x_secilen,y_secilen,secilen_tas,sheet):
    liste = []
    konum = []
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=2, max_col=2):
        for cell in row:
            if cell.value == x_secilen.value+1:
                y = sheet.cell(cell.row, 3).value
                if y == y_secilen.value -1:
                    liste.append((sheet.cell(cell.row, 1).value, cell.value, y))
    if liste == []:
        if x_secilen.value==8 or y_secilen.value==1:
            konum=[]
        else:
            liste.append((x_secilen.value+1, y_secilen.value - 1))
            konum.append((liste[0][0], liste[0][1]))
    else:
        olen_tas = liste[0][0]
        if "Siyah" in liste[0][0]:
            konum.append((liste[0][1], liste[0][2]))
    return konum


def beyazsah_sol_asagi(x_secilen,y_secilen,secilen_tas,sheet):
    liste = []
    konum = []
    for row in sheet.iter_rows(min_row=2, max_row=33, min_col=2, max_col=2):
        for cell in row:
            if cell.value == x_secilen.value-1:
                y = sheet.cell(cell.row, 3).value
                if y == y_secilen.value - 1:
                    liste.append((sheet.cell(cell.row, 1).value, cell.value, y))
    if liste == []:
        if x_secilen.value==1 or y_secilen.value==1:
            konum=[]
        else:
            liste.append((x_secilen.value-1, y_secilen.value - 1))
            konum.append((liste[0][0], liste[0][1]))
    else:
        olen_tas = liste[0][0]
        if "Siyah" in liste[0][0]:
            konum.append((liste[0][1], liste[0][2]))
    return konum
