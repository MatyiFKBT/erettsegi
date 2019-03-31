import os
from letolt import letoltp #letoltp = letolt + print
from letolt import letolts #secret
secret = 0
while True:
    os.system('cls')
    jelenhó = 'maj'
    beszint= 'kozep'
    beév = input('Add meg az évszámot, illetve a hónapot,vagy nyomj Entert ha megfelel a jelenlegi: \n Például: 15 okt\n') or '15 okt'
    if beév == 'secret':
        secret = 1
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
            beszint = input('Ha megfelel, nyomj Entert, vagy adj meg egy szintet:\n') or jelenszint
            break
        except:
            beszint = input('Nincs eltárolva szint, kozep/emelt\n')
            jelenszint = beszint
            break
    while True:
        try:
            print('Jelenlegi: ', betárgyak)
            jelentárgyak = betárgyak
            betárgy = input('Ha jó az előző adag akkor nyomj Entert, vagy adj meg tárgyakat:\n') or jelentárgyak
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
    bemappa = input('Ha szeretnéd megadni, hogy hova mentsen a program, itt megteheted\nAmennyiben jó a telepítési/jelenlegi könyvtár, akkor nyomj egy Entert:\n')
    if bemappa != '':
        for tárgy in betárgyak:
            letoltp(év,behó,beszint,tárgy,bemappa)
    elif bemappa == '':
        for tárgy in betárgyak:    
            letoltp(év,behó,beszint,tárgy)
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
        print('Kész is vagyunk.')
        if bemappa != '':
            print('Érdemes a fájlokat áthelyezni!')
        print('Nyomj egy Entert a mappa megnyitásához...')
        input()
        if bemappa != '':
            os.startfile(bemappa)
        elif bemappa == '':
            os.startfile(os.getcwd())
        break

if secret == 1:
    tárgy = input('Tárgy?\n')
    bemappa = input('Ha szeretnéd megadni, hogy hova mentsen a program, itt megteheted\nHa jó a telepítési könyvtár, akkor nyomj egy Entert:\n')
    folder = bemappa+'/'+tárgy
    évek = input('Kezdő és vég év szóközzel? ')
    beszint = input('Szint ékezet nélkül? ')
    behó = input('maj vagy okt? ')
    for év in range(int(évek.split()[0]), int(évek.split()[1])+1):
        if bemappa != '':
                letolts(str(év),behó,beszint,tárgy,bemappa)
        elif bemappa == '':  
                print('Nincs mappa.')
                #letolts(str(év),behó,beszint,tárgy)