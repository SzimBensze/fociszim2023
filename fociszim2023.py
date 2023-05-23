import random
import time
import re


STAT_JELEN = False
print("Szim Foci Szimulátor 2023 (v1.7)")


def csapat_input(csapat):
    if csapat["oldal"] == "hazai":
        print("Hazai csapat")
        print("-----")
    elif csapat["oldal"] == "vendeg":
        print("Vendég csapat")
        print("-----")
    csapat["nev"] = input("Csapat neve: ")
    try:
        csapat["atk"] = ell100(int(input("Támadás pontok (1-99 között): ")))
        csapat["mid"] = ell100(int(input("Középpálya pontok (1-99 között): ")))
        csapat["def"] = ell100(int(input("Védelem pontok (1-99 között): ")))
        print("-----")
        return csapat
    except ValueError:
        print("Hibás input!")
        return {}


def csapat_print(csapat):
    print("Ellenőrzés: Név - ATK - MID - DEF")
    if csapat["oldal"] == "hazai":
        print(f"Hazai: {csapat['nev']} - {csapat['atk']} - {csapat['mid']} - {csapat['def']}")
    elif csapat["oldal"] == "vendeg":
        print(f"Vendég: {csapat['nev']} - {csapat['atk']} - {csapat['mid']} - {csapat['def']}")
    else:
        print("Hibás input!")


def ell100(input_szam):
    if input_szam > 99:
        return 99
    elif input_szam < 1:
        return 1
    else:
        return input_szam


def esely_print(rand, csapat):
    if csapat["oldal"] == "hazai":
        print(f"R: {rand} H: {csapat['percesely']}")
    elif csapat["oldal"] == "vendeg":
        print(f"R: {rand} V: {csapat['percesely']}")


def csapat_esely(hazcs, vencs, szmertek=6):
    esely = 500
    hazszer = szmertek / 7 + random.randrange(1, 4) / 7
    venszer = szmertek / 7 + random.randrange(1, 4) / 7
    hazesely = esely + (hazcs["atk"]*hazszer - vencs["atk"] + hazcs["mid"] - vencs["mid"] + hazcs["def"] - vencs["atk"]*venszer)
    venesely = esely + (vencs["atk"]*venszer - hazcs["atk"] + vencs["mid"] - hazcs["mid"] + vencs["def"] - hazcs["atk"]*hazszer)
    hazcs["loves"], vencs["loves"], hazcs["gol"], vencs["gol"] = 0, 0, 0, 0
    hazcs["esely"] = hazesely
    vencs["esely"] = venesely
    pass


def felallas(csapat):
    felallasok = {
        "2-3-5": [4, 2, 7],
        "3-4-3": [11, 6, -4],
        "3-5-2": [8, 4, 1],
        "3-6-1": [0, 11, 2],
        "4-3-3": [6, 7, 0],
        "4-4-2": [7, 7, 1],
        "4-5-1": [2, 9, 2],
        "4-6-0": [5, 12, -4],
        "5-3-2": [-2, 4, 11],
        "5-4-1": [-5, 6, 12],
        "X-X-X": [4, 5, 4],
        "3-3-3-1": [3, 13, -3],
        "3-4-1-2": [12, 3, -2],
        "3-4-2-1": [13, 5, -5],
        "4-1-4-1": [-4, 8, 9],
        "4-2-2-2": [4, 4, 5],
        "4-2-3-1": [7, 1, 5],
        "4-3-1-2": [3, 1, 9],
        "4-4-1-1": [2, 6, 5],
        "5-2-1-2": [-4, 4, 13],
        "5-2-2-1": [6, -1, 8],
        "X-X-X-X": [3, 4, 6],
        "X-X-X-X-X": [4, 7, 2]}
    
    print("Felállás input például: \n5-3-2 vagy 4-3-2-1 vagy 4-2-2-1-1 szigorúan ebben a formátumban!")
    felnev = f"{csapat['nev']} felállása: "
    felinput = input(felnev)
    
    if felinput in felallasok:
        csapat["atk"] += felallasok[felinput][0]
        csapat["mid"] += felallasok[felinput][1]
        csapat["def"] += felallasok[felinput][2]
        print(f"Választott felállás: {felinput}")    
    elif re.search("^[0-9]-[0-9]-[0-9]$", felinput):
        csapat["atk"] += felallasok["X-X-X"][0]
        csapat["mid"] += felallasok["X-X-X"][1]
        csapat["def"] += felallasok["X-X-X"][2]
        print("Választott felállás: X-X-X")
    elif re.search("^[0-9]-[0-9]-[0-9]-[0-9]$", felinput):
        csapat["atk"] += felallasok["X-X-X-X"][0]
        csapat["mid"] += felallasok["X-X-X-X"][1]
        csapat["def"] += felallasok["X-X-X-X"][2]
        print("Választott felállás: X-X-X-X")
    elif re.search("^[0-9]-[0-9]-[0-9]-[0-9]-[0-9]$", felinput):
        csapat["atk"] += felallasok["X-X-X-X-X"][0]
        csapat["mid"] += felallasok["X-X-X-X-X"][1]
        csapat["def"] += felallasok["X-X-X-X-X"][2]
        print("Választott felállás: X-X-X-X-X")
    else:
        print("Helytelen formátum!")
    pass


