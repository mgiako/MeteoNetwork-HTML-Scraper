"""Config flow per MeteoNetwork HTML Scraper."""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers import config_validation as cv

DOMAIN = "meteonetwork_html_scraper"

SENSORS = [
    ("temperatura", "Temperatura"),
    ("umidita", "Umidità"),
    ("pioggia", "Pioggia"),
    ("pressione", "Pressione"),
    ("radiazione_solare", "Radiazione solare"),
    ("vento", "Vento"),
]

class MeteoNetworkHTMLScraperConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gestisce il flusso di configurazione."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            if not user_input.get("url", "").startswith("http"):
                errors["url"] = "invalid_url"
            if user_input.get("refresh_minutes", 0) <= 0:
                errors["refresh_minutes"] = "invalid_refresh"
            if not user_input.get("sensors"):
                errors["sensors"] = "no_sensors"
            if not errors:
                return self.async_create_entry(
                    title="MeteoNetwork HTML Scraper",
                    data=user_input
                )

        data_schema = vol.Schema({
            vol.Required("url"): str,
            vol.Required("refresh_minutes", default=5): int,
            vol.Required(
                "sensors",
                default=[s[0] for s in SENSORS]
            ): cv.multi_select({s[0]: s[1] for s in SENSORS})
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )
