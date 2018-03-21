import requests
import zipfile
import os
import shutil
def letolt(év, mo, szint, tárgy):
    if mo == 'okt':
        évszak = 'osz'
        mo = 'okt'
    elif mo =='maj':
        évszak = 'tavasz'
        
    folder = év + mo
    pdf = '%s%s%s.pdf'%(tárgy,év,mo)
    zipfajl = 'inf%s%s.zip'%(év,mo)
    mpdf = '%s%s%s_ut.pdf'%(tárgy,év,mo)
    szintbetu = szint[0]
    feladatlap = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20%s%s_%s/%s_%s_%s%s_fl.pdf'%(év,évszak,szint,szintbetu,tárgy,év,mo)
    megoldas = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20%s%s_%s/%s_%s_%s%s_ut.pdf'%(év,évszak,szint,szintbetu,tárgy,év,mo)

    print(feladatlap, 'letöltése folyamatban...')
    feladatle = requests.get(feladatlap, allow_redirects=True)
    open(pdf, 'wb').write(feladatle.content) #feladatlap írása
    évmo = év+mo
    megoldás = évmo+'/Megoldasok'
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

    return
while True:
    os.system('cls')
    jelenhó = 'maj'
    beszint= 'kozep'
    beév = input('Add meg az évszámot, illetve a hónapot,vagy nyomj Entert ha megfelel a jelenlegi: \n Például: 15 okt\n')
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
        os.startfile(os.getcwd())
        break