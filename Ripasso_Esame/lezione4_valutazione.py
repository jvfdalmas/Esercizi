"""1. Nel gioco del blackjack, il valore di una mano è determinato dalla somma dei valori delle carte. Ogni carta ha un valore compreso tra 2 e 11 compresi. Tuttavia, se una mano contiene un asso, il valore dell'asso può essere 1 o 11, a seconda di quale sia più favorevole al giocatore in quel momento. Dato un elenco di valori delle carte che rappresentano una mano di blackjack, scrivi una funzione per determinare il valore totale della mano."""



# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""2. Uno sviluppatore web deve sapere come progettare le dimensioni di una pagina web. Pertanto, data l'area specifica di una pagina Web rettangolare, il tuo compito ora è progettare una pagina Web rettangolare, la cui lunghezza L e larghezza W soddisfino i seguenti requisiti:

1. L'area della pagina web rettangolare che hai progettato deve essere uguale all'area di destinazione specificata.
2. La larghezza W non deve essere maggiore della lunghezza L, il che significa L >= W.
3. La differenza tra la lunghezza L e la larghezza W dovrebbe essere la minima possibile.

Restituisce una lista [L, W] dove L e W sono la lunghezza e la larghezza della pagina web che hai progettato in sequenza.

Esempio:
construct_rectangle(4)
L'area target è 4 e tutti i modi possibili per costruirla sono [1,4], [2,2], [4,1].
Ma secondo il requisito 2, [1,4] è illegale; secondo il requisito 3, [4,1] non è ottimale rispetto a [2,2]. Quindi la lunghezza L è 2 e la larghezza W è 2.

print(construct_rectangle(4)) -> [2, 2]"""

def construct_rectangle(n: int) -> list[int]:

    def discoverLandW(l, w, n):
        memo = []

        if l == 0 or w == 0:
            return memo
        
        if w * l == n:
            memo.append([l, w])

        memo += discoverLandW(l, w - 1, n)
        memo += discoverLandW(l -1, w, n)

        return memo

    coord: list = discoverLandW(n, n, n)
    min_dif = n
    for item in coord:
        if item[0] <= item[1]:
            if abs(item[0] - item[1]) < min_dif:
                res = item
                min_dif = abs(item[0] - item[1])
    
    return res

print(construct_rectangle(4))




# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""3. Scrivi una funzione che accetta una stringa come input, rimuove le parole non significative comuni stop_words e restituisce un dizionario in cui le chiavi sono parole univoche nel testo rimanente (ignorando la distinzione tra maiuscole e minuscole e la punteggiatura) e i valori sono le frequenze di quelle parole.

For example:
Test 	Result
stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."
print(word_frequency(text, stopwords))
{'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 2, 'dog': 2, 'very': 1}"""

def word_frequency(stringa: str, stop: list) -> dict:
    res = {}

    for char in stringa:
        if not char.isalpha() and not char.isspace():
            stringa = stringa.replace(char,"")

    lista = stringa.lower().split()

    for word in lista:
        if res.get(word):
            res[word] += 1
        elif word not in stop:
            res[word] = 1
    
    return res

stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."
print(word_frequency(text, stopwords))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""4. Hai il compito di indagare su un caso di numeri mancanti! Ti viene fornito un elenco di numeri univoci (nums) da 1 a n, dove n è la lunghezza dell'elenco. Sembra però che ci sia un problema: mancano alcuni numeri!
La tua missione è scrivere una funzione che prenda come input questo elenco di numeri (nums) potenzialmente incompleti. Questo elenco rappresenta i numeri esistenti, ma alcuni numeri tra 1 e n potrebbero mancare.
La funzione restituisce una nuova lista contenente tutti i numeri mancanti da 1 a n che non sono presenti nella lista originale. 

For example:
Test 	Result
print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))

