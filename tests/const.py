"""Constants for tests."""

from homeassistant.const import (
    CONF_LATITUDE,
    CONF_LONGITUDE,
    CONF_NAME,
    CONF_SHOW_ON_MAP,
)

from custom_components.gismeteo.const import CONF_ADD_SENSORS

TEST_NAME = "Home"
TEST_UNIQUE_ID = "test_id"
TEST_LATITUDE = 55.55
TEST_LONGITUDE = 122.12

TEST_CONFIG = {
    CONF_NAME: TEST_NAME,
    CONF_LATITUDE: TEST_LATITUDE,
    CONF_LONGITUDE: TEST_LONGITUDE,
}

TEST_CONFIG_OPTIONS = {
    CONF_ADD_SENSORS: True,
}

TEST_CONFIG_YAML = {
    "home": {
        CONF_NAME: TEST_NAME,
        CONF_LATITUDE: TEST_LATITUDE,
        CONF_LONGITUDE: TEST_LONGITUDE,
        CONF_ADD_SENSORS: True,
        CONF_SHOW_ON_MAP: False,
    },
}
