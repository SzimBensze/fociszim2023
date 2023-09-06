import random
import time
import re


STAT_ON = False
print("Szim Foci Szimulátor 2023 (v1.13)")


def input_team(team):
    if team["side"] == "home":
        print("Hazai csapat")
        print("-----")
    elif team["side"] == "visitor":
        print("Vendég csapat")
        print("-----")
    team["name"] = input("Csapat neve: ")
    team["atk"] = input_points(team["name"], "atk")
    team["mid"] = input_points(team["name"], "mid")
    team["def"] = input_points(team["name"], "def")
    print("-----")
    return team


def print_team(team):
    print("Ellenőrzés: Név - ATK - MID - DEF")
    if team["side"] == "home":
        print(f"Hazai: {team['name']} - {team['atk']} - {team['mid']} - {team['def']}")
    elif team["side"] == "visitor":
        print(f"Vendég: {team['name']} - {team['atk']} - {team['mid']} - {team['def']}")
    else:
        print("Hibás input!")


def print_chances(rand, team):
    if team["side"] == "home":
        print(f"R: {rand} H: {team['minute_chance']}")
    elif team["side"] == "visitor":
        print(f"R: {rand} V: {team['minute_chance']}")


def input_points(name, type):
    types = {"atk": "Támadás", "mid": "Középpálya", "def": "Védelem"}
    input_text = f"{name} {types[type]} pontok (1-99 között): "
    while True:
        try:
            input_num = int(input(input_text))
            if 1 <= input_num <= 100:
                return input_num
            else:
                print("Csak 1 és 99 közötti érték elfogadott!")
        except ValueError:
            print("Hibás input!")


def calc_base_chance(home_team, vis_team, base=500, luck_value=6):
    home_luck = luck_value / 7 + random.randrange(1, 4) / 7
    vis_luck = luck_value / 7 + random.randrange(1, 4) / 7
    home_chance = base + (home_team["atk"] * home_luck - vis_team["def"] + home_team["mid"] - vis_team["mid"] + home_team["def"] - vis_team["atk"] * vis_luck)
    vis_chance = base + (vis_team["atk"] * vis_luck - home_team["def"] + vis_team["mid"] - home_team["mid"] + vis_team["def"] - home_team["atk"] * home_luck)
    home_team["shot"], vis_team["shot"], home_team["goal"], vis_team["goal"] = 0, 0, 0, 0
    home_team["base_chance"], vis_team["base_chance"] = home_chance, vis_chance
    pass


def formation(team):
    formations = {
        "2-3-5": [4, 2, 7],
        "3-4-3": [11, 6, -4],
        "3-5-2": [8, 4, 1],
        "3-6-1": [0, 11, 2],
        "4-3-3": [6, 7, 0],
        "4-4-2": [7, 7, -1],
        "4-5-1": [1, 9, 3],
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
        "4-4-1-1": [2, 7, 4],
        "5-2-1-2": [-4, 4, 13],
        "5-2-2-1": [6, -1, 8],
        "X-X-X-X": [3, 4, 6],
        "3-2-2-2-1": [-1, 4, 10],
        "4-1-2-1-2": [9, 4, 0],
        "4-2-1-2-1": [4, 10, -1],
        "4-2-2-1-1": [10, -2, 5],
        "X-X-X-X-X": [4, 7, 2]}
    
    print("Felállás input például: \n5-3-2 vagy 4-3-2-1 vagy 4-2-2-1-1 szigorúan ebben a formátumban!")
    form_name = f"{team['name']} felállása: "
    input_formation = input(form_name)
    
    if input_formation in formations:
        team["atk"] += formations[input_formation][0]
        team["mid"] += formations[input_formation][1]
        team["def"] += formations[input_formation][2]
        print(f"Választott felállás: {input_formation}")    
    elif re.search("^[0-9]-[0-9]-[0-9](-[0-9])?(-[0-9])?$", input_formation):
        if len(input_formation) == 5:
            team["atk"] += formations["X-X-X"][0]
            team["mid"] += formations["X-X-X"][1]
            team["def"] += formations["X-X-X"][2]
            print("Választott felállás: X-X-X")
        elif len(input_formation) == 7:
            team["atk"] += formations["X-X-X-X"][0]
            team["mid"] += formations["X-X-X-X"][1]
            team["def"] += formations["X-X-X-X"][2]
            print("Választott felállás: X-X-X-X")
        elif len(input_formation) == 9:
            team["atk"] += formations["X-X-X-X-X"][0]
            team["mid"] += formations["X-X-X-X-X"][1]
            team["def"] += formations["X-X-X-X-X"][2]
            print("Választott felállás: X-X-X-X-X")
    else:
        print("Helytelen formátum!")
    pass


