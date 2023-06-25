import random
import time

print("Szim Foci Szimulátor \"Legacy Edition\" (2020-2023)")
print("Elavult verzió! Legjobb élményért használd a legfrissebb változatot.\n")

hazai=input("Hazai csapat: ")
vendeg=input("Vendég csapat: ")

print("-----")
print(hazai,"támadás pontok")
hazatk=int(input("min. 1 max. 99: "))
if hazatk>99:
    hazatk=99
if hazatk<1:
    hazatk=1
print(hazai,"középpálya pontok")
hazmid=int(input("min. 1 max. 99: "))
if hazmid>99:
    hazmid=99
if hazmid<1:
    hazmid=1
print(hazai,"védelem pontok")
hazdef=int(input("min. 1 max. 99: "))
if hazdef>99:
    hazdef=99
if hazdef<1:
    hazdef=1
print("-----")
print(vendeg,"támadás pontok")
venatk=int(input("min. 1 max. 99: "))
if venatk>99:
    venatk=99
if venatk<1:
    venatk=1
print(vendeg,"középpálya pontok")
venmid=int(input("min. 1 max. 99: "))
if venmid>99:
    venmid=99
if venmid<1:
    venmid=1
print(vendeg,"védelem pontok")
vendef=int(input("min. 1 max. 99: "))
if vendef>99:
    vendef=99
if vendef<1:
    vendef=1
print("-----")



print("Felállás input például: \nsor: 4 - ahol 4 darab sorba rendeződnek a játékosok, kapust leszámítva;\n1. sor: 3 - ahol a kapustól nézve első sorban ennyi játékos van")
print(hazai,"felállás sorainak száma")
hazsor=int(input("sorok száma (3, 4, 5): "))
if hazsor!=3 and hazsor!=4 and hazsor!=5:
    print("\nHiba, csak 3 ,4 vagy 5 sor lehet!")
print(vendeg,"felállás sorainak száma")
vensor=int(input("sorok száma (3, 4, 5): "))
if vensor!=3 and vensor!=4 and vensor!=5:
    print("\nHiba, csak 3, 4 vagy 5 sor lehet!")
hazfel=[]
venfel=[]



print("-----")
for i in range(hazsor):
    print(hazai,i+1,"sor")
    hssor=int(input("játékosok száma: "))
    hazfel.append(hssor)
if hazsor==3:
    print("\nEllenőrzés:",hazai,"\ntámadás:",hazatk,"\nközéppályán:",hazmid,"\nvédelem:",hazdef,"\ncsapat felállása:",hazfel[0],"-",hazfel[1],"-",hazfel[2])
if hazsor==4:
    print("\nEllenőrzés:",hazai,"\ntámadás:",hazatk,"\nközéppályán:",hazmid,"\nvédelem:",hazdef,"\ncsapat felállása:",hazfel[0],"-",hazfel[1],"-",hazfel[2],"-",hazfel[3])
if hazsor==5:
    print("\nEllenőrzés:",hazai,"\ntámadás:",hazatk,"\nközéppályán:",hazmid,"\nvédelem:",hazdef,"\ncsapat felállása:",hazfel[0],"-",hazfel[1],"-",hazfel[2],"-",hazfel[3],"-",hazfel[4])
if sum(hazfel)!=10:
    print("\nHiba, a felállás nem 10 emberből áll!")
print("-----")
for i in range(vensor):
    print(vendeg,i+1,"sor")
    vssor=int(input("játékosok száma: "))
    venfel.append(vssor)
if vensor==3:
    print("\nEllenőrzés:",vendeg,"\ntámadás:",venatk,"\nközéppályán:",venmid,"\nvédelem:",vendef,"\ncsapat felállása:",venfel[0],"-",venfel[1],"-",venfel[2])
if vensor==4:
    print("\nEllenőrzés:",vendeg,"\ntámadás:",venatk,"\nközéppályán:",venmid,"\nvédelem:",vendef,"\ncsapat felállása:",venfel[0],"-",venfel[1],"-",venfel[2],"-",venfel[3])