def csapat_percesely(hazcs, vencs, szmertek=6):
    hazszer = szmertek / 10 + random.randrange(1, 3) / 10
    venszer = szmertek / 10 + random.randrange(1, 3) / 10
    hazesely = hazcs["esely"] + (hazcs["atk"]*hazszer - vencs["atk"] + hazcs["mid"] - vencs["mid"] + hazcs["def"] - vencs["atk"]*venszer)/3
    venesely = vencs["esely"] + (vencs["atk"]*venszer - hazcs["atk"] + vencs["mid"] - hazcs["mid"] + vencs["def"] - hazcs["atk"]*hazszer)/3
    randomizalo = 0.1
    hazcs["percesely"] = ((hazesely + hazszer) / 1000) * randomizalo
    vencs["percesely"] = ((venesely + venszer) / 1000) * randomizalo
    if hazcs["percesely"] - vencs["percesely"] >= 0.02:
        hazcs["percesely"] += 0.015
    elif hazcs["percesely"] - vencs["percesely"] >= 0.02:
        vencs["percesely"] += 0.015


def loves(hazcs, vencs, plusz):
    randomizalo = random.random()
    if plusz:
        eselyszorzo = 1.019
    else:
        eselyszorzo = 1
    if randomizalo < hazcs["percesely"] * eselyszorzo:
        hazcs["loves"] += 1
        if STAT_JELEN:
            esely_print(randomizalo, hazcs)
        randomizalo = random.random()
        if randomizalo < (hazcs["percesely"] * (2.3 + hazcs["atk"] / 100 - vencs["def"] / 100)):
            hazcs["gol"] += 1
            print(hazcs["nev"], "GÓÓÓL!")
            if plusz:
                hazcs["percesely"] -= 0.017
            else:
                hazcs["percesely"] -= 0.007
        else:
            print(hazcs["nev"], "sikertelen lövés")
        if STAT_JELEN:
            esely_print(randomizalo, hazcs)
    if plusz:
        hazcs["percesely"] += 0.005
    else:
        hazcs["percesely"] += 0.002
    randomizalo=random.random()
    if randomizalo < vencs["percesely"] * eselyszorzo:
        vencs["loves"] += 1
        if STAT_JELEN:
            esely_print(randomizalo, vencs)
        randomizalo = random.random()
        if randomizalo < (vencs["percesely"] * (2.3 + vencs["atk"] / 100 - hazcs["def"] / 100)):
            vencs["gol"] += 1
            print(vencs["nev"],"GÓÓÓL!")
            if plusz:
                vencs["percesely"] -= 0.019
            else:
                vencs["percesely"] -= 0.009
        else:
            print(vencs["nev"], "sikertelen lövés")
        if STAT_JELEN:
            esely_print(randomizalo, vencs)
    if plusz:
        vencs["percesely"] += 0.005
    else:
        vencs["percesely"] += 0.002
    hazcs["percesely"] -= (vencs["atk"] + vencs["mid"] + vencs["def"]) / 100000
    vencs["percesely"] -= (hazcs["atk"] + hazcs["mid"] + hazcs["def"]) / 100000
    if hazcs["percesely"] <= 0:
        hazcs["percesely"] == 0.0001
    if vencs["percesely"] <= 0:
        vencs["percesely"] == 0.0001


