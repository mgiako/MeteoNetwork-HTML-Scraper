"""Integrazione MeteoNetwork HTML Scraper."""
from __future__ import annotations

async def async_setup_entry(hass, entry):
    """Setup tramite config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True

async def async_unload_entry(hass, entry):
    """Unload della config entry."""
    return await hass.config_entries.async_unload_platforms(entry, ["sensor"])
