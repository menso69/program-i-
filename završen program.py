#importujem tj. uvozim biblioteke koje ću koristit
import time, sys, random, os


#funkcija za spori output, samo se trebam pozvat na ovo
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)


        
#ovde sam naštimo sve za random pozdrav, samo ga trebam isprintat
pozdravi = ['Zdravo', 'Veliki pozdrav', 'Ćao','Dobar dan']
random_pozdrav = random.choice(pozdravi)





#ovo je malo za estetiku, nekako mi ljepše, ko na igrici, a i da pokažem šta sam naučio
print_slow("Vaše puno ime i prezime je: ")
ime=input("")
print ( random_pozdrav + ' ' + ime + '.' )






#malo zezanja sa LENGHTOM / LEN 
#nije baš nešto posebno al eto da vidite da sam i ovo načio, tj da znam
#radit sa 'len'
print_slow("\nŽelite li znati koliko slova ima u vašem imenu i prezimenu? (Da/Ne) ")
print_slow("\nOdgovor: ")
odg1 = input("")
if odg1 == 'Da' or odg1 == 'da':
        print("\n-Vaše puno ime i prezime sadrži ",len(ime)-ime.count(' '),"slova.") 
elif odg1 == 'Ne' or odg1 == 'ne':
    print_slow("Okej, nije problem, idemo dalje.")
else:
    print_slow("\nZnao sam da ćete testirat šta će izbacit ako ukucate nešto što nisam ponudio.")
    print_slow("\nNadam se da ste zadovoljni rezultatom i mojom pažnjom o detaljima.")
    print_slow("\nUglavnom, idemo dalje.")





#malo zezanja sa VREMENOM
#ni ovo nije nešto posebno al meni je drago što znam ovakve sitnice
print_slow("\n\nNaučio sam nešto sitno i oko vremena.")
print_slow("\nŽelite li znati vrijeme i datum? (Da/Ne)")
print_slow("\nOdgovor: ")
odg2 = input('')
if odg2 == 'Da' or odg2 == 'da':
   vrijeme = time.asctime( time.localtime(time.time()) )
   print ("\n-Vrijeme i datum na vašem računaru je :", vrijeme)
elif odg2 == 'Ne' or odg2 == 'ne':
    print_slow("Okej, nije problem, idemo dalje.\n")
else:
    print_slow("\nZnao sam da ćete testirat šta će izbacit ako ukucate nešto što nisam ponudio.")
    print_slow("\nNadam se da ste zadovoljni rezultatom i mojom pažnjom o detaljima.")
    print_slow("\nUglavnom, idemo dalje.")



#malo zezanja sa UPPER / LOWER 
print_slow("\nTakođe, naučio sam povećat/smanjit slova u varijablama.")
print_slow("\nAko hoćete mogu Vam to demonstrirat na vašem imenu? (Da/Ne)")
print_slow("\nOdgovor: ")
odg3 = input('')
if odg3 == 'Da' or odg3 == 'da':
    povecaj = ime.upper()
    smanji = ime.lower()
    print("\n-Vaše ime velikim slovima: ",povecaj)
    print("-Vaše ime malim slovima: ",smanji)
elif odg3 == 'Ne' or odg3 == 'ne':
    print_slow("Okej, nije problem, idemo dalje.\n")
else:
    print_slow("\nZnao sam da ćete testirat šta će izbacit ako ukucate nešto što nisam ponudio.")
    print_slow("\nNadam se da ste zadovoljni rezultatom i mojom pažnjom o detaljima.")
    print_slow("\nUglavnom, idemo dalje.\n")




##################### max min broj #################
print_slow("\nŽelite li unijeti brojeve pa da vidite koji je najveći a koji najmanji? (Da/Ne)")
print_slow("\nOdgovor: ")
odg_mm = input("")

if odg_mm == "Da" or odg_mm == "da":
    a = float (input ("\nPrvi broj: "))
    b = float (input ("Drugi broj: "))
    c = float (input ("Treći broj: "))

    print("\n-Najveći od ta tri broja je ",max(a,b,c))
    print("-Najmanji od ta tri broja je ",min(a,b,c))

elif odg_mm == "Ne" or odg_mm == "ne":
    print_slow("Okej, nije problem, idemo dalje.\n")
else:
    print_slow("\nZnao sam da ćete testirat šta će izbacit ako ukucate nešto što nisam ponudio.")
    print_slow("\nNadam se da ste zadovoljni rezultatom i mojom pažnjom o detaljima.")
    print_slow("\nUglavnom, idemo dalje.\n")
##########################################################
    


############      IGRICA PISMO GLAVA    ###############

