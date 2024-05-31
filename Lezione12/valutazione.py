# Esercitazione Classi ed Ereditarietà

# Question 1
"""Vogliamo gestire un contatore che può essere incrementato, decrementato, resettato e visualizzato. La classe offre un modo semplice per tenere traccia di un conteggio che non può diventare negativo.

Classe Contatore
Attributi:
- conteggio: un intero che conserva il valore del conteggio, inizializzato a 0.

Metodi:
- __init__(): Inizializza l'attributo conteggio a 0.
- setZero(): Imposta il conteggio a 0.
- add1(): Incrementa il conteggio di 1.
- sub1(): Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo. Se il conteggio è già 0, stampa un messaggio di errore.
- get(): Restituisce il valore corrente del conteggio.
- mostra(): Stampa a schermo il valore corrente del conteggio.

For example:
Test 	Result
c = Contatore()  
c.add1() 
c.mostra()
Conteggio attuale: 1

c = Contatore()  
c.sub1()  
c.mostra()
Non è possibile eseguire la sottrazione
Conteggio attuale: 0

c = Contatore() 
c.add1()
c.add1()
c.add1()
c.add1()
c.sub1()  
c.add1()
c.add1()
z  = c.get()
print(z)
5"""

print("Soluzione - Question 1:")

class Contatore:

    def __init__(self):
        self.conteggio: int = 0

    def setZero(self):
        self.conteggio = 0
        return self.conteggio

    def add1(self):
        self.conteggio += 1
        return self.conteggio

    def sub1(self):
        if self.conteggio > 0:
            self.conteggio -= 1
            return self.conteggio
        else:
            print("Non è possibile eseguire la sottrazione")
    
    def get(self):
        return self.conteggio
    
    def mostra(self):
        print(f"Conteggio attuale: {self.conteggio}")

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

# Question 2

"""Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione di ricette e i loro ingredienti.

Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.

    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un dizionario con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.

    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - list_recipes(): Elenca tutte le ricette esistenti.

    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.

For example:
Test 	Result

manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))

{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella']}
{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella', 'Basilico']}
{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}
{'Pizza Margherita': ['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}
['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']"""


print("Soluzione - Question 2:")

class RecipeManager:

    def __init__(self):
        self.catalogo: dict[str, list[str]] = {}

    # create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un dizionario con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.
    def create_recipe(self, name: str, ingredients: list[str]) -> dict:
        ricetta: dict[str, list[str]] = {}
        if name not in self.catalogo:
            self.catalogo[name] = ingredients
            ricetta[name] = ingredients
            return ricetta
        else:
            raise ValueError("Ricetta esiste già")
        
    # add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.
    def add_ingredient(self, recipe_name: str, ingredient: str) -> dict:
        ricetta: dict[str, list[str]] = {}
        if recipe_name in self.catalogo:
            if ingredient not in self.catalogo[recipe_name]:
                self.catalogo[recipe_name].append(ingredient)
                ricetta[recipe_name] = self.catalogo[recipe_name]
                return ricetta
            else:
                raise ValueError("ingrediente esiste già")
        else:
            raise ValueError("Ricetta non esiste")
    
    # remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
    def remove_ingredient(self, recipe_name: str, ingredient: str) -> dict:
        ricetta: dict[str, list[str]] = {}
        if recipe_name in self.catalogo:
            if ingredient in self.catalogo[recipe_name]:
                self.catalogo[recipe_name].remove(ingredient)
                ricetta[recipe_name] = self.catalogo[recipe_name]
                return ricetta
            else:
                raise ValueError("ingrediente non esiste")
        else:
            raise ValueError("Ricetta non esiste")

    # update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        ricetta: dict[str, list[str]] = {}

        if recipe_name in self.catalogo:
            if old_ingredient in self.catalogo[recipe_name]:
                if new_ingredient not in self.catalogo[recipe_name]:
                    for i in range(len(self.catalogo[recipe_name])):
                        if self.catalogo[recipe_name][i] == old_ingredient:
                            self.catalogo[recipe_name][i] = new_ingredient
                            ricetta[recipe_name] = self.catalogo[recipe_name]
                else:
                    raise ValueError("ingrediente esiste già")
            else:
                raise ValueError("ingrediente non esiste")
        else:
            raise ValueError("Ricetta non esiste")

        return ricetta
    
    # list_recipes(): Elenca tutte le ricette esistenti.
    def list_recipes(self) -> str:
        list_recipes: list = [name for name in self.catalogo.keys()]
        return list_recipes
    
    # list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
    def list_ingredients(self, recipe_name: str) -> list[str]:
        if recipe_name in self.catalogo:
            return self.catalogo[recipe_name]
        else:
            raise ValueError("Ricetta non esiste")

    # search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
    def search_recipe_by_ingredient(self, ingredient: str) -> list[str]:
        search_result: dict = {}
        for key, value in self.catalogo.items():
            if ingredient in value:
                search_result[key] = value

        if search_result == []:
            raise ValueError("nessuna ricetta contiene l'ingrediente")
        else:
            return search_result

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