if vensor==5:
    print("\nEllenőrzés:",vendeg,"\ntámadás:",venatk,"\nközéppályán:",venmid,"\nvédelem:",vendef,"\ncsapat felállása:",venfel[0],"-",venfel[1],"-",venfel[2],"-",venfel[3],"-",venfel[4])
if sum(venfel)!=10:
    print("\nHiba, a felállás nem 10 emberből áll!")



print("-----")
hazesely=500
hazszer=6/7+random.randrange(1,4)/7
venesely=500
venszer=6/7+random.randrange(1,4)/7
hazlov=0
hazgol=0
venlov=0
vengol=0

hazesely=hazesely+(hazatk*hazszer-vendef+hazmid-venmid+hazdef-venatk*venszer)
venesely=venesely+(venatk*venszer-hazdef+venmid-hazmid+vendef-hazatk*hazszer)
#print(hazesely,venesely,hazszer,venszer)



if hazsor==3:
    if hazfel[0]==2 and hazfel[1]==3 and hazfel[2]==5:
        hazatk+=4
        hazmid+=2
        hazdef+=7
    if hazfel[0]==3 and hazfel[1]==4 and hazfel[2]==3:
        hazatk+=11
        hazmid+=7
        hazdef-=5
    if hazfel[0]==3 and hazfel[1]==5 and hazfel[2]==2:
        hazatk+=8
        hazmid+=4
        hazdef+=1
    if hazfel[0]==3 and hazfel[1]==6 and hazfel[2]==1:
        hazatk+=0
        hazmid+=11
        hazdef+=2
    if hazfel[0]==4 and hazfel[1]==3 and hazfel[2]==3:
        hazatk+=6
        hazmid+=7
        hazdef+=0
    if hazfel[0]==4 and hazfel[1]==4 and hazfel[2]==2:
        hazatk+=7
        hazmid+=7
        hazdef-=1
    if hazfel[0]==4 and hazfel[1]==5 and hazfel[2]==1:
        hazatk+=2
        hazmid+=9
        hazdef+=2
    if hazfel[0]==4 and hazfel[1]==6 and hazfel[2]==0:
        hazatk+=5
        hazmid+=12
        hazdef-=4
    if hazfel[0]==5 and hazfel[1]==3 and hazfel[2]==2:
        hazatk-=2
        hazmid+=4
        hazdef+=11
    if hazfel[0]==5 and hazfel[1]==4 and hazfel[2]==1:
        hazatk-=5
        hazmid+=6
        hazdef+=12
    else:
        hazatk+=4
        hazmid+=5
        hazdef+=4
if hazsor==4:
    if hazfel[0]==3 and hazfel[1]==3 and hazfel[2]==3 and hazfel[3]==1:
        hazatk+=3
        hazmid+=13
        hazdef-=3
    if hazfel[0]==3 and hazfel[1]==4 and hazfel[2]==1 and hazfel[3]==2:
        hazatk+=12
        hazmid+=3
        hazdef-=2
    if hazfel[0]==3 and hazfel[1]==4 and hazfel[2]==2 and hazfel[3]==1:
        hazatk+=13
        hazmid+=5
        hazdef-=5
    if hazfel[0]==4 and hazfel[1]==1 and hazfel[2]==4 and hazfel[3]==1:
        hazatk-=4
        hazmid+=8
        hazdef+=9
    if hazfel[0]==4 and hazfel[1]==2 and hazfel[2]==2 and hazfel[3]==2:
        hazatk+=4
        hazmid+=4
        hazdef+=5
    if hazfel[0]==4 and hazfel[1]==2 and hazfel[2]==3 and hazfel[3]==1:
        hazatk+=7
        hazmid+=1
        hazdef+=5
    if hazfel[0]==4 and hazfel[1]==3 and hazfel[2]==1 and hazfel[3]==2:
        hazatk+=3
        hazmid+=1
        hazdef+=9
    if hazfel[0]==4 and hazfel[1]==4 and hazfel[2]==1 and hazfel[3]==1:
        hazatk+=2
        hazmid+=6
        hazdef+=5
    if hazfel[0]==5 and hazfel[1]==2 and hazfel[2]==1 and hazfel[3]==2:
        hazatk-=4
        hazmid+=4
        hazdef+=13
    if hazfel[0]==5 and hazfel[1]==2 and hazfel[2]==2 and hazfel[3]==1:
        hazatk+=6
        hazmid-=1
        hazdef+=8
    else:
        hazatk+=3
        hazmid+=4
        hazdef+=6