def esemeny_sorsolas(idokezd, idoveg):
    esemeny_szam = [0,0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,3]
    esemenyek = [
        "tizenegyes",
        "tizenegyes",
        "tizenegyes",
        "tizenegyes",
        "tizenegyes",
        "tizenegyes",
        "sarga",
        "sarga",
        "sarga",
        "sarga",
        "piros",
        "piros",
        "vargol",
        "vargol",
        "nincsgol",
        "nincsgol",
        "serules",
        "baleset",
        "szurkolo",
        "semmi"]
    esemeny_lista = {}
    for _ in range(random.choice(esemeny_szam)):
        esemeny_lista[random.randrange(idokezd, idoveg)] = random.choice(esemenyek)
    #print(esemeny_lista)
    return esemeny_lista


def esemeny_valasztas(esemeny, csapat):
    def pont_print(szam):
        pontok = ""
        for i in range(szam):
            pontok += "."
            print(pontok)
            time.sleep(0.25)
    var = random.choice([True, False])
            
    match esemeny:
        case "tizenegyes":
            print(csapat["nev"], "tizenegyes!")
            time.sleep(2)
            pont_print(3)
            #print(csapat["esely"])
            csapat["loves"] += 1
            if random.randrange(1, 1000) < csapat["esely"]:
                csapat["gol"] += 1
                print(csapat["nev"], "GÓÓÓL!")
            else:
                print(csapat["nev"], "sikertelen lövés")
        case "sarga" | "piros":
            if var:
                print("[!] Incidens kivizsgálása")
                time.sleep(2)
                pont_print(5)
                if esemeny == "sarga":
                    print(f"VAR: {csapat['nev']} sárga lap!")
                    csapat["percesely"] -= 0.001
                elif esemeny == "piros":
                    print(f"VAR: {csapat['nev']} piros lap!")
                    csapat["percesely"] -= 0.01
            else:
                if esemeny == "sarga":
                    print(f"{csapat['nev']} sárga lap!")
                    csapat["percesely"] -= 0.002
                elif esemeny == "piros":
                    print(f"{csapat['nev']} piros lap!")
                    csapat["percesely"] -= 0.015
        case "vargol":
            if var:
                print("[!] GLT ellenőrzés")
            else:
                print("[!] Góleset kivizsgálása")
            time.sleep(2)
            pont_print(5)
            csapat["loves"] += 1
            csapat["gol"] += 1
            print(f"VAR: {csapat['nev']} GÓÓÓL!")
        case "nincsgol":
            csapat["loves"] += 1
            print(f"{csapat['nev']} GÓÓÓL!")
            time.sleep(1)
            if var:
                print("[!] GLT ellenőrzés")
            else:
                print("[!] Góleset kivizsgálása")
            time.sleep(2)
            pont_print(5)
            if var:
                indok = "nincs gól"
            else:
                indok = random.choice(["les", "szabálytalanság", "nincs gól"])
            print(f"VAR: {csapat['nev']} {indok}!")
        case "serules":
            print(csapat["nev"], "sérülés!")
            csapat["percesely"] -= 0.009
            time.sleep(2)
            print("A sérült játékost elszállítják")
            pont_print(5)
        case "baleset":
            print("Akadály került a pályára!")
            time.sleep(2)
            print("A személyzet elintézi a problémát")
            pont_print(3)
        case "szurkolo":
            print("Egy szurkoló beszaladt a pályára!")
            csapat["percesely"] += 0.0005
            time.sleep(2)
            print("A biztonsági őrök elszállítják a drukkert")
            pont_print(3)
        case "semmi":
            print("[!] Incidens kivizsgálása")
            time.sleep(2)
            pont_print(5)
            csapat["percesely"] += 0.002
            print(f"VAR: {csapat['nev']} nincs szabálytalanság!")
    time.sleep(0.5)
    return csapat


