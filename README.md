# MeteoNetwork HTML Scraper

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz/)
![license](https://img.shields.io/github/license/mgiako/meteonetwork-html-scraper)

**Custom integration for Home Assistant that allows you to add sensors from a MeteoNetwork station ([station list](https://www.meteonetwork.eu/it/stations-list)), especially when the station does *not* normally export data via the API.**

**In such cases, this integration retrieves the data by scraping the station’s HTML page.**

---

## When should you use this integration?

> **Warning:** If the MeteoNetwork station you want to add **exports its data**, I strongly recommend using [Davide Cavestro’s repository](https://github.com/davidecavestro/meteonetwork-weather), which provides structured data, faster updates, and more stability.  
> I believe a station **exports data** if you see the _CC-BY 4.0_ notice below the station’s name (as in the example below):
![image](https://github.com/user-attachments/assets/d891b2de-c168-47e9-a2d5-31f81d5ed4ff)

> If you **do NOT** see _CC-BY 4.0_ below the station’s name, like in the image below,  
> then you can use this integration, which scrapes the HTML page to get the data.  
> So, I recommend trying Davide Cavestro’s integration first, and if it doesn’t work, try this one.
![image](https://github.com/user-attachments/assets/c6ddd598-9c63-4313-95c9-10869273d7c9)

---

## What does this integration do?

- Reads values **directly from the station’s web page** via scraping.
- Allows you to choose which sensors to enable: Temperature, Humidity, Rain, Pressure, Solar Radiation, Wind.
- Updates data at configurable intervals (default: 5 minutes).
- Easy setup through the Home Assistant interface.

---

## Installation

**With HACS**
1. Go to HACS → Integrations → Custom repositories → Add this repo (`https://github.com/mgiako/MeteoNetwork-HTML-Scraper`)
2. Choose type “Integration”.
3. Restart Home Assistant.
4. Add the “MeteoNetwork HTML Scraper” integration from the settings.

**Manual**
- Copy the `meteonetwork_html_scraper` folder into the `custom_components` directory of your Home Assistant installation.
- Restart Home Assistant.
- Add the integration from the settings.

---

## Configuration

During configuration you will be asked for:
- The URL of the MeteoNetwork station (example: `https://www.meteonetwork.eu/it/weather-station/vnt344-stazione-meteorologica-di-belluno-aeroporto`)
- The update interval (in minutes)
- Which sensors to enable (checklist)

---

## Limitations & Notes

- HTML scraping is **more fragile** and less reliable than an API/JSON-based integration.  
  Changes to the website may break parsing.
- Do not scrape too frequently out of respect for MeteoNetwork’s resources (minimum recommended: every 5 minutes).
- Check the station’s historical data to see how often it updates and configure the refresh accordingly.

---

## Acknowledgements

- Icons by [Material Design Icons](https://materialdesignicons.com/).

---

## License

MIT (or any you prefer)

---

## Issues & Support

Open an issue on GitHub for bugs or feature requests.

---

### Screenshots

**Configuration**

![image](https://github.com/user-attachments/assets/b027abc0-8fbb-4a73-a1b2-7869a1505eed)

**Sensors Example**

![image](https://github.com/user-attachments/assets/3f4e50d7-0798-411e-8da6-66cae5a63f8c)
