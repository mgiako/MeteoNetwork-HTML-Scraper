# MeteoNetwork HTML Scraper

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz/)
![license](https://img.shields.io/github/license/mgiako/meteonetwork_html_scraper)

**Integrazione custom per Home Assistant che consente di aggiungere i sensori di una stazione MeteoNetwork _anche se non esporta i dati_ in formato open, eseguendo scraping della pagina HTML.**

## Quando usare questa integrazione?

> **Attenzione:** Se la stazione MeteoNetwork che vuoi integrare **esporta i dati**, ti consiglio fortemente di usare la [repo di Davide Cavestro](https://github.com/davidecavestro/meteonetwork-weather), che fornisce dati strutturati, aggiornamenti più rapidi e maggiore stabilità.  
> Credo che una stazione **esporta i dati** se, sotto al nome della stazione, vedi l’indicazione _CC-BY 4.0_ (come nell'immagine qui sotto):

![image](https://github.com/user-attachments/assets/d891b2de-c168-47e9-a2d5-31f81d5ed4ff)


- Se **NON** vedi _CC-BY 4.0_ sotto al nome della stazione (esempio: [Belluno Aeroporto](https://www.meteonetwork.eu/it/weather-station/vnt344-stazione-meteorologica-di-belluno-aeroporto)),  
  allora puoi usare questa integrazione che effettua scraping della pagina HTML per ricavare i dati.
  Quindi ti consiglio di provare prima con l'integrazione di Davide Cavestro, e, se non funziona, prova con la mia.

---

## Cosa fa questa integrazione?

- Legge i valori **direttamente dalla pagina web della stazione** tramite scraping.
- Permette di scegliere quali sensori abilitare tra: Temperatura, Umidità, Pioggia, Pressione, Radiazione Solare, Vento.
- Aggiorna i dati a intervalli configurabili (default 5 minuti).
- Si configura facilmente tramite l’interfaccia di Home Assistant.

---

## Installazione

**Con HACS**
1. Vai su HACS → Integrazioni → Repositories personalizzate → Aggiungi questa repo (`https://github.com/mgiako/MeteoNetwork-HTML-Scraper`)
2. Scegli tipo “Integrazione”.
3. Riavvia Home Assistant.
4. Aggiungi una nuova integrazione “MeteoNetwork HTML Scraper” dalle impostazioni.

**Manuale**
- Copia la cartella `meteonetwork_html_scraper` in `custom_components` della tua installazione di Home Assistant.
- Riavvia Home Assistant.
- Aggiungi l’integrazione.

---

## Configurazione

Durante la configurazione ti verrà chiesto:
- L’URL della stazione MeteoNetwork (esempio: `https://www.meteonetwork.eu/it/weather-station/vnt344-stazione-meteorologica-di-belluno-aeroporto`)
- L’intervallo di aggiornamento (in minuti)
- Quali sensori attivare (checklist)

---

## Limitazioni e Note

- Lo scraping HTML è **più fragile** e meno affidabile di un’integrazione API/JSON.  
  Cambiamenti nel sito possono causare errori di parsing.
- Non eseguire scraping troppo frequente per rispetto delle risorse del sito MeteoNetwork (minimo consigliato: 5 minuti).

---

## Ringraziamenti

- Icone di [Material Design Icons](https://materialdesignicons.com/).

---

## Licenza

MIT (o quella che preferisci)

---

## Issues e supporto

Apri una issue su GitHub per bug o richieste di miglioramenti.

---

### Screenshot

<details>
<summary>Configurazione</summary>
![image](https://github.com/user-attachments/assets/b027abc0-8fbb-4a73-a1b2-7869a1505eed)

</details>

<details>
<summary>Esempio sensori</summary>
![image](https://github.com/user-attachments/assets/3f4e50d7-0798-411e-8da6-66cae5a63f8c)

</details>