def meccs90(hazcs, vencs, idokoz):
    elsplusz = random.choice([0,0,1,1,1,1,2,2,2,2,2,2,3,3,3,3,4,4,4,5])
    masplusz = random.choice([0,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,6])
    esemenyek90 = esemeny_sorsolas(5, 90)
    if len(esemenyek90) >= 2:
        masplusz += 3
    elif len(esemenyek90) >= 1:
        masplusz += 2
    print("Szimuláció indul!")
    time.sleep(2)
    print("A pályát előkészítik...")
    time.sleep(1)
    print("A játékosok bemelegítenek...")
    time.sleep(1)
    print("Kezdőrúgás!")
    time.sleep(idokoz)
    for i in range(1, 91):
        print("Perc:", i)
        loves(hazcs, vencs, False)
        if i in esemenyek90.keys():
            esemeny_valasztas(esemenyek90[i], random.choice([hazcs, vencs]))
            if STAT_JELEN:
                esely_print("-", hazcs)
                esely_print("-", vencs)
        time.sleep(idokoz)
        if i == 45:
            for j in range(elsplusz):
                print("Perc: 45 +", j + 1)
                loves(hazcs, vencs, True)
                time.sleep(idokoz)
            print("Félidő!")
            time.sleep(2)
        if i == 90:
            for j in range(masplusz):
                print("Perc: 90 +", j + 1)
                loves(hazcs, vencs, True)
                time.sleep(idokoz)
            print("Meccs vége!")
            time.sleep(idokoz)
    print("-----")
    print(f"Végeredmény: {hazcs['nev']} - {vencs['nev']} : {hazcs['gol']} - {vencs['gol']}, lövések száma: {hazcs['loves']} - {vencs['loves']}")
    return gyoztes(hazcs, vencs)


def meccs120(hazcs, vencs, idokoz):
    hossz = ""
    while hossz not in ["igen", "nem"]:
        hossz = input("Hosszabbítás? igen/nem: ").lower()
        if hossz == "nem":
            print("Döntetlen! Gratulálunk mindkét csapatnak.")
            return {}
    print("-----")

    hossz_elsplusz = random.choice([0,0,0,1,1,1,1,2,2,3])
    hossz_masplusz = random.choice([0,0,0,1,1,1,2,2,3,4])
    esemenyek120 = esemeny_sorsolas(95, 120)
    
    for i in range(91, 121):
        print("Perc:", i)
        loves(hazcs, vencs, False)
        if i in esemenyek120.keys():
            esemeny_valasztas(esemenyek120[i], random.choice([hazcs, vencs]))
            if STAT_JELEN:
                esely_print("-", hazcs)
                esely_print("-", vencs)
        time.sleep(idokoz)
        if i == 105:
            for j in range(hossz_elsplusz):
                print("Perc: 105 +", j + 1)
                loves(hazcs, vencs, True)
                time.sleep(idokoz)
            print("H. Félidő!")
            time.sleep(2)
        if i == 120:
            for j in range(hossz_masplusz):
                print("Perc: 120 +", j + 1)
                loves(hazcs, vencs, True)
                time.sleep(idokoz)
            print("Hosszabbítás vége!")
            time.sleep(idokoz)
    print("-----")
    print(f"Hosszabbítás után: {hazcs['nev']} - {vencs['nev']} : {hazcs['gol']} - {vencs['gol']}, lövések száma: {hazcs['loves']} - {vencs['loves']}")
    return gyoztes(hazcs, vencs)