def calc_minute_chance(home_team, vis_team, luck_value=6):
    home_luck = luck_value / 10 + random.randrange(1, 3) / 10
    vis_luck = luck_value / 10 + random.randrange(1, 3) / 10
    home_chance = home_team["base_chance"] + (home_team["atk"]*home_luck - vis_team["atk"] + home_team["mid"] - vis_team["mid"] + home_team["def"] - vis_team["atk"]*vis_luck)/3
    vis_chance = vis_team["base_chance"] + (vis_team["atk"]*vis_luck - home_team["atk"] + vis_team["mid"] - home_team["mid"] + vis_team["def"] - home_team["atk"]*home_luck)/3
    randomizer = 0.1
    home_team["minute_chance"] = ((home_chance + home_luck) / 1000) * randomizer
    vis_team["minute_chance"] = ((vis_chance + vis_luck) / 1000) * randomizer
    if home_team["minute_chance"] - vis_team["minute_chance"] >= 0.02:
        home_team["minute_chance"] += 0.015
    elif home_team["minute_chance"] - vis_team["minute_chance"] >= 0.02:
        vis_team["minute_chance"] += 0.015


def shoot_goal(home_team, vis_team, plus, plus_value=1.019):
    randomizer = random.random()
    chance_multiplier = plus_value if plus else 1
    if randomizer < home_team["minute_chance"] * chance_multiplier:
        home_team["shot"] += 1
        if STAT_ON:
            print_chances(randomizer, home_team)
        randomizer = random.random()
        if randomizer < (home_team["minute_chance"] * (2.3 + home_team["atk"] / 100 - vis_team["def"] / 100)):
            home_team["goal"] += 1
            print(home_team["name"], "GÓÓÓL!")
            if plus:
                home_team["minute_chance"] -= 0.017
            else:
                home_team["minute_chance"] -= 0.007
        else:
            print(home_team["name"], "sikertelen lövés")
        if STAT_ON:
            print_chances(randomizer, home_team)
    if plus:
        home_team["minute_chance"] += 0.005
    else:
        home_team["minute_chance"] += 0.002
    randomizer=random.random()
    if randomizer < vis_team["minute_chance"] * chance_multiplier:
        vis_team["shot"] += 1
        if STAT_ON:
            print_chances(randomizer, vis_team)
        randomizer = random.random()
        if randomizer < (vis_team["minute_chance"] * (2.3 + vis_team["atk"] / 100 - home_team["def"] / 100)):
            vis_team["goal"] += 1
            print(vis_team["name"],"GÓÓÓL!")
            if plus:
                vis_team["minute_chance"] -= 0.019
            else:
                vis_team["minute_chance"] -= 0.009
        else:
            print(vis_team["name"], "sikertelen lövés")
        if STAT_ON:
            print_chances(randomizer, vis_team)
    if plus:
        vis_team["minute_chance"] += 0.005
    else:
        vis_team["minute_chance"] += 0.002
    home_team["minute_chance"] -= (vis_team["atk"] + vis_team["mid"] + vis_team["def"]) / 100000
    vis_team["minute_chance"] -= (home_team["atk"] + home_team["mid"] + home_team["def"]) / 100000
    if home_team["minute_chance"] <= 0:
        home_team["minute_chance"] == 0.0001
    if vis_team["minute_chance"] <= 0:
        vis_team["minute_chance"] == 0.0001


def event_randomizer(idokezd, idoveg):
    event_count = random.choices([0, 1, 2, 3, 4], [33, 36, 20, 9, 2])[0]
    random_events = random.choices(["tizenegyes",
                                "sarga",
                                "piros",
                                "vargol",
                                "nincsgol",
                                "serules",
                                "baleset",
                                "szurkolo",
                                "semmi"], [23, 26, 13, 7, 9, 6, 7, 5, 4], k=event_count)
    event_list = {}
    for event in random_events:
        event_list[random.randrange(idokezd, idoveg)] = event
    return event_list


