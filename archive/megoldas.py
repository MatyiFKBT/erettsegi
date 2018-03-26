import sys
import requests
import shutil
import os
# folder = 0
# f = open('dir.txt')
# for sor in f:
#     folder = sor
#     print(folder)
# év = str(sys.argv[1])
# mo = str(sys.argv[2])
# folder = str(sys.argv[3])
# folder = os.path.dirname(os.path.realpath(__file__))
folder = os.path.basename(os.getcwd())
lista = list(folder)
év = lista[0] + lista[1]
print(év)
mo = lista[2] + lista[3] + lista[4]
if mo == 'maj':
    mpdf = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20' + év + 'tavasz_emelt/e_inf_' + év + mo + '_ut.pdf'
else:
    mpdf = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20' + év + 'osz_emelt/e_inf_' + év + mo + '_ut.pdf'
m = requests.get(mpdf, allow_redirects=True)

megoldas = év + mo + '_ut.pdf'
open(megoldas, 'wb').write(m.content)
# shutil.move(megoldas, folder)