def buntetok(hazcs, vencs, idokoz):
    folyt = ""
    while folyt not in ["igen", "nem"]:
        folyt = input("Folytatás? igen/nem: ").lower()
        if folyt == "nem":
            print("Döntetlen! Gratulálunk mindkét csapatnak.")
            return {}
    print("-----")
    erme = random.choice(["F","I"])
    print(f"{hazcs['nev']} - F, {vencs['nev']} - I, érme - {erme}")
    if erme == "F":
        sorrend = [hazcs, vencs]
    else:
        sorrend = [vencs, hazcs]
    hazcs["buntlov"], vencs["buntlov"] = 1, 1
    hazcs["buntetok"], vencs["buntetok"] = "", ""
    time.sleep(2)
    for _ in range(5):
        for lov in sorrend:
            buntloves(lov, 7)
            lov["buntlov"] += 1
            time.sleep(idokoz / 2)
        time.sleep(idokoz)
    print("-----")
    print(f"Büntetők után: {hazcs['nev']} - {vencs['nev']} : {hazcs['gol']} - {vencs['gol']}, lövések: {hazcs['buntetok']} - {vencs['buntetok']}")
    if hazcs["gol"] == vencs["gol"]:
        print("Még nem dőlt el!")
        print("-----")
        time.sleep(2)
        while(hazcs["gol"] == vencs["gol"]):
            for lov in sorrend:
                buntloves(lov, 7)
                lov["buntlov"] += 1
                time.sleep(idokoz / 2)
            time.sleep(idokoz)
        return gyoztes(hazcs, vencs)
    else:
        return gyoztes(hazcs, vencs)


def buntloves(csapat, eselyszorzo):
    print(f"{csapat['nev']} {csapat['buntlov']}. büntető lövése:")
    randomizalo = random.random()
    if STAT_JELEN:
        esely_print(randomizalo, csapat)
    if csapat["percesely"] <= 0:
        csapat["percesely"] = 0.0001
    if randomizalo < (csapat["percesely"] * eselyszorzo):
        print("GÓL!")
        csapat["gol"] += 1
        csapat["buntetok"] += "✓"
    else:
        print("sikertelen")
        csapat["buntetok"] += "✗"
    return csapat


def gyoztes(hazcs, vencs):
    if hazcs["gol"] > vencs["gol"]:
        print(f"Győztes: {hazcs['nev']} Gratulálunk!")
        return hazcs
    elif hazcs["gol"] < vencs["gol"]:
        print(f"Győztes: {vencs['nev']} Gratulálunk!")
        return vencs
    else:
        return None


def main():
    hazai = {"oldal": "hazai"}
    vendeg = {"oldal": "vendeg"}

    print("-----")
    while len(hazai) != 5:
        csapat_input(hazai)
    csapat_print(hazai)
    print("-----")
    while len(vendeg) != 5:
        csapat_input(vendeg)
    csapat_print(vendeg)
    print("-----")

    csapat_esely(hazai, vendeg)

    felallas(hazai)
    print("-----")
    felallas(vendeg)
    print("-----")

    csapat_percesely(hazai, vendeg)

    stat = ""
    while stat not in ["igen", "nem"]:
        stat = input("Esélyek mutatása? igen/nem: ").lower()
    if stat == "igen":
        global STAT_JELEN
        STAT_JELEN = True
        esely_print("kezdés", hazai)
        esely_print("kezdés", vendeg)
    print("-----")

    meccs = meccs90(hazai, vendeg, 0.5)
    if meccs == None:
        hossz = meccs120(hazai, vendeg, 0.5)
        if hossz == None:
            bunt = buntetok(hazai, vendeg, 0.75)
            if bunt == None:
                print("Nincs győztes!")
                print(ValueError("Hibás adat?"))
                time.sleep(1)
                raise ValueError("Hibás adat?")
    
    #print(hazai, vendeg, meccs)
    input()

try:
    main()
except KeyboardInterrupt:
    print("Meccs megszakítva. Nyomj entert a kilépéshez.")
    input()
