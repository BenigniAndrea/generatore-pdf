from reportlab.lib.pagesizes import letter  #Per il formato della pagina in verticale
from reportlab.pdfgen import canvas  
import json  
from reportlab.lib import colors 

WIDTH, HEIGHT = letter   # Larghezza e altezza della pagina

STILE_TITOLI = "Helvetica-Bold"
STILE_TESTO = "Helvetica"
DIMENSIONE_TITOLI = 14
DIMENSIONE_TESTO = DIMENSIONE_TITOLI - 2

# Classe contenente i metodi per l'impaginazione del file PDF
class PDFmanager:
    numeroPagina = 1                                 # Per stampare il numero della pagina

    # Costruttore
    def __init__(self, c, dati):
        self.c = c                                   # Il canva su cui scriveremo i dati
        self.dati = dati                             # I dati caricati dal file JSON e quindi dal kickoff
        self.interlinea = DIMENSIONE_TESTO + 10      # Interlinea del testo

    # Aggiunge una nuova pagina
    def aggiungiPagina(self):
        self.c.showPage()                            # Crea una nuova pagina
        self.c.setFillColor(colors.black)            # Imposto il colore di testo e linee 
        self.numeroPagina += 1                       # Incremento il numero di pagina
    
    # Aggiunge un'intestazione per la pagina
    def aggiungiIntestazione(self, x, y, immagine, image_width, image_height, testo):    
        self.c.drawImage(immagine, x, y, image_width, image_height)                        # Aggiungo l'immagine
        self.c.setFont(STILE_TITOLI, DIMENSIONE_TITOLI)                                    # Setto il font del titolo
        self.c.drawString(WIDTH - x - self.c.stringWidth(testo, STILE_TITOLI, DIMENSIONE_TITOLI), HEIGHT - 70, testo)  # Scrivo il titolo dell'intestazione in modo che sia distante 'x' dal margine destro (alla larghezza della pagina sottraggo la 'x' e la larghezza del titolo)
        self.c.setFont(STILE_TESTO, DIMENSIONE_TESTO)                                      # Setto il font del testo
        self.c.drawString(WIDTH - x - self.c.stringWidth("P. ", STILE_TESTO, DIMENSIONE_TESTO), HEIGHT - DIMENSIONE_TITOLI - 75, "P." + str(self.numeroPagina))  # Scrivo il numero della pagina in modo che sia distante 'x' dal margine destro
 
    # Aggiunge un titolo
    def aggiungiTitolo(self, x, y, titolo):
        self.c.setFont(STILE_TITOLI, DIMENSIONE_TITOLI)
        self.c.drawString(x, y, titolo + ":")        # Dopo il titolo scrivo ':'
        
    # Aggiunge un testo    
    def aggiungiContenuto(self, x, y, testo):
        self.c.setFont(STILE_TESTO, DIMENSIONE_TESTO)
        self.c.drawString(x, y, testo)

    # Aggiunge una linea retta che va da x1 a x2 ed è ad altezza y
    def aggiungiLineaRetta(self, x1, x2, y):
        self.c.line(x1, y, x2, y)

    # Aggiunge un titolo affiancato alla sua destra da un testo
    def aggiungiTitoloConTesto(self, x, y, titolo, testo):
        self.c.setFont(STILE_TITOLI, DIMENSIONE_TITOLI)
        self.c.drawString(x, y, titolo + ": ")
        self.c.setFont(STILE_TESTO, DIMENSIONE_TESTO)
        self.c.drawString(x + self.c.stringWidth(titolo, STILE_TITOLI, DIMENSIONE_TITOLI) + 20, y, testo)  # Disegno il testo a destra del titolo di 20px, alla 'x' del titolo aggiungo quindi la larghezza del testo + 20px

    # Aggiunge un titolo affiancato alla sua destra da una linea retta che si estende fino a x2
    def aggiungiTitoloConLinea(self, x1, x2, y, titolo):
        self.c.setFont(STILE_TITOLI, DIMENSIONE_TITOLI)
        self.c.drawString(x1, y, titolo + ": ")
        self.c.line(x1 + self.c.stringWidth(titolo, STILE_TITOLI, DIMENSIONE_TITOLI) + 10, y, x2, y)  # Disegno una retta a destra del titolo di 10px che va fino a x2

    # Aggiunge un elenco puntato
    def aggiungiElencoPuntato(self, x, y, contenuto):
        self.c.setFont(STILE_TESTO, DIMENSIONE_TESTO)
        for elemento in contenuto:                           # Scansiono tutti gli elementi dell'elenco
            self.c.drawString(x, y, "●   " + str(elemento))  # Scrivo tutti gli elementi in formato stringa (in caso non lo siano) preceduti dal punto dell'elenco
            y -= self.interlinea                             # Mi abbasso dell'interlinea settata nel costruttore per scrivere l'elemento successivo

    # Aggiunge uno o più box uno sotto l'altro, composti da un titolo e un testo 
    def aggiungiBoxSchema(self, x, y, titolo, contenuto):
        interlineaCampi = 40                                 # L'interlinea tra il titolo e i vari campi nel box
        start_y = y + 20                                     # La 'y' iniziale del box per disegnare le linee quando i contenuti sono stati scritti
        
        self.c.setFont(STILE_TITOLI, DIMENSIONE_TITOLI)
        self.c.drawString(x, y, titolo)
        self.c.line(x - 20, y + 20, x + self.c.stringWidth(titolo, STILE_TITOLI, DIMENSIONE_TITOLI) + 10, y + 20)  # Disegno il margine sopra del box a 20px sopra il titolo che va da 20px prima del titolo a 20px dopo del titolo
        self.c.line(x - 20, y - DIMENSIONE_TITOLI, x + self.c.stringWidth(titolo, STILE_TITOLI, DIMENSIONE_TITOLI) + 10, y - DIMENSIONE_TITOLI) # Disegno la linea di mezzo che separa il titolo dai campi del box, uguale al margine sopra del box ma appena sotto al titolo
        y -= interlineaCampi
        self.c.setFont(STILE_TESTO, DIMENSIONE_TESTO)

        for elemento in contenuto:           # Per ogni campo del box
            self.c.drawString((x + x + self.c.stringWidth(titolo, STILE_TITOLI, DIMENSIONE_TITOLI) - 10) / 2 - self.c.stringWidth(elemento, STILE_TESTO, DIMENSIONE_TESTO) / 2, y, elemento)  # Scrivo il testo del box CENTRATO nel box
            self.c.line(x - 20, y - DIMENSIONE_TITOLI, x + self.c.stringWidth(titolo, STILE_TITOLI, DIMENSIONE_TITOLI) + 10, y - DIMENSIONE_TITOLI) # Disegno la linea di mezzo con il prossimo campo
            y -= interlineaCampi       

        self.c.line(x - 20, start_y, x - 20, y - DIMENSIONE_TITOLI + interlineaCampi)    # Disegno il margine sinistro del box che parte a 20 px a sinistra del testo e va dalla y iniziale alla y dell'ultima riga di testo diminuita dell'interlinea
        self.c.line(x + self.c.stringWidth(titolo, STILE_TITOLI, DIMENSIONE_TITOLI) + 10, start_y, x + self.c.stringWidth(titolo, STILE_TITOLI, DIMENSIONE_TITOLI) + 10, y - DIMENSIONE_TITOLI + interlineaCampi) # Disegno il margine destro del box, come quello sinistro ma 20px a destra del testo

    # Variante di box schema che contiene dei titoli in corsivo e due campi testo in ogni box       
    def aggiungiBoxSchemaInterfacce(self, x, y, titolo, contenuto):
        interlineaCampi = 40
        interLineaContenuto = 15         # L'interlinea tra le righe di testo in ogni campo
        start_y = y + 20
        
        self.c.setFont(STILE_TITOLI, DIMENSIONE_TITOLI)
        self.c.drawString(x, y, titolo)
        self.c.line(x - 20, y + 20, x + self.c.stringWidth(titolo, STILE_TITOLI, DIMENSIONE_TITOLI) + 10, y + 20)            # Margine sopra
        self.c.line(x - 20, y - DIMENSIONE_TITOLI, x + self.c.stringWidth(titolo, STILE_TITOLI, DIMENSIONE_TITOLI) + 10, y - DIMENSIONE_TITOLI)             # Linea di mezzo
        y -= interlineaCampi

        for elemento in contenuto:        # Per ogni campo del box (che deve essere una lista)
            self.c.setFont("Helvetica-Oblique", DIMENSIONE_TESTO)   # Setto il testo in corsivo
            self.c.drawString((x + x + self.c.stringWidth(titolo, STILE_TITOLI, DIMENSIONE_TITOLI) - 10) / 2 - self.c.stringWidth(elemento, STILE_TESTO, DIMENSIONE_TESTO) / 2, y, elemento)  # Scrivo il testo centrato
            self.c.setFont(STILE_TESTO, DIMENSIONE_TESTO) 
            for elemento2 in contenuto[elemento]:      # Per ogni riga del campo di testo
              y -= interLineaContenuto
              self.c.drawString((x + x + self.c.stringWidth(titolo, STILE_TITOLI, DIMENSIONE_TITOLI) - 10) / 2 - self.c.stringWidth(elemento2, STILE_TESTO, DIMENSIONE_TESTO) / 2, y, elemento2)  # Scrivo il testo centrato
            self.c.line(x - 20, y - DIMENSIONE_TITOLI, x + self.c.stringWidth(titolo, STILE_TITOLI, DIMENSIONE_TITOLI) + 10, y - DIMENSIONE_TITOLI)    # Disegno la linea di mezzo tra i campi
            y -= interlineaCampi       

        self.c.line(x - 20, start_y, x - 20, y - DIMENSIONE_TITOLI + interlineaCampi)  # Margine sinistro del box
        self.c.line(x + self.c.stringWidth(titolo, STILE_TITOLI, DIMENSIONE_TITOLI) + 10, start_y, x + self.c.stringWidth(titolo, STILE_TITOLI, DIMENSIONE_TITOLI) + 10, y - DIMENSIONE_TITOLI + interlineaCampi)   # Margine destro del box

    # Aggiunge un box di una certa larghezza e una certa altezza composto da un titolo e un testo separati da una linea, usato per comporre le tabelle con celle di dimensioni diverse
    def aggiungiBoxTabella(self, x, y, larghezza, altezza, titolo, contenuto):
        self.c.setFont(STILE_TITOLI, DIMENSIONE_TITOLI)
        self.c.rect(x, y - DIMENSIONE_TITOLI, larghezza, altezza/2)    # Disegno un rettangolo che circonda il titolo e che ha una certa larghezza
        self.c.drawString(x + (larghezza - self.c.stringWidth(titolo, STILE_TITOLI, DIMENSIONE_TITOLI)) / 2, y - DIMENSIONE_TITOLI - DIMENSIONE_TITOLI + ((altezza/2) + DIMENSIONE_TITOLI) / 2, titolo)  # Scrivo il titolo centrato nel rettangolo
        self.c.setFont(STILE_TESTO, DIMENSIONE_TESTO)
        self.c.rect(x, y - DIMENSIONE_TITOLI - (altezza/2), larghezza, altezza/2)    # Disegno un rettangolo che circonda il testo, attaccato al margine inferiore del rettangolo precedente
        self.c.drawString(x + (larghezza - self.c.stringWidth(contenuto, STILE_TESTO, DIMENSIONE_TESTO)) / 2, y - DIMENSIONE_TITOLI - DIMENSIONE_TITOLI - (altezza/2) + ((altezza/2) + DIMENSIONE_TITOLI) / 2, contenuto)  # Scrivo il testo centrato nel rettangolo

    # Aggiunge una checklist
    def aggiungiCheckList(self, x, y, contenuto):
        self.c.setFont(STILE_TESTO, DIMENSIONE_TESTO)
        for elemento in contenuto:     # Per ogni elemento della checklist
            self.c.drawString(x, y, "☐  " + str(elemento))   # Scrivo l'elemento della checklist 
            y -= self.interlinea

    # Aggiunge un elenco puntato sviluppato orizzontalmente
    def aggiungiElenchiPuntatiOrizzontali(self, x, y, contenuto):
        self.c.setFont(STILE_TESTO, DIMENSIONE_TESTO)
        for elemento in contenuto:     # Per ogni elemento dell'elenco 
            self.c.drawString(x, y, "●   " + str(elemento))
            x += 200       # Mi sposto a destra di 200px per disegnare il prossimo elemento

    # Aggiunge un elenco di titoli con sott un testo sviluppato orizzontalmente
    def aggiungiElencoOrizzontale(self, x, y, contenuto):
        for elemento in contenuto:     # Per ogni elemento dell'elenco 
            for chiave, valore in elemento.items():    # Leggo il titolo (chiave) e il testo (valore)
                self.c.setFont(STILE_TITOLI, DIMENSIONE_TITOLI)
                self.c.drawString(x, y, str(chiave))   # Scrivo il titolo
                y -= 20    # Mi abbasso di 20px
                self.c.setFont(STILE_TESTO, DIMENSIONE_TESTO)
                self.c.drawString(x, y, str(valore))   # Scrivo il testo
                y += 20    # Mi riposiziono all' altezza del titolo per scrivere il titolo successivo
                x += 200   # Mi sposto a destra di 200px per disegnare il prossimo elemento