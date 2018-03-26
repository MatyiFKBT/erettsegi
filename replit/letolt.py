import requests
import shutil
import os
import sys
import zipfile
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
    #print(feladatlap, 'letöltése folyamatban...')
    feladatle = requests.get(feladatlap, allow_redirects=True)
    if feladatok == 2:
        #print(feladatlap2, 'letöltése folyamatban...')
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
        #print(forrasok, 'letöltése folyamatban...')
        forrasle = requests.get(forrasok, allow_redirects=True)
        open(zipfajl, 'wb').write(forrasle.content) #forrás írása
        zipfile.ZipFile(zipfajl, 'r').extractall(évmo)
        open(zipfajl, 'wb').close()
        os.remove(zipfajl)
    
    #print(megoldas, 'letöltése folyamatban...')
    megoldasle = requests.get(megoldas, allow_redirects=True)
    open(mpdf, 'wb').write(megoldasle.content) #megoldás írása
    shutil.move(mpdf, megoldás)
    shutil.move(pdf, évmo)
    if feladatok == 2:
        shutil.move(pdf2, évmo)
    return
def letoltp(év, mo, szint, tárgy, *args):
    #printeli a folyamatot
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