if hazsor==5:
    hazatk+=4
    hazmid+=7
    hazdef+=2
        
if vensor==3:
    if venfel[0]==2 and venfel[1]==3 and venfel[2]==5:
        venatk+=4
        venmid+=2
        vendef+=7
    if venfel[0]==3 and venfel[1]==4 and venfel[2]==3:
        venatk+=11
        venmid+=7
        vendef-=5
    if venfel[0]==3 and venfel[1]==5 and venfel[2]==2:
        venatk+=8
        venmid+=4
        vendef+=1
    if venfel[0]==3 and venfel[1]==6 and venfel[2]==1:
        venatk+=0
        venmid+=11
        vendef+=2
    if venfel[0]==4 and venfel[1]==3 and venfel[2]==3:
        venatk+=6
        venmid+=7
        vendef+=0
    if venfel[0]==4 and venfel[1]==4 and venfel[2]==2:
        venatk+=7
        venmid+=7
        vendef-=1
    if venfel[0]==4 and venfel[1]==5 and venfel[2]==1:
        venatk+=2
        venmid+=9
        vendef+=2
    if venfel[0]==4 and venfel[1]==6 and venfel[2]==0:
        venatk+=5
        venmid+=12
        vendef-=4
    if venfel[0]==5 and venfel[1]==3 and venfel[2]==2:
        venatk-=2
        venmid+=4
        vendef+=11
    if venfel[0]==5 and venfel[1]==4 and venfel[2]==1:
        venatk-=5
        venmid+=6
        vendef+=12
    else:
        venatk+=4
        venmid+=5
        vendef+=4
if vensor==4:
    if venfel[0]==3 and venfel[1]==3 and venfel[2]==3 and venfel[3]==1:
        venatk+=3
        venmid+=13
        vendef-=3
    if venfel[0]==3 and venfel[1]==4 and venfel[2]==1 and venfel[3]==2:
        venatk+=12
        venmid+=3
        vendef-=2
    if venfel[0]==3 and venfel[1]==4 and venfel[2]==2 and venfel[3]==1:
        venatk+=13
        venmid+=5
        vendef-=5
    if venfel[0]==4 and venfel[1]==1 and venfel[2]==4 and venfel[3]==1:
        venatk-=4
        venmid+=8
        vendef+=9
    if venfel[0]==4 and venfel[1]==2 and venfel[2]==2 and venfel[3]==2:
        venatk+=4
        venmid+=4
        vendef+=5
    if venfel[0]==4 and venfel[1]==2 and venfel[2]==3 and venfel[3]==1:
        venatk+=7
        venmid+=1
        vendef+=5
    if venfel[0]==4 and venfel[1]==3 and venfel[2]==1 and venfel[3]==2:
        venatk+=3
        venmid+=1
        vendef+=9
    if venfel[0]==4 and venfel[1]==4 and venfel[2]==1 and venfel[3]==1:
        venatk+=2
        venmid+=6
        vendef+=5
    if venfel[0]==5 and venfel[1]==2 and venfel[2]==1 and venfel[3]==2:
        venatk-=4
        venmid+=4
        vendef+=13
    if venfel[0]==5 and venfel[1]==2 and venfel[2]==2 and venfel[3]==1:
        venatk+=6
        venmid-=1
        vendef+=8
    else:
        venatk+=3
        venmid+=4
        vendef+=6
if vensor==5:
    venatk+=4
    venmid+=7
    vendef+=2



stat=input("Stat? igen/nem: ")
def stat_print(van, rand, hesely, vesely):
    if van=="igen":
        print(rand, hesely, vesely)



