def siyahat(x_secilen,y_secilen,secilen_tas,sheet):
    h1=siyahat_saga_ve_bir_yukari(x_secilen,y_secilen,secilen_tas,sheet)
    h2=siyahat_saga_ve_iki_yukari(x_secilen,y_secilen,secilen_tas,sheet)
    h3=siyahat_saga_ve_bir_asagi(x_secilen,y_secilen,secilen_tas,sheet)
    h4=siyahat_saga_ve_iki_asagi(x_secilen,y_secilen,secilen_tas,sheet)
    h5=siyahat_sola_ve_bir_yukari(x_secilen,y_secilen,secilen_tas,sheet)
    h6=siyahat_sola_ve_iki_yukari(x_secilen,y_secilen,secilen_tas,sheet)
    h7=siyahat_sola_ve_bir_asagi(x_secilen,y_secilen,secilen_tas,sheet)
    h8=siyahat_sola_ve_iki_asagi(x_secilen,y_secilen,secilen_tas,sheet)
    geri=h1+h2+h3+h4+h5+h6+h7+h8
    return geri,geri

def siyahat_saga_ve_bir_yukari(x_secilen,y_secilen,secilen_tas,sheet):
    x=x_secilen.value+2
    y=y_secilen.value+1
    konum=[]
    sayac=0
    if x>8 or y>8:
        konum=[]
    else:
        for row in sheet.iter_rows(min_row=2,max_row=33,min_col=2,max_col=2):
            for cell in row:
                if x==cell.value and y==sheet.cell(cell.row,3).value:
                    if "Beyaz" in sheet.cell(cell.row,1).value:
                        konum.append((x, y))
                else:
                    sayac=sayac+1
                    if sayac==32:
                        konum.append((x, y))
    return konum

def siyahat_saga_ve_iki_yukari(x_secilen,y_secilen,secilen_tas,sheet):
    x=x_secilen.value+1
    y=y_secilen.value+2
    konum=[]
    sayac=0
    if x>8 or y>8:
        konum=[]
    else:
        for row in sheet.iter_rows(min_row=2,max_row=33,min_col=2,max_col=2):
            for cell in row:
                if x==cell.value and y==sheet.cell(cell.row,3).value:
                    if "Beyaz" in sheet.cell(cell.row,1).value:
                        konum.append((x, y))
                else:
                    sayac=sayac+1
                    if sayac==32:
                        konum.append((x, y))
    return konum


def siyahat_saga_ve_bir_asagi(x_secilen,y_secilen,secilen_tas,sheet):
    x=x_secilen.value+2
    y=y_secilen.value-1
    konum=[]
    sayac=0
    if x>8 or y<1:
        konum=[]
    else:
        for row in sheet.iter_rows(min_row=2,max_row=33,min_col=2,max_col=2):
            for cell in row:
                if x==cell.value and y==sheet.cell(cell.row,3).value:
                    if "Beyaz" in sheet.cell(cell.row,1).value:
                        konum.append((x, y))
                else:
                    sayac=sayac+1
                    if sayac==32:
                        konum.append((x, y))
    return konum


def siyahat_saga_ve_iki_asagi(x_secilen,y_secilen,secilen_tas,sheet):
    x=x_secilen.value+1
    y=y_secilen.value-2
    konum=[]
    sayac=0
    if x>8 or y<1:
        konum=[]
    else:
        for row in sheet.iter_rows(min_row=2,max_row=33,min_col=2,max_col=2):
            for cell in row:
                if x==cell.value and y==sheet.cell(cell.row,3).value:
                    if "Beyaz" in sheet.cell(cell.row,1).value:
                        konum.append((x, y))
                else:
                    sayac=sayac+1
                    if sayac==32:
                        konum.append((x, y))
    return konum


def siyahat_sola_ve_bir_yukari(x_secilen, y_secilen, secilen_tas,sheet):
    x = x_secilen.value -2
    y = y_secilen.value +1
    konum = []
    sayac = 0
    if x <1 or y > 8:
        konum = []
    else:
        for row in sheet.iter_rows(min_row=2, max_row=33, min_col=2, max_col=2):
            for cell in row:
                if x == cell.value and y == sheet.cell(cell.row, 3).value:
                    if "Beyaz" in sheet.cell(cell.row, 1).value:
                        konum.append((x, y))
                else:
                    sayac = sayac + 1
                    if sayac == 32:
                        konum.append((x, y))
    return konum


def siyahat_sola_ve_iki_yukari(x_secilen, y_secilen, secilen_tas,sheet):
    x=x_secilen.value-1
    y=y_secilen.value+2
    konum=[]
    sayac=0
    if x<1 or y>8:
        konum=[]
    else:
        for row in sheet.iter_rows(min_row=2,max_row=33,min_col=2,max_col=2):
            for cell in row:
                if x==cell.value and y==sheet.cell(cell.row,3).value:
                    if "Beyaz" in sheet.cell(cell.row,1).value:
                        konum.append((x, y))
                else:
                    sayac=sayac+1
                    if sayac==32:
                        konum.append((x, y))
    return konum


def siyahat_sola_ve_bir_asagi(x_secilen, y_secilen, secilen_tas,sheet):
    x=x_secilen.value-2
    y=y_secilen.value-1
    konum=[]
    sayac=0
    if x<1 or y<1:
        konum=[]
    else:
        for row in sheet.iter_rows(min_row=2,max_row=33,min_col=2,max_col=2):
            for cell in row:
                if x==cell.value and y==sheet.cell(cell.row,3).value:
                    if "Beyaz" in sheet.cell(cell.row,1).value:
                        konum.append((x, y))
                else:
                    sayac=sayac+1
                    if sayac==32:
                        konum.append((x, y))
    return konum


def siyahat_sola_ve_iki_asagi(x_secilen, y_secilen, secilen_tas,sheet):
    x=x_secilen.value-1
    y=y_secilen.value-2
    konum=[]
    sayac=0
    if x<1 or y<1:
        konum=[]
    else:
        for row in sheet.iter_rows(min_row=2,max_row=33,min_col=2,max_col=2):
            for cell in row:
                if x==cell.value and y==sheet.cell(cell.row,3).value:
                    if "Beyaz" in sheet.cell(cell.row,1).value:
                        konum.append((x, y))
                else:
                    sayac=sayac+1
                    if sayac==32:
                        konum.append((x, y))
    return konum
