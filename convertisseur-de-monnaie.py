from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyCodes()
c.get_symbol('GBP')
ratio = CurrencyRates()

#===================== zone de test ================================

"""
print(ratio.get_rates("USD"))
print (CurrencyRates().convert("USD","EUR",10))
taux_eur_usd = ratio.get_rate ("EUR", "USD")

print(taux_eur_usd)
total = ratio.convert('USD', 'EUR', 10)  # convert('USD', 'INR', 10) devise de base vers la devise target
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
 
    with open("historique.txt","a") as fichier:
        fichier.write(f"Pour {quantité} {name_base} vous aurez =======> {round(resultat,2)} {name_target}" + "\n")

def lire_historique():                      # Définie la fonction qui permet de lire le fichier historique.txt et de l'afficher dans le terminal
    with open("historique.txt", "r") as fichier:
	    print (fichier.read())

def choix_utilisateur_historique():         # Définie la fonction qui demande a l'utilisateur si il veux ou non afficher l'historique

    while True:
        
        reponse = input("Voulez-vous consulter l'historique ? (y/n): ").lower()
        if reponse == 'y':
            print("voici l'historique !")
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

def convertisseur():                        # Définie la fonction principale
    
    liste_devises()
    while True:
        
        global quantité, name_base, name_target, resultat

        try:
            quantité = float(input("argent que vous avez : "))
            devise_base= str(input("choisissez la devise que vous avez : ")).upper()
            devise_target = str(input("choisissez la devise que vous voulez : ")).upper()

            resultat = ratio.convert(devise_base, devise_target, quantité)
            name_base = c.get_currency_name(devise_base)
            name_target = c.get_currency_name(devise_target)
        

        except Exception as e :
            print("rentrez une Valeur valide")
            break
        else:
            historique()
            return print (f"Pour {quantité} {name_base} vous aurez =======> {round(resultat,2)} {name_target}")
        finally:
            
            choix_utilisateur_historique()
            quitter()
            continue
        
convertisseur()