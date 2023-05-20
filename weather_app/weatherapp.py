### Programmi ülessane on otsida linna kohta praegusel hetkel ilma kohta infot, läbi google search engine.
### kirjutasime, sest seda on mugavam kasutada kui igakord avada chrome ning sealt eraldi otsingusse kirjutada ilmateate lehed.

from lib2to3.pgen2 import driver
from tkinter import N
from requests_html import HTMLSession
from datetime import date
import calendar
from bs4 import BeautifulSoup as bs
import urllib
from easygui import *
import PySimpleGUI as sg


#dictionarid
nparvutamine = {"Esmaspäev": "0", "Teisipäev": "1", "Kolmapäev": "2", "Neljapäev": "3", "Reede": "4", "Laeupäev": "5", "Pühapäev": "6"} #dictionary nädalapäevadele pannakse dictionarys võrduma numbritega
nparvutamine2 = {"0": "Esmaspäev", "1": "Teisipäev", "2": "Kolmapäev", "3": "Neljapäev", "4": "Reede", "5": "Laeupäev", "6": "Pühapäev"} #dictionary numbrid pannakse dictionarys võrduma nädalapäevadega
np = {"Monday": "Esmaspäev", "Tuesday": "Teisipäev", "Wednesday": "Kolmapäev", "Thursday": "Neljapäev", "Friday": "Reede", "Saturday": "Laupäev", "Sunday": "Pühapäev"} #inglisekeelsed nädalapäevad pannakse võrduma eestikeelsetega

#nädala päevade saamine 
tana = date.today()                         #kuupäeva saamine
tana1 = calendar.day_name[tana.weekday()]   # nädalapäeva saamine mis antakse inglise keeles
paev = (np[tana1])                          # saadyd päev inglise keeles muudetakse üle eesti keelseks
paev = (nparvutamine[paev])                 # saadud päev muudetakse eesti keelsest numbriks

hommme=[]       

def homme(arv):                             # kood arvutab järgmist päeva.
    arv = int(arv) + 1                      # päev tehakse arvuks kasutades üleval olevat dict ning listakse arvule +1
    if arv >= 7:                            # kui arv on suurem kui 6, muutub see 0-ks
        arv = 0                             # ^^^^^^
    arv = str(arv)                          # saadud number tehakse stringiks
    arv = (nparvutamine2[arv])              # saadud number asendatakse dict päevaga
    hommme.append(arv)                      # saadud päev listakse listi

homme(paev)                 

headline = "Weatherapp"
nimi = enterbox("Sisestage linn mille kohta te infot soovite.", title = headline) #kasti sisestatud linna nime võtab väärtusena nimesse

query = nimi
lehekulg = f"http://www.google.com/search?q=weather+{query}" #query asendatakse ülevalpool kasti antud nimi inputi ning see asendatakse leheküljega.

s= HTMLSession()
r = s.get(lehekulg, headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0"}) #avab lehekülje 

#esimenepaev
olustik1=(r.html.find('span#wob_dc', first=True).text)          #võtab interneti lehelt olustiku andmed
kraad1= (r.html.find('span#wob_tm', first=True).text + " °C")   #võtab interneti lehelt tempteratuuri andmed
tuul1=str(r.html.find('span#wob_ws', first=True).text)     #võtab interneti lehelt tuulekiiruse andmed
sademed1=str(r.html.find('span#wob_pp', first=True).text)     #võtab interneti lehelt sademete  andmed
niiskus1=str(r.html.find('span#wob_hm', first=True).text)     #võtab interneti lehelt niiskus andmed

#homnepäev
for hommmme in hommme:      
    hommmme = hommmme   #et saada järjendist välja homne päev stringina

kraad2=(r.html.find('div.gNCp2e', first=True).find('span.wob_t', first=True).text)#võtab järgmise päeva temperatuuri

#variable
praegu = ("Täna on " + np[tana1] + "\n" + "\n" ) # tänane kuupäev
praegu1 = (" Õues on " + olustik1 + ". \n " + "Väljas on " + kraad1 + ". \n " + "Tuulekiirus on " + tuul1 + ". \n " +  "Sademed: " + sademed1 + ". \n " + "Õhuniiskus: "  + niiskus1 + ". \n " + "\n" ) # kõik andmed kokku tänase päeva kohta
homnepaev= ("Homme on "+ hommmme + " ning siis on " + kraad2 + " °C" + ".\n" + "\n" ) #homse päeva temperatuuri andmed ning homne päev

msgbox(praegu + praegu1 + homnepaev, title = headline) #UI output