# Question 3

"""In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di veicoli.

1. Classe Base: Veicolo
Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
 
Attributi:

    marca (stringa)
    modello (stringa)
    anno (intero)

Metodi:

    __init__(self, marca, modello, anno): metodo costruttore che inizializza gli attributi marca, modello e anno.
    descrivi_veicolo(self): metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".

2. Classe Derivata: Auto
Crea una classe derivata chiamata Auto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
Attributi:

    numero_porte (intero)

Metodi:

    __init__(self, marca, modello, anno, numero_porte): metodo costruttore che inizializza gli attributi della classe base e numero_porte.
    descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il numero di porte nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]".

3. Classe Derivata: Moto
Crea una classe derivata chiamata Moto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
Attributi:

    tipo (stringa, ad esempio "sportiva", "cruiser", ecc.)

Metodi:

    __init__(self, marca, modello, anno, tipo): metodo costruttore che inizializza gli attributi della classe base e tipo.
    descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il tipo di moto nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]".

For example:
Test 	Result

veicolo = Veicolo("Generic", "Model", 2020)
auto = Auto("Toyota", "Corolla", 2021, 4)
moto = Moto("Yamaha", "R1", 2022, "sportiva")

veicolo.descrivi_veicolo() 
auto.descrivi_veicolo()
moto.descrivi_veicolo()

Marca: Generic, Modello: Model, Anno: 2020
Marca: Toyota, Modello: Corolla, Anno: 2021, Numero di porte: 4
Marca: Yamaha, Modello: R1, Anno: 2022, Tipo: sportiva"""

print("Soluzione - Question 3:")

class Veicolo:

    def __init__(self,marca: str, modello: str, anno: int) -> None:
        self.marca: str = marca
        self.modello: str = modello
        self.anno: int = anno

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")


class Auto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int) -> None:
        Veicolo.__init__(self, marca, modello, anno)
        self.numero_porte: int = numero_porte

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")


class Moto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, tipo: int) -> None:
        Veicolo.__init__(self, marca, modello, anno)
        self.tipo: int = tipo

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")
# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

# Question 4

"""Obiettivo. L'obiettivo di questo esercizio è creare un modello semplice per simulare la crescita delle popolazioni di due specie animali usando la programmazione orientata agli oggetti in Python.

Descrizione del problema
Due specie animali, i Bufali Klingon e gli Elefanti, vivono in una riserva naturale. Ogni specie ha una popolazione iniziale e un tasso di crescita annuo. Vogliamo sapere:
- In quanti anni la popolazione degli Elefanti supererà quella dei Bufali Klingon.
- n quanti anni la popolazione dei Bufali Klingon raggiungerà una densità di 1 individuo per km².
 
Specifiche tecniche

1. Classe Specie
- Attributi:

    nome (str): Nome della specie.
    popolazione (int): Popolazione iniziale.
    tasso_crescita (float): Tasso di crescita annuo percentuale.

- Metodi:

    __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float): Costruttore per inizializzare gli attributi della classe.
    cresci(self): Metodo per aggiornare la popolazione per l'anno successivo.
    anni_per_superare(self, altra_specie: 'Specie') -> int: Metodo per calcolare in quanti anni la popolazione di questa specie supererà quella di un'altra specie.
    getDensita(self, area_kmq: float) -> int: Metodo per calcolare in quanti anni la popolazione raggiungerà una densità di 1 individuo per km².

2. Sottoclassi BufaloKlingon e Elefante
Entrambe le sottoclassi animali BufaloKlingon ed Elefante devono ereditare dalla classe base Specie e devono inizializzare il nome della specie rispettiva.
 
Formule Matematiche:

    Aggiornamento della popolazione per l'anno successivo:
        Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)
    Calcolo della densità di popolazione:
        Formula: popolazione / area_kmq
        Hint: Loop incrementale che continua ad aggiornare la popolazione finché la densità non raggiunge 1 individuo per km²
    Calcolo degli anni necessari per superare la popolazione di un'altra specie:
        Hint: Loop incrementale che continua ad aggiornare la popolazione di entrambe le specie finché la popolazione di questa specie non supera quella dell'altra.

For example:
Test 	Result
# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

# Calcolo degli anni necessari per superare
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

# Calcolo della densità di popolazione per i Bufali Klingon
anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")

Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: 16
Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: 4"""