[5, 6]"""

def find_disappeared_numbers(lista: list[int]) -> list[int]:
    base = set(range(1,len(lista)+1))
    lista = set(lista)
    missingNo = list(base - lista)

    return missingNo

print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""5. Sei un detective esperto nel mondo dei testi e un caso sconcertante è arrivato sulla tua scrivania. Due stringhe, s e t, sono i tuoi sospettati. La tua missione: determinare se s si nasconde in bella vista all'interno di t, ma con una svolta!
Qual è il problema?
Non puoi semplicemente confrontare le stringhe lettera per lettera. Immagina che s sia un personaggio subdolo che cerca di confondersi tra la folla (t). Potrebbero camuffarsi nascondendosi tra altri personaggi, ma non cambiano mai il loro ordine! Quindi, "ace" può intrufolarsi in "abcde" (rimuove semplicemente "b" e "d"), ma "aec" non funzionerebbe (l'ordine cambia).
Scrivi una funzione di interruzione del codice che prenda la stringa s (il carattere subdolo) e t (la folla) come input. Se è possibile trovare s in agguato all'interno di t mantenendo il suo travestimento (ordine), restituisce True. Altrimenti restituisce False. Dimostra le tue abilità da detective e svela la verità nascosta!

For example:
Test 	Result
print(is_subsequence("abc", "ahbgdc"))
True
print(is_subsequence("axc", "ahbgdc"))
False"""

def is_subsequence(s: str, t: str) -> bool:
    s = list(s)
    for char in t:
        if char == s[0]:
            s.pop(0)
    
    return len(s) == 0



print(is_subsequence("abc", "ahbgdc"))
#True
print(is_subsequence("axc", "ahbgdc"))
#False


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""6. Data una lista di numeri interi, riordina i numeri in modo che tutti i numeri pari appaiano prima di tutti i numeri dispari. Restituisce l'elenco riorganizzato.

For example:
Test 	Result
print(even_odd_pattern([3, 6, 1, 8, 4, 7]))
[6, 8, 4, 3, 1, 7]"""

def even_odd_pattern(lista: list[int]) -> list[int]:
    even = []
    odd = []
    for n in lista:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    res = even + odd
    return res

print(even_odd_pattern([3, 6, 1, 8, 4, 7]))

#merge sort algorithm
def mergesort(lista: list[int]) -> list[int]:
    if len(lista) > 1:
        left = lista[:len(lista)//2]
        right = lista[len(lista)//2:]

        mergesort(right)
        mergesort(left)

        i = 0 # left
        j = 0 # right
        k = 0 # main

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
                k += 1
            else:
                lista[k] = right[j]
                j += 1
                k += 1
        
        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1

        return lista

print(mergesort([3, 6, 1, 8, 4, 7]))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""7. Scrivi una funzione prime_factors(n: int) -> list[int] che trova i fattori primi di un numero n dato in input

For example:
Test 	Result

print(prime_factors(4))
[2, 2]"""

def prime_factors(n: int) -> list[int]:
    n = abs(n)
    res = []
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n = int(n / divisor)
            res.append(divisor)
        else:
            divisor += 1

    return res


def run_tests():
    # Test case 1: Small number with multiple prime factors
    print("Test case 1:", prime_factors(4))  # Expected: [2, 2]
    
    # Test case 2: Prime number
    print("Test case 2:", prime_factors(5))  # Expected: [5]
    
    # Test case 3: Composite number with multiple prime factors
    print("Test case 3:", prime_factors(18))  # Expected: [2, 3, 3]
    
    # Test case 4: Larger composite number
    print("Test case 4:", prime_factors(60))  # Expected: [2, 2, 3, 5]
    
    # Test case 5: Large prime number
    print("Test case 5:", prime_factors(101))  # Expected: [101]
    
    # Test case 6: Number with no factors except itself (prime)
    print("Test case 6:", prime_factors(29))  # Expected: [29]
    
    # Test case 7: Number 1 (edge case)
    print("Test case 7:", prime_factors(1))  # Expected: []
    
    # Test case 8: Negative number (if you want to handle negatives)
    print("Test case 8:", prime_factors(-12))  # Expected: [2, 2, 3]

