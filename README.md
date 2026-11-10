SPIEGAZIONE PROGETTO: 
Il progetto ha come scopo quello di generare automaticamente documenti PDF strutturati a 
partire da dati organizzati, combinando validazione degli input, formattazione e 
automazione. Utilizza Python come linguaggio principale, integrato con librerie come 
Pydantic per la validazione dei dati e ReportLab per la creazione dinamica di PDF. I dati del 
progetto, definiti in un file JSON, includono campi come nome del progetto, cliente, 
descrizioni, requisiti tecnici, stakeholder e vincoli. Questi dati vengono prima validati tramite 
modelli Pydantic, che garantiscono la correttezza dei tipi e la presenza di campi obbligatori, 
evitando errori comuni durante la compilazione. 
Il cuore del sistema risiede nella classe “DocumentoPDF” (definita in Template6.py), che 
coordina la generazione del PDF. Questa classe inizializza un canvas di ReportLab, 
serializza i dati validati in JSON e utilizza metodi della classe “PDFmanager” (in 
pdf_manager.py) per posizionare elementi grafici e testuali nel documento. Il “PDFmanager” 
gestisce l’impaginazione con precisione, aggiungendo intestazioni con logo aziendale, titoli 
in grassetto, elenchi puntati, linee divisorie e sezioni dinamiche come "Requisiti" o "Vincoli". 
Le coordinate degli elementi (es. HEIGHT - 170) sono predefinite per mantenere un layout 
coerente, mentre la numerazione delle pagine e la creazione di nuove pagine vengono 
gestite automaticamente. 
Il template del PDF (Template6.pdf) è suddiviso in tre pagine principali: la prima contiene 
informazioni generali del progetto, la seconda focalizza su requisiti tecnici e architettura, e la 
terza elenca vincoli e assunzioni. Elementi fissi come il logo e l’intestazione "AISENT s.r.l." 
compaiono in ogni pagina, assicurando un’identità visiva uniforme. L’esecuzione avviene 
tramite un Jupyter Notebook (test.ipynb), dove l’utente definisce i dati in un oggetto Kickoff, 
avvia la generazione del PDF e verifica il risultato finale. 
I vantaggi principali includono l’automazione di processi ripetitivi per la creazione di PDF 
personalizzati, la riduzione di errori umani grazie alla validazione Pydantic e la possibilità di 
personalizzare il template senza modificare la logica sottostante. Il sistema è ideale per 
contesti aziendali che richiedono documenti standardizzati (come in questo caso per 
l’azienda AISENT s.r.l.). 
TECNOLOGIE E LINGUAGGI USATI: 
1. Python: Linguaggio principale per la logica di generazione. 
2. ReportLab: Libreria per creare e manipolare file PDF. 
3. Pydantic: Libreria per la validazione e serializzazione dei dati. 
4. JSON: Formato per lo storage strutturato dei dati. 
5. Jupyter Notebook: Un ambiente interattivo, non essenziale, per eseguire, testare e 
visualizzare il processo di generazione del file PDF in modo intuitivo. 
PASSAGGI PER GENERARE IL FILE PDF SECONDO IL TEMPLATE 
FORNITO: 
Per prima cosa assicurarsi di avere installato sulla macchina la versione più recente di 
Python, dopodiché, aprire il terminale e installare i pacchetti necessari: 
● py -m pip install pydantic jupyterlab python-dotenv    # Dipendenze base 
● py -m pip install reportlab                                            
# Per la generazione di PDF 
Una volta fatto ciò è possibile eseguire il Jupyter Notebook “test.ipynb” su un editor come VS 
Code (assicurarsi di aver installato le estensioni per Python e Jupyter sull’editor).  
In questo caso, verrà generato un file PDF, all’interno della directory del progetto, in base al 
template “template6.py”, compilato con i dati forniti nel file JSON. 
OBBIETTIVI FUTURI: 
Creazione di un’applicazione web che permetta agli utenti di compilare dei campi dati e 
ottenere un file PDF contenente tali dati disposti secondo il template selezionato.
