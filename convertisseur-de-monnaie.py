from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError

c = CurrencyCodes()
c.get_symbol('GBP')
ratio = CurrencyRates()
taux_de_conversion = {}

#===================== zone de test ================================

"""
print(ratio.get_rates("USD"))
print (CurrencyRates().convert("USD","EUR",10))
taux_eur_usd = ratio.get_rate ("EUR", "USD")


print(taux_eur_usd)

total = ratio.convert('BTC', 'EUR', 10)  # convert('USD', 'INR', 10) devise de base vers la devise target
print(total)
674.73
#total2 = CurrencyRates.convert('USD', 'INR', 10)
"""

#======================= fin de zone =========================================
#======================= Zone definition de fonction =========================================

def liste_devises():                        # Afficher la liste des codes de devise initial
    
    codes_iso_devises = [
        "EUR", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON",
        "MYR", "SEK", "SGD", "HKD", "AUD", "CHF", "KRW", "CNY", "TRY", "HRK",
        "NZD", "THB","USD", "NOK", "RUB", "INR", "MXN", "CZK", "BRL", "PLN", "PHP","ZAR"
    ]
    print (codes_iso_devises)

def historique():                           # Définie la fonction historique qui écrie le resultat de la fonction convertisseur
 
    with open("historique.txt","a", encoding="utf-8") as fichier:
        fichier.write(f"Pour {quantité} {name_base} vous aurez =======> {round(resultat,2)} {name_target}" + "\n")

def lire_historique():
    
    try:                      # Définie la fonction qui permet de lire le fichier historique.txt et de l'afficher dans le terminal
        with open("historique.txt", "r", encoding="utf-8") as fichier:
	        print (fichier.read())
    except FileNotFoundError:
        print("Aucun historique trouvé.")
    
def choix_utilisateur_historique():         # Définie la fonction qui demande a l'utilisateur si il veux ou non afficher l'historique

    while True:
        
        reponse = input("Voulez-vous consulter l'historique ? (y/n): ").lower()
        if reponse == 'y':
            print("Voici l'historique !")
            lire_historique()
            break
        elif reponse == 'n':
            print("Continuons...")
            break
            
        else:
            print("Réponse non valide. Veuillez entrer 'y' pour oui ou 'n' pour non.")

    return

def quitter():                              # Définie la fonction qui permet de quitter le programme
    
    while True:
        
        reponse = input("Voulez-vous quitter ? (y/n): ").lower()
        if reponse == 'y':
            print("Au revoir!")
            exit()
        elif reponse == 'n':
            print("Continuons...")
            break
        else:
            print("Réponse non valide. Veuillez entrer 'y' pour oui ou 'n' pour non.")
    return

def choix_utilisateur_ajout_Devise():         # Définie la fonction qui demande a l'utilisateur si il veux ou non ajouter une devise

    while True:
        
        reponse = input("Voulez-vous ajouter une devise ? (y/n): ").lower()
        if reponse == 'y':
            nom = input("Veuillez entrer le nom de la devise: ")
            code_iso = input("Veuillez entrer le code iso: ").upper()
            quantité_en_usd = input("Veuillez entrer le taux conversion: ")
            ajouter_devise(nom, code_iso, quantité_en_usd)
            break
        elif reponse == 'n':
            print("Continuons...")
            break
            
        else:
            print("Réponse non valide. Veuillez entrer 'y' pour oui ou 'n' pour non.")

    return

def ajouter_devise(nom, code_iso, quantité_en_usd):
    
    taux_de_conversion = recuperer_devises_enregistrees()
    taux_de_conversion[code_iso] = {"nom": nom,"quantite en usd": quantité_en_usd}
    with open("taux_de_conversion.txt", "w", encoding="utf-8") as fichier:
        fichier.write(str(taux_de_conversion))
    print(f"La devise {nom} ({code_iso}) a été ajoutée avec un taux de conversion de {quantité_en_usd}.")

def recuperer_devises_enregistrees():
    try:
        with open("taux_de_conversion.txt", "r", encoding="utf-8") as fichier:
            taux_de_conversion = eval(fichier.read())
    except FileNotFoundError:
        taux_de_conversion = {}

    return taux_de_conversion

def recuperer_quantité_en_usd(taux_de_conversion,code_iso):
    if code_iso in taux_de_conversion:
        quantite_en_usd = taux_de_conversion[code_iso].get("quantite en usd")
    else:
        print(f"Le code ISO '{code_iso}' n'a pas été trouvé dans le dictionnaire de taux de conversion.")
    return quantite_en_usd

def fin_de_processus():
    if resultat > 0 :
        historique()
        print (f"Pour {quantité} {name_base} vous aurez =======> {round(resultat,2)} {name_target}")
        choix_utilisateur_historique()
        quitter()
    else: 
        print ("taux de change impossible")
        quitter()


def convertisseur():
    choix_utilisateur_ajout_Devise()
    taux_de_conversion = recuperer_devises_enregistrees()                        # Définie la fonction principale
    liste_devises()
    while True:
        
        global quantité, name_base, name_target, resultat
        quantité = 0
        name_base = ""
        name_target = ""
        resultat = 0
        
        try:
            quantité = float(input("argent que vous avez : "))
            devise_base= str(input("choisissez la devise que vous avez : ")).upper()
            devise_target = str(input("choisissez la devise que vous voulez : ")).upper()

            name_base = c.get_currency_name(devise_base)
            name_target = c.get_currency_name(devise_target)

            try:
                resultat = ratio.convert(devise_base, devise_target, quantité)

            except RatesNotAvailableError:
                if devise_base in taux_de_conversion:
                    quantite_en_usd = recuperer_quantité_en_usd (taux_de_conversion, devise_base)
                    resultat = ratio.convert("USD", devise_target, quantite_en_usd)
                    
                    fin_de_processus()


                elif devise_target in taux_de_conversion:
                    quantite_en_usd = recuperer_quantité_en_usd (taux_de_conversion, devise_target)
                    resultat = ratio.convert(devise_base, "USD", quantité)
                    resultat =  resultat / quantite_en_usd
                    fin_de_processus()
                else: 
                    print("Les taux de change ne sont pas disponibles pour le moment. Veuillez réessayer plus tard.")
                continue
                
        except ValueError:
            print("Veuillez entrer une valeur numérique valide.")
            
        except KeyError:
            print("Devise invalide. Veuillez choisir une devise valide.")
    
        fin_de_processus()

        
convertisseur()