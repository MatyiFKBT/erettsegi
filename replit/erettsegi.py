import requests
import zipfile
import os
import shutil
bemappavolt = 0
def letolt(év, mo, szint, tárgy, *args):
    if mo == 'okt':
        évszak = 'osz'
        hónap = 'október'
    elif mo =='maj':
        hónap = 'május'
        évszak = 'tavasz'
    folder = év + mo
    pdf = '%s%s%s.pdf'%(tárgy,év,mo)
    zipfajl = 'inf%s%s.zip'%(év,mo)
    mpdf = '%s%s%s_ut.pdf'%(tárgy,év,mo)
    szintbetu = szint[0]
    feladatok = 1
    while True:
        try:
          felhpath = args[0]
          évmo = felhpath+'/'+folder+'/'
          megoldás = évmo+'/Megoldasok'
          break
        except:
          évmo = év+mo
          megoldás = évmo+'/Megoldasok'
          break
    feladatlap = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20%s%s_%s/%s_%s_%s%s_fl.pdf'%(év,évszak,szint,szintbetu,tárgy,év,mo)
    megoldas = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20%s%s_%s/%s_%s_%s%s_ut.pdf'%(év,évszak,szint,szintbetu,tárgy,év,mo)
    if tárgy == 'mat':
        if szint == 'emelt':
            feladatlap = 'https://github.com/MatyiFKBT/erettsegi/raw/master/jimdo/%s/emelt20%s%s.pdf'%(szint,év,hónap)
        elif szint == 'kozep':
            feladatlap = 'https://github.com/MatyiFKBT/erettsegi/raw/master/jimdo/%s/közép20%s%s1.pdf'%(szint,év,hónap)
            feladatlap2 = 'https://github.com/MatyiFKBT/erettsegi/raw/master/jimdo/%s/közép20%s%s2.pdf'%(szint,év,hónap)
            feladatok = 2
    print(feladatlap, 'letöltése folyamatban...')
    feladatle = requests.get(feladatlap, allow_redirects=True)
    if feladatok == 2:
        print(feladatlap2, 'letöltése folyamatban...')
        feladatle2 = requests.get(feladatlap2, allow_redirects=True)
        pdf2 = '%s%s%s2.pdf'%(tárgy,év,mo)
        open(pdf2, 'wb').write(feladatle2.content)
    open(pdf, 'wb').write(feladatle.content) #feladatlap írása
    if not os.path.exists(évmo):
        os.makedirs(évmo)
    if not os.path.exists(évmo):
        os.makedirs(évmo)
    if not os.path.exists(megoldás):
        os.makedirs(megoldás)

    if tárgy == 'inf':
        forrasok = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20%s%s_%s/%s_%sfor_%s%s_fl.zip'%(év,évszak,szint,szintbetu,tárgy,év,mo)
        print(forrasok, 'letöltése folyamatban...')
        forrasle = requests.get(forrasok, allow_redirects=True)
        open(zipfajl, 'wb').write(forrasle.content) #forrás írása
        zipfile.ZipFile(zipfajl, 'r').extractall(évmo)
        open(zipfajl, 'wb').close()
        os.remove(zipfajl)
    
    print(megoldas, 'letöltése folyamatban...')
    megoldasle = requests.get(megoldas, allow_redirects=True)
    open(mpdf, 'wb').write(megoldasle.content) #megoldás írása
    shutil.move(mpdf, megoldás)
    shutil.move(pdf, évmo)
    if feladatok == 2:
        shutil.move(pdf2, évmo)
    return

while True:
    os.system('cls')
    jelenhó = 'maj'
    beszint= 'kozep'
    beév = input('Add meg az évszámot, illetve a hónapot,vagy nyomj Entert ha megfelel a jelenlegi: \n Például: 15 okt\n')
    if beév == 'secret':
        break
    év = beév.split()[0]
    while True:
        try:
            behó = beév.split()[1]
            jelenhó = behó
            break
        except:
            behó = jelenhó
            break
    while True:
        try:
            print('Jelenlegi szint: ',jelenszint)
            beszint = input('Ha megfelel, nyomj Entert, vagy adj meg egy szintet:\n')
            if beszint == '':
                beszint = jelenszint
            break
        except:
            beszint = input('Nincs eltárolva szint, kozep/emelt\n')
            jelenszint = beszint
            break
    while True:
        try:
            print('Jelenlegi: ', betárgyak)
            jelentárgyak = betárgyak
            betárgy = input('Ha jó az előző adag akkor nyomj Entert, vagy adj meg tárgyakat:\n')
            if betárgy == '':
                betárgyak = jelentárgyak
            elif betárgyak != '':
                betárgyak = []
                for tárgy in betárgy.split():
                    betárgyak.append(tárgy)
            break
        except:
            betárgyak = []
            print('Nincs tárolt tárgylista')
            betárgy = input('Tárgyak szóközzel:\n',)
            for tárgy in betárgy.split():
                betárgyak.append(tárgy)
            break
    bemappa = input('Ha szeretnéd megadni, hogy hova mentsen a program, itt megteheted\nHa jó a telepítési könyvtár, akkor nyomj egy Entert:\n')
    if bemappa != '':
        for tárgy in betárgyak:
            letolt(év,behó,beszint,tárgy,bemappa)
    elif bemappa == '':
        for tárgy in betárgyak:    
            letolt(év,behó,beszint,tárgy)
            #print(év,behó,beszint,tárgy)
    while True:
        még = input('Na még egy kör? (i/n) | Enter = n: ')
        if még in ('i', 'n'):
            break
        break
        print('Sajnos ezt nem tudtam értelmezni')
    if még == 'i':
        continue
    else:
        print('Kész is vagyunk.\nÉrdemes a fájlokat áthelyezni!\n\nNyomj egy Entert a mappa megnyitásához...')
        input()
        if bemappa != '':
            os.startfile(bemappa)
        elif bemappa == '':
            os.startfile(os.getcwd())
        break
while True:
    tárgy = input('Tárgy?\n')
    bemappa = input('Ha szeretnéd megadni, hogy hova mentsen a program, itt megteheted\nHa jó a telepítési könyvtár, akkor nyomj egy Entert:\n')
    folder = bemappa+'/'+tárgy
    évek = input('Kezdő és vég év szóközzel? ')
    beszint = input('Szint ékezet nélkül? ')
    behó = input('maj vagy okt? ')
    for év in range(int(évek.split()[0]), int(évek.split()[1])+1):
        if bemappa != '':
                letolt(str(év),behó,beszint,tárgy,bemappa)
        elif bemappa == '':  
                letolt(str(év),behó,beszint,tárgy)

    while True:
        még = input('Na még egy kör? (i/n) | Enter = n: ')
        if még in ('i', 'n'):
            break
        break
        print('Sajnos ezt nem tudtam értelmezni')
    if még == 'i':
        continue
    else:
        print('Kész is vagyunk.\nÉrdemes a fájlokat áthelyezni!\n\nNyomj egy Entert a mappa megnyitásához...')
        input()
        if bemappa != '':
            os.startfile(bemappa)
        elif bemappa == '':
            os.startfile(os.getcwd())
        break