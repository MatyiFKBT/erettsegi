# Érettségi letöltő
![](https://imgur.com/DS7qQay.gif)

Letölthető [innen a legfrissebb változat](https://github.com/MatyiFKBT/erettsegi/releases)

Ez a kis python program bekéri az évjáratot, a hónapot, illetve a tantárgyakat, és azonnal letölti az adott érettségi feladatsorokat .pdf-ben, illetve a megoldásokat egy *megoldás* mappába.

Informatika esetén a forrásokat is, amit ki is tömörít a megfelelő mappába, ahova a .pdf-eket is elhelyezi azzal a lendülettel, így a felhasználó végeredményként csak egy mappát kap benne a sok-sok feladattal. ::wink::
# A bekért adatok formátuma:
 - év (2 számjegy, 2017 esetén `17`)
 - május/október dönti el hogy őszi vagy tavaszi vizgsa, itt `maj` vagy `okt` a lehetséges érték
 - szint:`emelt` vagy `kozep`
- tárgyak szóközzel, többet is meg lehet adni, hogy egybe letöltse a program:
- **Fontos! A tanárgyakat az oktatas.hu-n szereplő formában kell megadni:**
    - magyar irodalom: `magyir`
    - informatika: `inf`
    - történelem: `tort`
    - matematika: `mat`
    - nyelvek esetén ékezet nélkül pl **`angol, nemet`**
- A végén a program újrafuttatható, amennyiben másik évjárat tárgyait is szeretnénk letölteni, ilyenkor a program már az előzőleg bekért tárgyak listájából is tud dolgozni.