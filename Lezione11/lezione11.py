"""Sistema di Prenotazione Cinema. Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in programmazione. Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.

Classi:
- Film: Rappresenta un film con titolo e durata.
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.
    Metodi:
    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
- Cinema: Gestisce le operazioni legate alla gestione delle sale.
    Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato."""

class Film:

    def __init__(self, movie_title: str, runtime: float) -> None:
        self.movie_title = movie_title
        self.runtime = runtime

    def __str__(self) -> str:
        return f"movie title: {self.movie_title}, runtime: {self.runtime}."


class Sala:

    def __init__(self, auditorium_number: int, available_seats: int, currently_showing: Film = None) -> None:
        self.auditorium_number = auditorium_number
        self.available_seats = available_seats
        self.booked_seats = 0
        self.currently_showing = currently_showing

    def __str__(self) -> str:
        return f"auditorium number: {self.auditorium_number}, available seats: {self.available_seats}, booked seats: {self.booked_seats}, currently showing: {self.currently_showing}"
    
    def book_seat(self, seats: int) -> str:
        if seats <= self.available_seats:
            self.available_seats -= seats
            self.booked_seats += seats
            print(f"{seats} tickets were booked!")
        else:
            return "not enough seats available."
    
    def get_available_seats(self) -> int:
        return self.available_seats
    

class Cinema:

    def __init__(self) -> None:
        self.auditorium_list: list[Sala] = []

    def __str__(self) -> str:
        return "\n".join(str(auditorium) for auditorium in self.auditorium_list)

    def increase_auditorium_list(self, auditorium: Sala) -> None:
        self.auditorium_list.append(auditorium)
    
    def book_movie(self, film: str, seats: int) -> str:
        for auditorium in self.auditorium_list:
            if auditorium.currently_showing.movie_title == film:
                return auditorium.book_seat(seats)
            

"""Test case:
- Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
- Un cliente sceglie un film e prenota un certo numero di posti.
- Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione."""

film1: Film = Film("Furiosa: A Mad Max Saga", 2.5)
film2: Film = Film("Castle in the Sky", 2.1)
film3: Film = Film("Challengers", 3.1)

sala1: Sala = Sala(auditorium_number = 1, available_seats = 100, currently_showing = film1)
sala2: Sala = Sala(auditorium_number = 2, available_seats = 50, currently_showing = film2)
sala3: Sala = Sala(auditorium_number = 3, available_seats = 20, currently_showing = film3)   

cinema1: Cinema = Cinema()

cinema1.increase_auditorium_list(sala1)
cinema1.increase_auditorium_list(sala2)
cinema1.increase_auditorium_list(sala3)
print()
cinema1.book_movie("Castle in the Sky", 5)
print()
cinema1.book_movie("Challengers", 15)
print()
cinema1.book_movie("Furiosa: A Mad Max Saga", 20)
print()
print(sala1.get_available_seats())
print()
print(cinema1)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Gestione di un magazzino. Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino."""

class Product:

    def __init__(self, name: str, quantity: int) -> None:
        self.name = name
        self.quantity = quantity

class Warehouse:

    def __init__(self):
        self.product_list = []

    def add_product(self, product: Product) -> None:
        self.product_list.append(product)

    def find_product(self, product_name: str) -> str:
        for product in self.product_list:
            if product_name == product.name:
                return product.name
            else:
                return "product not available!"
            
    def check_quantity(self, product_name: str) -> str:
        product: str = self.find_product(product_name)

        for item  in self.product_list:
            if item.name == product:
                return item.quantity
            
prodotto1: Product = Product("shampoo", 3)
prodotto2: Product = Product("soap", 10)

warehouse1: Warehouse = Warehouse()

warehouse1.add_product(prodotto1)
warehouse1.add_product(prodotto2)

print(warehouse1.find_product("shampoo"))
print(warehouse1.check_quantity("shampoo"))
print(warehouse1.find_product("banana"))
print(warehouse1.check_quantity("banana"))