hazszer=6/10+random.randrange(1,3)/10
venszer=6/10+random.randrange(1,3)/10
hazesely=hazesely+(hazatk*hazszer-vendef+hazmid-venmid+hazdef-venatk*venszer)/3
venesely=venesely+(venatk*venszer-hazdef+venmid-hazmid+vendef-hazatk*hazszer)/3
if stat=="igen":
    print(hazesely,venesely,hazszer,venszer)
randomizalo=0.1
hazpercesely=((hazesely+hazszer)/1000)*randomizalo
venpercesely=((venesely+venszer)/1000)*randomizalo
stat_print(stat, randomizalo, hazpercesely, venpercesely)



print("Szimuláció indul!")
time.sleep(1.5)
print("A pályát előkészítik...")
time.sleep(1)
print("A játékosok bemelegítenek...")
time.sleep(1)
print("Indul a kezdőrúgás!")
time.sleep(1)

if hazpercesely-venpercesely>=0.02:
    hazpercesely+=0.015
if venpercesely-hazpercesely>=0.02:
    venpercesely+=0.015
for i in range(90):
    print("Perc:",i+1)
    randomizalo=random.random()
    if randomizalo<(hazpercesely):
        hazlov+=1
        stat_print(stat, randomizalo, hazpercesely, venpercesely)
        randomizalo=random.random()
        if randomizalo>(hazpercesely*(2.3+hazatk/100-vendef/100)):
            print(hazai,"sikertelen lövés")
        if randomizalo<(hazpercesely*(2.3+hazatk/100-vendef/100)):
            hazgol+=1
            print(hazai,"GÓÓÓL!")
            hazpercesely=hazpercesely-0.007
    stat_print(stat, randomizalo, hazpercesely, venpercesely)
    hazpercesely+=0.002
    randomizalo=random.random()
    if randomizalo<(venpercesely):
        venlov+=1
        stat_print(stat, randomizalo, hazpercesely, venpercesely)
        randomizalo=random.random()
        if randomizalo>(venpercesely*(2.3+venatk/100-hazdef/100)):
            print(vendeg,"sikertelen lövés")
        if randomizalo<(venpercesely*(2.3+venatk/100-hazdef/100)):
            vengol+=1
            print(vendeg,"GÓÓÓL!")
            venpercesely=venpercesely-0.009
    stat_print(stat, randomizalo, hazpercesely, venpercesely)
    venpercesely+=0.002
    randomizalo=random.random()
    hazpercesely=hazpercesely-(venatk+venmid+vendef)/100000
    venpercesely=venpercesely-(hazatk+hazmid+hazdef)/100000
    time.sleep(0.5)
    if i+1==45:
        for j in range(random.choice([0,0,0,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,5])):
            print("Perc: 45 +",j+1)
            randomizalo=random.random()
            if randomizalo<(hazpercesely*1.1):
                hazlov+=1
                randomizalo=random.random()
                if randomizalo>(hazpercesely*(1.1+hazatk/100-vendef/100)):
                    print(hazai,"sikertelen lövés")
                if randomizalo<(hazpercesely*(1.1+hazatk/100-vendef/100)):
                    hazgol+=1
                    print(hazai,"GÓÓÓL!")
                    hazpercesely=hazpercesely-0.017
            stat_print(stat, randomizalo, hazpercesely, venpercesely)
            hazpercesely+=0.005
            randomizalo=random.random()
            if randomizalo<(venpercesely*1.1):
                venlov+=1
                randomizalo=random.random()
                if randomizalo>(venpercesely*(1.1+venatk/100-hazdef/100)):
                    print(vendeg,"sikertelen lövés")
                if randomizalo<(venpercesely*(1.1+venatk/100-hazdef/100)):
                    vengol+=1
                    print(vendeg,"GÓÓÓL!")
                    venpercesely=venpercesely-0.019
            stat_print(stat, randomizalo, hazpercesely, venpercesely)
            venpercesely+=0.005
            time.sleep(0.5)
        print("Félidő!")
        time.sleep(2)
    if i+1==90:
        for j in range(random.choice([0,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,6])):
            print("Perc: 90 +",j+1)
            randomizalo=random.random()
            if randomizalo<(hazpercesely*1.05):
                hazlov+=1
                randomizalo=random.random()
                if randomizalo>(hazpercesely*(1.2+hazatk/100-vendef/100)):
                    print(hazai,"sikertelen lövés")
                if randomizalo<(hazpercesely*(1.2+hazatk/100-vendef/100)):
                    hazgol+=1
                    print(hazai,"GÓÓÓL!")
                    hazpercesely=hazpercesely-0.02
            stat_print(stat, randomizalo, hazpercesely, venpercesely)
            hazpercesely+=0.005
            randomizalo=random.random()
            if randomizalo<(venpercesely*1.05):
                venlov+=1
                randomizalo=random.random()
                if randomizalo>(venpercesely*(1.2+venatk/100-hazdef/100)):
                    print(vendeg,"sikertelen lövés")
                if randomizalo<(venpercesely*(1.2+venatk/100-hazdef/100)):
                    vengol+=1
                    print(vendeg,"GÓÓÓL!")
                    venpercesely=venpercesely-0.02
            stat_print(stat, randomizalo, hazpercesely, venpercesely)
            venpercesely+=0.005
            time.sleep(0.5)
    if hazlov>=10:
        hazpercesely-=0.002
    if venlov>=10:
        venpercesely-=0.002