def play_event(event, team):
    def print_dots(szam):
        dots = ""
        for i in range(szam):
            dots += "."
            print(dots)
            time.sleep(0.25)
    is_var = random.choice([True, False])
            
    match event:
        case "tizenegyes":
            print(team["name"], "tizenegyes!")
            if STAT_ON:
                print(team["base_chance"])
            time.sleep(2)
            print_dots(3)
            team["shot"] += 1
            if random.randrange(1, 1000) < team["base_chance"]:
                team["goal"] += 1
                print(team["name"], "GÓÓÓL!")
            else:
                print(team["name"], "sikertelen lövés")
        case "sarga" | "piros":
            if is_var:
                print("[!] Incidens kivizsgálása")
                time.sleep(2)
                print_dots(5)
                if event == "sarga":
                    print(f"VAR: {team['name']} sárga lap!")
                    team["minute_chance"] -= 0.001
                elif event == "piros":
                    print(f"VAR: {team['name']} piros lap!")
                    team["minute_chance"] -= 0.01
            else:
                if event == "sarga":
                    print(f"{team['name']} sárga lap!")
                    team["minute_chance"] -= 0.002
                elif event == "piros":
                    print(f"{team['name']} piros lap!")
                    team["minute_chance"] -= 0.015
        case "vargol":
            if is_var:
                print("[!] GLT ellenőrzés")
            else:
                print("[!] Góleset kivizsgálása")
            time.sleep(2)
            print_dots(5)
            team["shot"] += 1
            team["goal"] += 1
            print(f"VAR: {team['name']} GÓÓÓL!")
        case "nincsgol":
            team["shot"] += 1
            print(f"{team['name']} GÓÓÓL!")
            time.sleep(1)
            if is_var:
                print("[!] GLT ellenőrzés")
            else:
                print("[!] Góleset kivizsgálása")
            time.sleep(2)
            print_dots(5)
            if is_var:
                indok = "nincs gól"
            else:
                indok = random.choice(["les", "szabálytalanság", "nincs gól"])
            print(f"VAR: {team['name']} {indok}!")
        case "serules":
            print(team["name"], "sérülés!")
            team["minute_chance"] -= 0.009
            time.sleep(2)
            print("A sérült játékost elszállítják")
            print_dots(5)
        case "baleset":
            print("Akadály került a pályára!")
            time.sleep(2)
            print("A személyzet elintézi a problémát")
            print_dots(3)
        case "szurkolo":
            print("Egy szurkoló beszaladt a pályára!")
            team["minute_chance"] += 0.001
            time.sleep(2)
            print("A biztonsági őrök elszállítják a drukkert")
            print_dots(3)
        case "semmi":
            print("[!] Incidens kivizsgálása")
            time.sleep(2)
            print_dots(5)
            team["minute_chance"] += 0.002
            print(f"VAR: {team['name']} nincs szabálytalanság!")
    time.sleep(0.5)
    return team


def match90(home_team, vis_team, print_pause):
    first_half_added_mins = random.choices([0, 1, 2, 3, 4, 5], [9, 21, 32, 17, 14, 7])[0]
    sec_half_added_mins = random.choices([0, 1, 2, 3, 4, 5, 6], [6, 16, 21, 27, 17, 9, 4])[0]
    events90 = event_randomizer(5, 90)
    if len(events90) == 1:
        sec_half_added_mins += 2
    if len(events90) >= 2:
        sec_half_added_mins += 2
    if len(events90) >= 3:
        sec_half_added_mins += 3
    print("Szimuláció indul!")
    time.sleep(2)
    print("A pályát előkészítik...")
    time.sleep(1)
    print("A játékosok bemelegítenek...")
    time.sleep(1)
    print("Kezdőrúgás!")
    time.sleep(print_pause)
    for i in range(1, 91):
        print("Perc:", i)
        shoot_goal(home_team, vis_team, False)
        if i in events90.keys():
            play_event(events90[i], random.choice([home_team, vis_team]))
            if STAT_ON:
                print_chances("-", home_team)
                print_chances("-", vis_team)
        time.sleep(print_pause)
        if i == 45:
            for j in range(first_half_added_mins):
                print("Perc: 45 +", j + 1)
                shoot_goal(home_team, vis_team, True)
                time.sleep(print_pause)
            print("Félidő!")
            time.sleep(2)
        if i == 90:
            for j in range(sec_half_added_mins):
                print("Perc: 90 +", j + 1)
                shoot_goal(home_team, vis_team, True)
                time.sleep(print_pause)
            print("Meccs vége!")
            time.sleep(print_pause)
    print("-----")
    print(f"Végeredmény: {home_team['name']} - {vis_team['name']} : {home_team['goal']} - {vis_team['goal']}, lövések száma: {home_team['shot']} - {vis_team['shot']}")
    return winner(home_team, vis_team)


