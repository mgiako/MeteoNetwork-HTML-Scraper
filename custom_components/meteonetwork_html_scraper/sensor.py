"""Sensore per MeteoNetwork HTML Scraper."""
import logging
from datetime import timedelta
from homeassistant.helpers.entity import Entity
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator
from homeassistant.helpers.device_registry import DeviceInfo

import requests
from bs4 import BeautifulSoup
import re

_LOGGER = logging.getLogger(__name__)

SENSOR_TYPES = {
    "temperatura": {
        "name": "Temperatura",
        "unit": "°C",
        "icon": "mdi:thermometer"
    },
    "umidita": {
        "name": "Umidità",
        "unit": "%",
        "icon": "mdi:water-percent"
    },
    "pioggia": {
        "name": "Pioggia",
        "unit": "mm",
        "icon": "mdi:weather-rainy"
    },
    "pressione": {
        "name": "Pressione",
        "unit": "hPa",
        "icon": "mdi:gauge"
    },
    "radiazione_solare": {
        "name": "Radiazione solare",
        "unit": "W/m²",
        "icon": "mdi:white-balance-sunny"
    },
    "vento": {
        "name": "Vento",
        "unit": "km/h",
        "icon": "mdi:weather-windy"
    }
}

def extract_station_name(url: str) -> str:
    # Ottiene la parte finale del link dopo "weather-station/"
    match = re.search(r"weather-station/([^/]+)", url)
    if match:
        return match.group(1).replace("-", " ").capitalize()
    return "Stazione Meteo"

async def async_setup_entry(hass, entry, async_add_entities):
    url = entry.data["url"]
    refresh = int(entry.data.get("refresh_minutes", 5))
    sensors = entry.data.get("sensors", list(SENSOR_TYPES.keys()))
    station_name = extract_station_name(url)

    coordinator = MeteoNetworkCoordinator(hass, url, refresh, sensors)
    await coordinator.async_config_entry_first_refresh()

    entities = [
        MeteoNetworkSensor(coordinator, sensor_type, station_name)
        for sensor_type in sensors
    ]
    async_add_entities(entities, True)

class MeteoNetworkCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, url, refresh, sensors):
        super().__init__(
            hass,
            _LOGGER,
            name="MeteoNetwork HTML Scraper",
            update_interval=timedelta(minutes=refresh),
        )
        self.url = url
        self.sensors = sensors
        self.data = {}

    def _extract_value(self, soup, label, pattern, fallback_div=None):
        # Cerca nello span
        for span in soup.find_all("span", class_="c_head"):
            if label in span.text:
                testo = span.get_text(separator="\n")
                match = re.search(pattern, testo)
                if match:
                    return match.group(1)
        # Per radiazione solare
        if fallback_div:
            for div in soup.find_all("div", class_="card-header"):
                if fallback_div in div.text:
                    p = div.find_next("p", class_="card-text")
                    if p:
                        match = re.search(pattern, p.text)
                        if match:
                            return match.group(1)
        return None

    async def _async_update_data(self):
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            # FIX: usa executor per la richiesta bloccante
            response = await self.hass.async_add_executor_job(
                lambda: requests.get(self.url, headers=headers, timeout=15)
            )
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            results = {}

            if "temperatura" in self.sensors:
                value = self._extract_value(soup, "Temperatura", r"([\d.,]+)\s*[°]C")
                results["temperatura"] = float(value.replace(",", ".")) if value else None
            if "umidita" in self.sensors:
                value = self._extract_value(soup, "Umidità", r"([\d.,]+)\s*%")
                results["umidita"] = float(value.replace(",", ".")) if value else None
            if "pioggia" in self.sensors:
                value = self._extract_value(soup, "Pioggia", r"([\d.,]+)\s*mm")
                results["pioggia"] = float(value.replace(",", ".")) if value else None
            if "pressione" in self.sensors:
                value = self._extract_value(soup, "Pressione", r"([\d.,]+)\s*hPa")
                results["pressione"] = float(value.replace(",", ".")) if value else None
            if "radiazione_solare" in self.sensors:
                value = self._extract_value(soup, "", r"([\d.,]+)\s*W/m", fallback_div="Radiazione solare")
                results["radiazione_solare"] = float(value.replace(",", ".")) if value else None
            if "vento" in self.sensors:
                value = self._extract_value(soup, "Vento", r"([\d.,]+)\s*km/h")
                results["vento"] = float(value.replace(",", ".")) if value else None

            return results
        except Exception as e:
            _LOGGER.error(f"Errore aggiornando dati MeteoNetwork: {e}")
            return {}


class MeteoNetworkSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, sensor_type, station_name):
        super().__init__(coordinator)
        self._sensor_type = sensor_type
        self._station_name = station_name
        self._attr_name = f"{SENSOR_TYPES[sensor_type]['name']} {station_name}"
        self._attr_icon = SENSOR_TYPES[sensor_type]["icon"]
        self._attr_native_unit_of_measurement = SENSOR_TYPES[sensor_type]["unit"]
        self._attr_unique_id = f"meteonetwork_{station_name}_{sensor_type}"

        self._attr_device_info = DeviceInfo(
            identifiers = {("meteonetwork_html_scraper", station_name)},
            name = f"MeteoNetwork {station_name}",
            manufacturer = "MeteoNetwork",
            model = "Web HTML Scraper",
            entry_type = "service"
        )

    @property
    def native_value(self):
        return self.coordinator.data.get(self._sensor_type)

    @property
    def available(self):
        return self.coordinator.data.get(self._sensor_type) is not None