print("-----")
print("Végeredmény:",hazai,"-",vendeg,":",hazgol,"-",vengol,"lövések száma:",hazlov,"-",venlov)
if hazgol>vengol:
    print("Győztes:",hazai,"Gratulálunk!")
if hazgol<vengol:
    print("Győztes:",vendeg,"Gratulálunk!")



if hazgol==vengol:
    print("-----")
    hossz=input("Hosszabbítás? igen/nem: ")
    if hossz=="igen":
        for i in range(30):
            print("Perc:",i+91)
            randomizalo=random.random()
            #print(randomizalo)
            if randomizalo<(hazpercesely*1.5):
                hazlov+=1
                randomizalo=random.random()
                if randomizalo>(hazpercesely*(1.8+hazatk/100-vendef/100)):
                    print(hazai,"sikertelen lövés")
                if randomizalo<(hazpercesely*(1.8+hazatk/100-vendef/100)):
                    print(hazai,"GÓÓÓL!")
                    hazgol+=1
                    hazpercesely=hazpercesely-0.05
            stat_print(stat, randomizalo, hazpercesely, venpercesely)
            if randomizalo<(venpercesely*1.5):
                venlov+=1
                randomizalo=random.random()
                if randomizalo>(venpercesely*(1.8+venatk/100-hazdef/100)):
                    print(vendeg,"sikertelen lövés")
                if randomizalo<(venpercesely*(1.8+venatk/100-hazdef/100)):
                    print(vendeg,"GÓÓÓL!")
                    vengol+=1
                    venpercesely=venpercesely-0.05
            stat_print(stat, randomizalo, hazpercesely, venpercesely)
            time.sleep(0.5)
            if (i+91)==105:
                for j in range(random.randrange(0,4)):
                    print("Perc: 105 +",j+1)
                    randomizalo=random.random()
                    if randomizalo<(hazpercesely*0.9):
                        hazlov+=1
                        randomizalo=random.random()
                        if randomizalo>(hazpercesely*(1.1+hazatk/100-vendef/100)):
                            print(hazai,"sikertelen lövés")
                        if randomizalo<(hazpercesely*(1.1+hazatk/100-vendef/100)):
                            hazgol+=1
                            print(hazai,"GÓÓÓL!")
                            hazpercesely=hazpercesely-0.02
                    stat_print(stat, randomizalo, hazpercesely, venpercesely)
                    hazpercesely+=0.005
                    randomizalo=random.random()
                    if randomizalo<(venpercesely*0.9):
                        venlov+=1
                        randomizalo=random.random()
                        if randomizalo>(venpercesely*(1.1+venatk/100-hazdef/100)):
                            print(vendeg,"sikertelen lövés")
                        if randomizalo<(venpercesely*(1.1+venatk/100-hazdef/100)):
                            vengol+=1
                            print(vendeg,"GÓÓÓL!")
                            venpercesely=venpercesely-0.02
                    stat_print(stat, randomizalo, hazpercesely, venpercesely)
                    venpercesely+=0.005
                    time.sleep(0.5)
                print("H. Félidő!")
                time.sleep(2)
            if (i+91)==120:
                for j in range(random.randrange(0,4)):
                    print("Perc: 120 +",j+1)
                    randomizalo=random.random()
                    if randomizalo<(hazpercesely*0.9):
                        hazlov+=1
                        randomizalo=random.random()
                        if randomizalo>(hazpercesely*(1.2+hazatk/100-vendef/100)):
                            print(hazai,"sikertelen lövés")
                        if randomizalo<(hazpercesely*(1.2+hazatk/100-vendef/100)):
                            hazgol+=1
                            print(hazai,"GÓÓÓL!")
                            hazpercesely=hazpercesely-0.02
                    stat_print(stat, randomizalo, hazpercesely, venpercesely)
                    hazpercesely+=0.005
                    randomizalo=random.random()
                    if randomizalo<(venpercesely*0.9):
                        venlov+=1
                        randomizalo=random.random()
                        if randomizalo>(venpercesely*(1.2+venatk/100-hazdef/100)):
                            print(vendeg,"sikertelen lövés")
                        if randomizalo<(venpercesely*(1.2+venatk/100-hazdef/100)):
                            vengol+=1
                            print(vendeg,"GÓÓÓL!")
                            venpercesely=venpercesely-0.02
                    stat_print(stat, randomizalo, hazpercesely, venpercesely)
                    venpercesely+=0.005
                    time.sleep(0.5)
        print("-----")
        print("Hosszabbítás után:",hazai,"-",vendeg,":",hazgol,"-",vengol,"lövések száma:",hazlov,"-",venlov)
        if hazgol>vengol:
            print("Győztes:",hazai,"Gratulálunk!")
        if hazgol<vengol:
            print("Győztes:",vendeg,"Gratulálunk!")
    if hossz=="nem":
        print("Döntetlen! Gratulálunk mindkét csapatnak.")



