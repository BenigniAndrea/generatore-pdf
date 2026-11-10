from pydantic import BaseModel  # Per le classi BaseModel
from typing import List         # Per i dati costituiti da una o più liste

# Classi BaseModel tipizzate per la gestione dei dati
class Feature(BaseModel):  
    feature1: str
    feature2: str

class Kickoff(BaseModel):
    nome_progetto: str
    codice_progetto: str
    cliente: str
    descrizione: str
    finalita: str
    ambito: str
    definizioni_generali: str
    stakeholders: List[str]
    overview_funzionale: str
    features: List[Feature]
    dati_necessari: str
    requisiti_performance: str
    requisiti_sicurezza: str
    requisiti_usabilita: str
    requisiti_affidabilita: str
    requisiti_scalabilita: str
    architettura: str
    moduli: str
    assunzioni: List[str]
    vincoli: List[str]