#postavka članova tj pismo i glava te postavka za izvlačenje istih
igra = ["Pismo","Glava"]
izvlacenje = random.choice(igra)

print_slow("\nŽelite li igrati pismo-glava? (Da/Ne)")
print_slow("\nOdgovor: ")
odg4 = input("")
if odg4 == "Da" or odg4 == "da":
    print_slow("\nBiraj šta ćeš, pismo ili glava? (Pismo/Glava)")
    print_slow("\nIzabrat ću: ")
    odg5 = input ("")

#ovaj dio ovde je napravljen da bude ljepše, zanimljivije, da ubacim malo
#drame, kao bacili kovanicu u zrak pa sad čekamo tri sekunde da spane
#ne znam, meni je tako ljepše, neću da bude samo početak-kraj
    print_slow("\nKovanica je bačena!\n")
    time.sleep(1)
    print("\n1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("\n-Dobili ste: ",izvlacenje)

    
    if odg5 == "Pismo" or odg5 == "pismo" and izvlacenje == (igra[0]):
        print_slow("\nČestitam, pobijedili ste.\n")
    elif odg5 == "Glava" or odg5 == "glava" and izvlacenje == (igra[1]):
        print_slow("\nČestitam, pobjedili ste.\n")
    else:
        print_slow("\nSori bro, više sreće drugi put.\n")
else:
    print_slow("Okej, nije problem, idemo dalje.\n")

#################### KRAJ IGRICE, ZAVRŠENO ################################



#################### KLASE #########################


class Osoba:

    def postavka(self,ime,prezime,godine,visina,tezina,nadimak,zanimanje):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.visina = visina
        self.tezina = tezina
        self.nadimak = nadimak
        self.zanimanje = zanimanje
    
    def printaj(self):
        print("\nOsnovni podaci o toj osobi: ")
        print("\n- Ime: ",self.ime,"\n- Prezime: ",self.prezime,"\n- Nadimak: ",self.nadimak)
        print("- Visina: ",self.visina, "\n- Težina: ",self.tezina, "\n- Zanimanje:", self.zanimanje)

Mirela=Osoba()
Mirela.postavka("Mirela","Avdić",69,185,69,"Mensina djevojka","Profesorica")

Menso=Osoba()
Menso.postavka("Mensur","Begović",17,189,75,"Menso","Šuga (smara sve oko sebe)")

Mcc=Osoba()
Mcc.postavka("Adi","Mehmedćehajić",18,190,80,"Mćć / Senzor", "Rukometaš")

Sanjin=Osoba()
Sanjin.postavka("Sanjin","Milošević",19,190,70,"Retard", "Ništa ga ne zanima")

print("Ovo je da demonstriram da znam radit i s klasama.")
print("Ukratko, izaberi jednu od ponuđenih osoba i dobit ćeš osnovne informacije o njima.")
print("\nPonuđene osobe: \n- Mirela \n- Menso \n- Adi \n- Sanjin")
kl_odg = input("\nŽelim znati više o: ")


if kl_odg == "Mirela" or kl_odg == "mirela" or kl_odg == "Mireli" or kl_odg == "mireli" :
    Mirela.printaj()
    
elif kl_odg == "Menso" or kl_odg == "menso" or kl_odg == "Mensi" or kl_odg == "mensi":
        Menso.printaj()

elif kl_odg == "Adi" or kl_odg == "adi" or kl_odg == "adiju" or kl_odg =="Adiju":
        Mcc.printaj()

elif kl_odg == "Sanjin" or kl_odg == "sanjin" or kl_odg =="Sanjinu" or kl_odg =="sanjinu":
        Sanjin.printaj()
else:
    print("\nTakav objekat se ne nalazi u klasi.")

##########################################

print_slow("\nTo bi otprilike bilo to, nadam se da ste uživali i da ste zadovoljni.")
print_slow("\nZnam da nije nešto teško i komplikovano al ja smatram da je dovoljno za početak.")
print_slow("\nCilj ovog programa je da vam pokažem šta znam trenutno, mislim da sam ostvario taj cilj.")
print_slow("\nHvala Vam na svemu što ste me naučili i što znate lijepo objasnit.")
print_slow("\nZnate me nekad iznervirat nije malo, al zbog Vas sam i dobio želju za programiranjem.")
print_slow("\nUglavnom, dobra ste profesorica (i psihički i fizički khmm khmmmm).")
print_slow("\nHVALA Vam na svemu što ste me do sad naučili, lijep pozdrav i ugodan ostatak dana :D")

###########################################

#
#
#
#
#
#
#
#           ovo je da ne vidite šta piše gore, nemojte čitat odma, pročitajte u programu kad pokrenete
#
#
#
#
#
#
#

        


    
    




    