if hazgol==vengol and hossz=="igen":
    print("-----")
    folyt=input("Folytatás? igen/nem: ")
    if folyt=="igen":
        bunterme=random.choice(["F","I"])
        print(hazai,"- F",vendeg,"- I","érme -",bunterme)
        hazbuntlov=1
        venbuntlov=1
        hazbuntkiir=""
        venbuntkiir=""
        time.sleep(1)
        for i in range(10):
            if bunterme=="F":
                if i%2==0:
                    print(hazai,hazbuntlov,". büntető lövése:")
                    hazbuntlov+=1
                    randomizalo=random.random()
                    stat_print(stat, randomizalo, hazpercesely, venpercesely)
                    if randomizalo<(hazpercesely*7):
                        print("GÓL!")
                        hazgol+=1
                        hazbuntkiir=hazbuntkiir+"✓"
                    else:
                        print("sikertelen")
                        hazbuntkiir=hazbuntkiir+"✗"
                time.sleep(0.25)
                if i%2!=0:
                    print(vendeg,venbuntlov,". büntető lövése:")
                    venbuntlov+=1
                    randomizalo=random.random()
                    stat_print(stat, randomizalo, hazpercesely, venpercesely)
                    if randomizalo<(venpercesely*7):
                        print("GÓL!")
                        vengol+=1
                        venbuntkiir=venbuntkiir+"✓"
                    else:
                        print("sikertelen")
                        venbuntkiir=venbuntkiir+"✗"
            if bunterme=="I":
                if i%2!=0:
                    print(hazai,hazbuntlov,". büntető lövése:")
                    hazbuntlov+=1
                    randomizalo=random.random()
                    stat_print(stat, randomizalo, hazpercesely, venpercesely)
                    if randomizalo<(hazpercesely*7):
                        print("GÓL!")
                        hazgol+=1
                        hazbuntkiir=hazbuntkiir+"✓"
                    else:
                        print("sikertelen")
                        hazbuntkiir=hazbuntkiir+"✗"
                time.sleep(0.25)
                if i%2==0:
                    print(vendeg,venbuntlov,". büntető lövése:")
                    venbuntlov+=1
                    randomizalo=random.random()
                    stat_print(stat, randomizalo, hazpercesely, venpercesely)
                    if randomizalo<(venpercesely*7):
                        print("GÓL!")
                        vengol+=1
                        venbuntkiir=venbuntkiir+"✓"
                    else:
                        print("sikertelen")
                        venbuntkiir=venbuntkiir+"✗"
            time.sleep(0.5)
        print("-----")
        print("Büntetők után:",hazai,"-",vendeg,":",hazgol,"-",vengol,"lövések:",hazbuntkiir,"-",venbuntkiir)
        if hazgol>vengol:
            print("Győztes:",hazai,"Gratulálunk!")
        if hazgol<vengol:
            print("Győztes:",vendeg,"Gratulálunk!")
        if hazgol==vengol:
            print("Még nem dőlt el!")
            print("-----")
            time.sleep(2)
            while hazgol==vengol:
                for j in range(1):
                    if bunterme=="F":
                        print(hazai,hazbuntlov,". büntető lövése:")
                        hazbuntlov+=1
                        randomizalo=random.random()
                        stat_print(stat, randomizalo, hazpercesely, venpercesely)
                        if randomizalo<(hazpercesely*7):
                            print("GÓL!")
                            hazgol+=1
                            hazbuntkiir=hazbuntkiir+"✓"
                        else:
                            print("sikertelen")
                            hazbuntkiir=hazbuntkiir+"✗"
                        time.sleep(0.25)
                        print(vendeg,venbuntlov,". büntető lövése:")
                        venbuntlov+=1
                        randomizalo=random.random()
                        stat_print(stat, randomizalo, hazpercesely, venpercesely)
                        if randomizalo<(venpercesely*7):
                            print("GÓL!")
                            vengol+=1
                            venbuntkiir=venbuntkiir+"✓"
                        else:
                            print("sikertelen")
                            venbuntkiir=venbuntkiir+"✗"
                    if bunterme=="I":
                        print(hazai,hazbuntlov,". büntető lövése:")
                        hazbuntlov+=1
                        randomizalo=random.random()
                        stat_print(stat, randomizalo, hazpercesely, venpercesely)
                        if randomizalo<(hazpercesely*7):
                            print("GÓL!")
                            hazgol+=1
                            hazbuntkiir=hazbuntkiir+"✓"
                        else:
                            print("sikertelen")
                            hazbuntkiir=hazbuntkiir+"✗"
                        time.sleep(0.25)
                        print(vendeg,venbuntlov,". büntető lövése:")
                        venbuntlov+=1
                        randomizalo=random.random()
                        stat_print(stat, randomizalo, hazpercesely, venpercesely)
                        if randomizalo<(venpercesely*7):
                            print("GÓL!")
                            vengol+=1
                            venbuntkiir=venbuntkiir+"✓"
                        else:
                            print("sikertelen")
                            venbuntkiir=venbuntkiir+"✗"
                    time.sleep(0.5)
                if hazgol!=vengol:
                    break
            print("-----")
            print("Büntetők befejezése:",hazai,"-",vendeg,":",hazgol,"-",vengol,"lövések:",hazbuntkiir,"-",venbuntkiir)
            if hazgol>vengol:
                print("Győztes:",hazai,"Gratulálunk!")
            if hazgol<vengol:
                print("Győztes:",vendeg,"Gratulálunk!")
    if folyt=="nem":
        print("Döntetlen! Gratulálunk mindkét csapatnak.")
time.sleep(2)

input()
