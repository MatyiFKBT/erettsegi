import requests
import zipfile
import os
import shutil
os.system('cls') #clear screen

while True:
    év = input("Évjárat? ") # 2 számjegyet vár a program
    mo = input("maj / okt? ") # május/október eldöntése, fontos hogy 3 karakter legyen az input
    folder = év + mo
    pdf = év + mo + '.pdf'
    forras = év + mo + '.zip'
    if mo == 'okt':
        évszak = 'osz'
    else:
        évszak = 'tavasz'

    if mo == 'maj': #tavaszi szezon meghatározása
        url = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20' + év + évszak + '_emelt/e_inf_' + év + mo + '_fl.pdf'
        forrasok = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20' + év + évszak + '_emelt/e_inffor_' + év + mo + '_fl.zip'
    else:
        url = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20' + év + 'osz_emelt/e_inf_' + év + mo + '_fl.pdf'
        forrasok = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20' + év + 'osz_emelt/e_inffor_' + év + mo + '_fl.zip'

    print('Mappa kész.\n')
    print(url, 'letöltése folyamatban...')
    print(forrasok, 'letöltése folyamatban...')

    r = requests.get(url, allow_redirects=True)
    f = requests.get(forrasok, allow_redirects=True)

    open(forras, 'wb').write(f.content) #forrás letöltése
    zipfile.ZipFile(forras, 'r').extractall(év + mo) #új mappa, oda megy az extract
    open(forras, 'wb').close() #becsukjuk a forrásfájlt pythonban, hogy később tudjuk törölni, itt a fájlt lenullázza a python
    os.remove(forras) #töröljük, hiszen már egyszer kitömörítettük, meg amúgyis üres
    open(pdf, 'wb').write(r.content) #feladatlap letöltése

    shutil.move(pdf, folder)
    print('Sikeresen letöltve.')

# ez a while true -s megoldás elég csúnya, de legalább működik.
    while True:
        még = input('Szeretnél még mást is letölteni? (i/n): ')
        if még in ('i', 'n'):
            break
        print('Sajnos ezt nem tudtam értelmezni')
    if még == 'i':
        continue
    else:
        print('Kész is vagyunk.')
        break