def match120(home_team, vis_team, print_pause):
    is_continue = ""
    while is_continue not in ["igen", "nem", "i", "n"]:
        is_continue = input("Hosszabbítás? igen/nem: ").lower()
        if is_continue == "nem" or is_continue == "n":
            print("Döntetlen! Gratulálunk mindkét csapatnak.")
            return {}
    print("-----")

    extra_time_first_half_added_mins = random.choices([0, 1, 2, 3], [26, 38, 22, 14])[0]
    extra_time_sec_half_added_mins = random.choices([0, 1, 2, 3, 4], [21, 31, 25, 14, 9])[0]
    events120 = event_randomizer(95, 120)
    
    for i in range(91, 121):
        print("Perc:", i)
        shoot_goal(home_team, vis_team, False)
        if i in events120.keys():
            play_event(events120[i], random.choice([home_team, vis_team]))
            if STAT_ON:
                print_chances("-", home_team)
                print_chances("-", vis_team)
        time.sleep(print_pause)
        if i == 105:
            for j in range(extra_time_first_half_added_mins):
                print("Perc: 105 +", j + 1)
                shoot_goal(home_team, vis_team, True)
                time.sleep(print_pause)
            print("H. Félidő!")
            time.sleep(2)
        if i == 120:
            for j in range(extra_time_sec_half_added_mins):
                print("Perc: 120 +", j + 1)
                shoot_goal(home_team, vis_team, True)
                time.sleep(print_pause)
            print("Hosszabbítás vége!")
            time.sleep(print_pause)
    print("-----")
    print(f"Hosszabbítás után: {home_team['name']} - {vis_team['name']} : {home_team['goal']} - {vis_team['goal']}, lövések száma: {home_team['shot']} - {vis_team['shot']}")
    return winner(home_team, vis_team)


def penalties(home_team, vis_team, print_pause):
    is_continue = ""
    while is_continue not in ["igen", "nem", "i", "n"]:
        is_continue = input("Folytatás? igen/nem: ").lower()
        if is_continue == "nem" or is_continue == "n":
            print("Döntetlen! Gratulálunk mindkét csapatnak.")
            return {}
    print("-----")
    coin = random.choice(["F","I"])
    print(f"{home_team['name']} - F, {vis_team['name']} - I, érme - {coin}")
    if coin == "F":
        pen_order = [home_team, vis_team]
    else:
        pen_order = [vis_team, home_team]
    home_team["pen_shot"], vis_team["pen_shot"] = 1, 1
    home_team["pens_string"], vis_team["pens_string"] = "", ""
    time.sleep(2)
    for _ in range(5):
        for shoot in pen_order:
            shoot_pen(shoot, 7)
            shoot["pen_shot"] += 1
            time.sleep(print_pause / 2)
        time.sleep(print_pause)
    print("-----")
    print(f"Büntetők után: {home_team['name']} - {vis_team['name']} : {home_team['goal']} - {vis_team['goal']}, lövések: {home_team['pens_string']} - {vis_team['pens_string']}")
    if home_team["goal"] == vis_team["goal"]:
        print("Még nem dőlt el!")
        print("-----")
        time.sleep(2)
        while(home_team["goal"] == vis_team["goal"]):
            for shoot in pen_order:
                shoot_pen(shoot, 7)
                shoot["pen_shot"] += 1
                time.sleep(print_pause / 2)
            time.sleep(print_pause)
        return winner(home_team, vis_team)
    else:
        return winner(home_team, vis_team)


def shoot_pen(team, chance_multiplier):
    print(f"{team['name']} {team['pen_shot']}. büntető lövése:")
    randomizer = random.random()
    if STAT_ON:
        print_chances(randomizer, team)
    if team["minute_chance"] <= 0:
        team["minute_chance"] = 0.0005
    if randomizer < (team["minute_chance"] * chance_multiplier):
        print("GÓL!")
        team["goal"] += 1
        team["pens_string"] += "✓"
    else:
        print("sikertelen")
        team["pens_string"] += "✗"
    return team


def winner(home_team, vis_team):
    if home_team["goal"] > vis_team["goal"]:
        print(f"Győztes: {home_team['name']} Gratulálunk!")
        return home_team
    elif home_team["goal"] < vis_team["goal"]:
        print(f"Győztes: {vis_team['name']} Gratulálunk!")
        return vis_team
    else:
        return None


def main():
    home = {"side": "home"}
    visitor = {"side": "visitor"}

    print("-----")
    while len(home) != 5:
        input_team(home)
    print_team(home)
    print("-----")
    while len(visitor) != 5:
        input_team(visitor)
    print_team(visitor)
    print("-----")

    calc_base_chance(home, visitor)

    formation(home)
    print("-----")
    formation(visitor)
    print("-----")

    calc_minute_chance(home, visitor)

    stat = ""
    while stat not in ["igen", "nem", "i", "n"]:
        stat = input("Esélyek mutatása? igen/nem: ").lower()
    if stat == "igen" or stat == "i":
        global STAT_ON
        STAT_ON = True
        print(f"Kezdő esély: H: {home['base_chance']}, V: {visitor['base_chance']}")
        print_chances("kezdés", home)
        print_chances("kezdés", visitor)
    print("-----")

    match = match90(home, visitor, 0.5)
    if match == None:
        extra_time = match120(home, visitor, 0.5)
        if extra_time == None:
            pens = penalties(home, visitor, 0.75)
            if pens == None:
                print("Nincs győztes!")
                time.sleep(1)
                raise ValueError("Hibás adat?")
    input()

try:
    main()
except KeyboardInterrupt:
    print("Meccs megszakítva. Nyomj entert a kilépéshez.")
    input()
