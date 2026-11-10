from pdf_manager import *      # Importo le librerie e le classi di PDFmanager
from modelloPydantic import *  # Importo le librerie e le classi di modelloPydantic

# Contiene i metodi per la creazione del template e del documento pdf vero e proprio
class DocumentoPDF: 
    # Costruttore a cui viene passato il nome che si vuole dare al file e i dati nel kickoff
    def __init__(self, nomeFile, kickoff):
        self.nomeFile = nomeFile
        self.c = canvas.Canvas(nomeFile, pagesize=letter)   # Crea il canva su cui verranno scritti gli elementi del pdf
        self.kickoff = kickoff

        # Serializzazione del modello pydantic in JSON
        json_output = kickoff.model_dump_json(indent=2)

        # Scrittura del file JSON
        with open('dati.json', 'w', encoding='utf-8') as f:
            f.write(json_output) 
        
        # Apertura del file JSON
        with open('dati.json', 'r') as file:
          self.dati = json.load(file)
    
    # Creazione del template
    def createTemplate(self):
        impaginazione = PDFmanager(self.c, self.dati)   
  
        # Aggiunta di tutti gli elementi che compongono il file PDF
        impaginazione.aggiungiIntestazione(80, HEIGHT - 100, "immagine1.png", 200, 50, "PROGETTO FUNZIONALE")
        impaginazione.aggiungiLineaRetta(80, WIDTH - 80, HEIGHT - 150)
        impaginazione.aggiungiTitolo(80, HEIGHT - 170, "NOME PROGETTO")
        impaginazione.aggiungiContenuto(80, HEIGHT - 190, self.dati['nome_progetto'])  
        impaginazione.aggiungiLineaRetta(80, WIDTH - 80, HEIGHT - 210)
        impaginazione.aggiungiTitoloConTesto(80, HEIGHT - 230, "CODICE PROGETTO", self.dati['codice_progetto'])
        impaginazione.aggiungiTitoloConTesto(80, HEIGHT - 260, "CLIENTE", self.dati['cliente'])
        impaginazione.aggiungiLineaRetta(80, WIDTH - 80, HEIGHT - 280)
        impaginazione.aggiungiTitolo(80, HEIGHT - 300, "DESCRIZIONE")
        impaginazione.aggiungiContenuto(80, HEIGHT - 320, self.dati['descrizione']) 
        impaginazione.aggiungiTitolo(80, HEIGHT - 360, "FINALITÀ")
        impaginazione.aggiungiContenuto(80, HEIGHT - 380, self.dati['finalita']) 
        impaginazione.aggiungiTitolo(80, HEIGHT - 420, "AMBITO")
        impaginazione.aggiungiContenuto(80, HEIGHT - 440, self.dati['ambito']) 
        impaginazione.aggiungiTitolo(80, HEIGHT - 480, "DEFINIZIONI GENERALI")
        impaginazione.aggiungiContenuto(80, HEIGHT - 500, self.dati['definizioni_generali']) 
        impaginazione.aggiungiTitolo(80, HEIGHT - 540, "STAKEHOLDERS")
        impaginazione.aggiungiElenchiPuntatiOrizzontali(100, HEIGHT - 570, self.dati['stakeholders'])
        impaginazione.aggiungiLineaRetta(80, WIDTH - 80, HEIGHT - 600)
        impaginazione.aggiungiTitolo(80, HEIGHT - 640, "OVERVIEW FUNZIONALE")
        impaginazione.aggiungiContenuto(80, HEIGHT - 660, self.dati['overview_funzionale']) 
        impaginazione.aggiungiTitolo(80, HEIGHT - 700, "FEATURES")
        impaginazione.aggiungiElencoOrizzontale(100, HEIGHT - 730, self.dati['features'])
        impaginazione.aggiungiPagina()
        impaginazione.aggiungiIntestazione(80, HEIGHT - 100, "immagine1.png", 200, 50, "PROGETTO FUNZIONALE")
        impaginazione.aggiungiTitolo(80, HEIGHT - 140, "DATI NECESSARI")
        impaginazione.aggiungiContenuto(80, HEIGHT - 160, self.dati['dati_necessari'])
        impaginazione.aggiungiLineaRetta(80, WIDTH - 80, HEIGHT - 200)
        impaginazione.aggiungiTitolo(80, HEIGHT - 240, "REQUISITI DI PERFORMANCE")
        impaginazione.aggiungiContenuto(80, HEIGHT - 260, self.dati['requisiti_performance']) 
        impaginazione.aggiungiTitolo(80, HEIGHT - 300, "REQUISITI DI SICUREZZA")
        impaginazione.aggiungiContenuto(80, HEIGHT - 320, self.dati['requisiti_sicurezza'])  
        impaginazione.aggiungiTitolo(80, HEIGHT - 360, "REQUISITI DI USABILITÀ")
        impaginazione.aggiungiContenuto(80, HEIGHT - 380, self.dati['requisiti_usabilita']) 
        impaginazione.aggiungiTitolo(80, HEIGHT - 420, "REQUISITI DI AFFIDABILITÀ")
        impaginazione.aggiungiContenuto(80, HEIGHT - 440, self.dati['requisiti_affidabilita']) 
        impaginazione.aggiungiTitolo(80, HEIGHT - 480, "REQUISITI DI SCALABILITÀ")
        impaginazione.aggiungiContenuto(80, HEIGHT - 500, self.dati['requisiti_scalabilita']) 
        impaginazione.aggiungiLineaRetta(80, WIDTH - 80, HEIGHT - 520)
        impaginazione.aggiungiTitolo(80, HEIGHT - 550, "ARCHITETTURA")
        impaginazione.aggiungiContenuto(80, HEIGHT - 570, self.dati['architettura']) 
        impaginazione.aggiungiTitolo(80, HEIGHT - 610, "MODULI")
        impaginazione.aggiungiContenuto(80, HEIGHT - 630, self.dati['moduli']) 
        impaginazione.aggiungiLineaRetta(80, WIDTH - 80, HEIGHT - 660)
        impaginazione.aggiungiTitolo(80, HEIGHT - 690, "ASSUNZIONI")
        impaginazione.aggiungiElencoPuntato(100, HEIGHT - 720, self.dati['assunzioni'])
        impaginazione.aggiungiPagina()
        impaginazione.aggiungiIntestazione(80, HEIGHT - 100, "immagine1.png", 200, 50, "PROGETTO FUNZIONALE")
        impaginazione.aggiungiTitolo(80, HEIGHT - 140, "VINCOLI")
        impaginazione.aggiungiElencoPuntato(100, HEIGHT - 170, self.dati['vincoli'])

    def createPdf(self):
        self.createTemplate()
        self.c.save()
