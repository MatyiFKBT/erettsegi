import requests
import zipfile
import os

os.system('cls')


év = input("Évjárat? ") # 2 számjegyet vár a program
mo = input("maj / okt? ") # május/október eldöntése, fontos hogy 3 karakter legyen az input
if mo == 'maj': #tavaszi szezon meghatározása
    url = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20' + év + 'tavasz_emelt/e_inf_' + év + mo + '_fl.pdf'
    forrasok = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20' + év + 'tavasz_emelt/e_inffor_' + év + mo + '_fl.zip'
else:
    url = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20' + év + 'osz_emelt/e_inf_' + év + mo + '_fl.pdf'
    forrasok = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20' + év + 'osz_emelt/e_inffor_' + év + mo + '_fl.zip'

print('Mappa kész.\n')
print(url, 'letöltése folyamatban...')
print(forrasok, 'letöltése folyamatban...')

r = requests.get(url, allow_redirects=True)
f = requests.get(forrasok, allow_redirects=True)
folder = év + mo
pdf = év + mo + '.pdf'
forras = év + mo + '.zip'

open(év + mo + '.zip', 'wb').write(f.content) #ZIP LETÖLTÉSE
zip = zipfile.ZipFile(forras, 'r')
zip.extractall(év + mo) #új mappa, oda megy az extract
open(pdf, 'wb').write(r.content) #PDF
print('Letöltve.')
input()
