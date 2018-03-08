import requests
import zipfile
import os
import shutil

while True:
    os.system('cls') #clear screen
    be = input("Évjárat, évszak? ") # 2 számjegyet vár a program
    # mo = input("maj / okt? ") # május/október eldöntése, fontos hogy 3 karakter legyen az input
    év = be.split()[0]
    mo = be.split()[1]
    folder = év + mo
    pdf = év + mo + '.pdf'
    forras = év + mo + '.zip'
    megoldas = év + mo + '_ut.pdf'
    if mo == 'okt':
        évszak = 'osz'
    else:
        évszak = 'tavasz'
    url = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20' + év + évszak + '_emelt/e_inf_' + év + mo + '_fl.pdf'
    forrasok = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20' + év + évszak + '_emelt/e_inffor_' + év + mo + '_fl.zip'
    mpdf = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20' + év + évszak + '_emelt/e_inf_' + év + mo + '_ut.pdf'
    #
    # else:
    #     url = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20' + év + 'osz_emelt/e_inf_' + év + mo + '_fl.pdf'
    #     forrasok = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20' + év + 'osz_emelt/e_inffor_' + év + mo + '_fl.zip'
    #     mpdf = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20' + év + 'osz_emelt/e_inf_' + év + mo + '_ut.pdf'

    print('Mappa kész.\n')
    print(url, 'letöltése folyamatban...')
    print(forrasok, 'letöltése folyamatban...')
    print(mpdf, 'letöltése folyamatban...')

    r = requests.get(url, allow_redirects=True)
    f = requests.get(forrasok, allow_redirects=True)
    m = requests.get(mpdf, allow_redirects=True)

    open(forras, 'wb').write(f.content) #forrás letöltése
    print('Kitömörítés...')
    zipfile.ZipFile(forras, 'r').extractall(év + mo) #új mappa, oda megy az extract
    open(forras, 'wb').close() #becsukjuk a forrásfájlt pythonban, hogy később tudjuk törölni, itt a fájlt lenullázza a python
    os.remove(forras) #töröljük, hiszen már egyszer kitömörítettük, meg amúgyis üres
    open(pdf, 'wb').write(r.content) #feladatlap letöltése
    open(megoldas, 'wb').write(m.content)
    shutil.move(megoldas, folder)
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
