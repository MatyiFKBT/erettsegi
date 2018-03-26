import requests
import zipfile
import os
import shutil
import os
be = input("elfogadott tantárgyak = mat, tort, magyir, inf\nÉvjárat évszak szint tantárgy? szóközzel ")

# év = be[0]
# évszak = be[1]
# szint = be[2]
# tárgy = be[3]
def letolt(év, évszak, szint, tárgy):
    mo = ''
    if évszak == 'okt':
        évszak = 'osz'
        mo = 'okt'
    elif évszak =='maj':
        évszak = 'tavasz'
        mo = 'maj'
    folder = év + mo
    pdf = '%s%s%s.pdf'%(tárgy,év,mo)
    zipfajl = 'inf%s%s.zip'%(év,mo)
    mpdf = '%s%s%s_ut.pdf'%(tárgy,év,mo)
    szintbetu = szint[0]
    print(szintbetu)
    feladatlap = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20%s%s_%s/%s_%s_%s%s_fl.pdf'%(év,évszak,szint,szintbetu,tárgy,év,mo)
    megoldas = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20%s%s_%s/%s_%s_%s%s_ut.pdf'%(év,évszak,szint,szintbetu,tárgy,év,mo)
    forrasok = 'http://dload.oktatas.educatio.hu/erettsegi/feladatok_20%s%s_%s/%s_%sfor_%s%s_fl.zip'%(év,évszak,szint,szintbetu,tárgy,év,mo)

    print(feladatlap, 'letöltése folyamatban...')
    feladatle = requests.get(feladatlap, allow_redirects=True)
    open(pdf, 'wb').write(feladatle.content) #feladatlap írása

    if tárgy == 'inf':
        print(forrasok, 'letöltése folyamatban...')
        forrasle = requests.get(forrasok, allow_redirects=True)
        open(zipfajl, 'wb').write(forrasle.content) #forrás írása

    print(megoldas, 'letöltése folyamatban...')
    megoldasle = requests.get(megoldas, allow_redirects=True)
    open(mpdf, 'wb').write(megoldasle.content) #megoldás írása
    mappa = év+'/'+tárgy
    if not os.path.exists(mappa):
        os.makedirs(mappa)
    shutil.move(mpdf, mappa)
    # shutil.move(év/mpdf, tárgy)
    shutil.move(pdf, mappa)
    # shutil.move(év/pdf, tárgy)

    return
# letolt('15','maj','emelt','inf')
letolt(be.split()[0], be.split()[1], be.split()[2], be.split()[3])