run_tests()

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""8. Immagina di avere uno scrigno pieno di gioielli (rappresentati da una lista di numeri interi). Questi gioielli hanno vari valori, alcuni più preziosi di altri. Il tuo compito è trovare il terzo gioiello distinto più prezioso nello scrigno.
Qual è la svolta?
Nello scrigno possono esserci gioielli duplicati (numeri con lo stesso valore). A noi però interessano solo valori distinti, ovvero gioielli con valori unici.
Scrivi una funzione che prenda come input questo array di valori di gioielli (numeri). Se nello scrigno sono presenti almeno tre valori distinti, la funzione dovrebbe restituire il valore del terzo gioiello distinto di maggior valore.
Ma c'è un problema!
Se non ci sono tre valori distinti (ad esempio, solo due valori univoci o tutti i valori sono uguali), la funzione dovrebbe restituire il valore del gioiello più prezioso nello scrigno.
For example:
Test 	Result
print(third_max([3, 2, 1])) #1
print(third_max([1, 2])) #2
print(third_max([2, 2, 3, 1])) #1"""

def third_max(arr: list[int]) -> int:
    arr = sorted(list(set(arr)), reverse= True)
    if len(arr) >= 3:
        return arr[2]
    else:
        return arr[0]

print(third_max([3, 2, 1])) #1
print(third_max([1, 2])) #2
print(third_max([2, 2, 3, 1])) #1
# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Bonus 1. Immaginiamo di avere un tipo speciale di sistema numerico in cui gli unici elementi costitutivi sono i numeri 2, 3 e 5. Chiamiamo questi elementi costitutivi "fattori primi" perché non possono essere ulteriormente scomposti. Un "numero brutto" in questo sistema è un numero costruito utilizzando solo questi fattori primi (2, 3 o 5). Ad esempio, 6 (che può essere costruito come 2 x 3) è un numero brutto, ma 7 (che ha un fattore primo pari a 7) non lo è.

For example:
print(ugly_number(6))
True
print(ugly_number(1))
True
print(ugly_number(14))
False"""



# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Bonus 2.Immagina di avere una raccolta di note musicali rappresentate da una serie di numeri interi. Queste note possono avere altezze (valori) diversi. Una sequenza armoniosa è come una melodia piacevole in cui la differenza di altezza tra la nota massimale e quella minimale è uguale a 1. Ad esempio, la serie di note [3,2,2,2,3] è armoniosa, perché la differenza fra 3 e 2 è 1.
Trovare l'armonia perfetta:
Il tuo compito è scrivere una funzione che prenda come input questa serie di note musicali (numeri). La funzione dovrebbe trovare la sequenza armoniosa più lunga che puoi creare da queste note. Ricorda, una sottosequenza è una selezione di note dalla lista originale che mantiene l'ordine degli elementi.
Colpire le note giuste:
Ad esempio, se nums è [1, 3, 2, 2, 5, 2, 3, 7], la sottosequenza armonica più lunga è [3, 2, 2, 2, 3]. La funzione dovrebbe restituire 5 (la lunghezza di questa sottosequenza)."""


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Bonus 3. Date due stringhe note e magazine, restituisci true se note può essere costruita utilizzando le lettere di magazine e false in caso contrario. Ogni lettera nella magazine può essere utilizzata solo una volta in note.
For example:
print(ransom("a","b"))
False
print(ransom("aa", "ab"))
False
print(ransom("aa","aab"))
True"""


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Bonus 4. Dato un numero intero, restituisce una stringa che ne rappresenta la rappresentazione esadecimale. Per gli interi negativi viene utilizzato il metodo del complemento a due.

Tutte le lettere nella stringa di risposta dovrebbero essere caratteri minuscoli e non dovrebbero esserci zeri iniziali nella risposta tranne lo zero stesso.

Nota: non è consentito utilizzare alcun metodo di libreria integrato per risolvere direttamente questo problema.

For example:
print(to_hex(26))
1a

print(to_hex(-1))
ffffffff"""