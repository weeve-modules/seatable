from os import getenv

PARAMS = {
    "API_TOKEN": getenv("API_TOKEN", ""),
    "TABLE": getenv("TABLE", ""),
}
