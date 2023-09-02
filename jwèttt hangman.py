import random

def chwazi_mo_aleyatwa(mo_yo):
    return random.choice(list(mo_yo.keys()))

def afiche_deskripsyon(mot, mo_yo):
    print("Deskripsyon mo a:")
    print(mo_yo[mot])

def afiche_mo_kache(mot_kache):
    print("Mo a: " + mot_kache)

def revele_lèt(mot_kache, mo, lèt):
    revele = list(mot_kache)
    for i in range(len(mo)):
        if mo[i] == lèt:
            revele[i] = lèt
    return ''.join(revele)

def devine_lèt():
    lèt_devine = input("Devine yon lèt: ")
    return lèt_devine.lower()

def verifye_devine(lèt_devine, mo_aleyatwa, mot_kache, ese_rete):
    if lèt_devine in mo_aleyatwa:
        print("Bon travay! Lèt la nan mo a.")
        mot_kache = revele_lèt(mot_kache, mo_aleyatwa, lèt_devine)
    else:
        print("se pa kòrèk. Lèt sa pa nan mo a.")
        ese_rete -= 1
        print("Ou gen", ese_rete, "ese rete.")
    return mot_kache, ese_rete

def jwe_jwèt(mo_yo):
    mo_aleyatwa = chwazi_mo_aleyatwa(mo_yo)
    mot_kache = "_" * len(mo_aleyatwa)

    print("Byenveni nan jwèt Hangman! nou ap ba ou yon deskripsyon pou yon mo epi ou ap devine ki mo li ye, w ap antre yon let a chak fwa ou gen selman 5 ese sinon ou pedi.")
    afiche_deskripsyon(mo_aleyatwa, mo_yo)

    max_ese = 5 
    ese_rete = max_ese

    while ese_rete > 0:
        afiche_mo_kache(mot_kache)
        lèt_devine = devine_lèt()
        mot_kache, ese_rete = verifye_devine(lèt_devine, mo_aleyatwa, mot_kache, ese_rete)

        if mot_kache == mo_aleyatwa:
            print("Bravo! Ou genyen! Mo a se:", mo_aleyatwa)
            break

    if mot_kache != mo_aleyatwa:
        print("dezole! Ou pèdi. Mo a se:", mo_aleyatwa)

mo_yo = {
    "piman": "li gen bon gou nan manje, men ou pa ka kraze l anba dan, li gen yon koulè vèt, gen gwo gen piti ",
    "fig": "li mi li gen koule oranj, ayisyen renmen manje l ak pen a manba, epi ze bouyi",
    "pom": "Yon fwi ki souvan wouj oubyen vèt, li manje nan plizyè fason",
    "zaboka": "Yon fwi ki gen koule ki vèt, pafwa vyolet, li manje nan plizyè fason, li donnen sitou nan peryod vakans",
    "yanm": "se yon rasin, ki gwo anpil, moun konn manje l anpil, lel grandi li gwo anpil,fey li monte sou lot pye bwa le lap grandi",
    "machin": "Yon machin se yon aparèy ki sèvi pou deplase moun ak bagay yo.",
    "solèy": "Solèy se etwal ki klere nan syèl la pandan jou."
    
}



while True:
    
    jwe_jwèt(mo_yo)

    rejwe = input("ou vle jwe ankò? (wi/non): ")
    if rejwe.lower() != "wi":
        print("Mèsi paske ou te chwazi jwe Hangman avek nou! n ap tann ou yon pwochen fwa.")
        break