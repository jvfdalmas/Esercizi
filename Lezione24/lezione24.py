# Testi Digitali

""" Si definisca una classe Documento che contenga una variabile di tipo stringa chiamata testo e che memorizza qualsiasi contenuto testuale per il documento.

Si crei un metodo getText() che restituisca il testo. Si crei un metodo setText() per impostare il testo. Scrivere un metodo isInText() che restituisce True se un documento contiene la parola chiave specificata.

Si definisca poi una classe Email che sia derivata da Documento e che includa le variabili per il mittente, il destinatario e il titolo del messaggio.

Si implementino i metodi get() e set() appropriati per tali variabili. Il corpo del messaggio dell’e-mail dovrebbe essere memorizzato nella variabile ereditata testo.

Si ridefinisca il metodo getText() per concatenare e ritornare tutti i campi di testo (mittente, destinatario, titolo del messaggio, e messaggio) come di seguito:
 
    Da: alice@example.com, A: bob@example.com
    Titolo: Incontro
    Messaggio: Ciao Bob, possiamo incontrarci domani?
 
Inoltre, si implementi un metodo writeToFile() per scrivere il risultato del metodo getText() in un file di testo e in un percorso specificato.
 
Analogamente, si definisca una classe File che sia derivata da Documento e includa una variabile per il nomePercorso.
Crea un file document.txt con all'interno la stringa "Questo e' il contenuto del file." e salvalo in una directory a tua scelta e che sarà indicata in nomePercorso.

I contenuti testuali del file dovrebbero essere letti da questo file di testo al percorso specificato in nomePercorso e memorizzati nella variabile ereditata testo tramite un metodo leggiTestoDaFile().

Si ridefinisca il metodo getText() che concateni e ritorni il nome del percorso e il testo, come di seguito:
 
    Percorso: nomePercorso/document.txt
    Contenuto: Questo e' il contenuto del file."""


class Documento:

    def __init__(self) -> None:
        self._testo: str = ""

    def getText(self) -> str:
        return self._testo 

    def setText (self, testo: str) -> None:
        self._testo: str = testo
        return self._testo 

    def isInText(self, arg) -> bool:
        if arg in self.testo:
            return True
        else:
            return False


class Email(Documento):

    def __init__(self) -> None:
        super().__init__()
        self._mittente: str = ""
        self._destinatario: str = ""
        self.oggetto: str = ""

    def setMittente(self, _mittente: str) -> None:
        self._mittente: str = _mittente
        return self._mittente

    def getMittente(self) -> str:
        return self._mittente

    def setDestinatario(self, _destinatario: str) -> None:
        self._destinatario: str = _destinatario
        return self._destinatario

    def getDestinatario(self) -> str:
        return self._destinatario

    def setOggetto(self, oggetto: str) -> None:
        self._oggetto: str = oggetto
        return self._oggetto

    def getOggetto(self) -> str:
        return self._oggetto

    def getText(self) -> str:
        return f""""
        Da: {self.getMittente()}, A: {self.getDestinatario()}
        Titolo: {self.getOggetto()}
        Messaggio: {super().getText()}
            """
    
    def writeToFile(self, fname: str = "document.txt") -> None:
        with open(fname, mode="w") as f:
            f.write(self.getText())
            return f

        


"""Analogamente, si definisca una classe File che sia derivata da Documento e includa una variabile per il nomePercorso.
Crea un file document.txt con all'interno la stringa "Questo e' il contenuto del file." e salvalo in una directory a tua scelta e che sarà indicata in nomePercorso.

I contenuti testuali del file dovrebbero essere letti da questo file di testo al percorso specificato in nomePercorso e memorizzati nella variabile ereditata testo tramite un metodo leggiTestoDaFile().

Si ridefinisca il metodo getText() che concateni e ritorni il nome del percorso e il testo, come di seguito:
 
    Percorso: nomePercorso/document.txt
    Contenuto: Questo e' il contenuto del file."""

class File(Documento):
    
    def __init__(self) -> None:
        super().__init__()
        self._path = ""

    def setPath(self, _path):
        self._path = _path
        return self._path
    
    def getPath(self) -> str:
        return self._path

    def leggiTestoDaFile(self) -> str:
        with open(self.getPath(), mode="r") as f:
            return f.read()

    def getText(self) -> str:
        return f""""
        Percorso: {self.getPath()}
    Contenuto: {self.leggiTestoDaFile()}"""


###########################################################################

doc = Documento()
doc.setText("""SUGLI ERRORI
Gli errori sono inevitabili. Errare è umano,
perseverare è diabolico. Non ci sono rimedi
a questo stato di cose (su questa terra).""")
print(doc.getText())

print("\n")

mail = Email()
mail.setText("""SUGLI ERRORI
Gli errori sono inevitabili. Errare è umano,
perseverare è diabolico. Non ci sono rimedi
a questo stato di cose (su questa terra).""")
mail.setDestinatario("dddd@hotmail.com")
mail.setMittente("mmm@gmail.com")
mail.setOggetto("Poesia")
print(mail.getText())
mail.writeToFile()
