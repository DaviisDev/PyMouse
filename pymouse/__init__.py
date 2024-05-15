from .utils import log
from pymouse.config import Config
from pymouse.client import PyMouse, START_TIME
from pymouse.database.modules import DataBase


log.info("Compiling DataBase...")
try:
    db = DataBase()
except Exception:
    log.info("Error in compiling DataBase...")
    exit()
log.info("DataBase compiled with sucessfully...")


# if use database input here
from pymouse.database.plugins.utilities import (
    usersmodel_db, # Use in decorator with others...
    afkmodel_db, # Use in modules with use a afk function's, WARNING: This uses the usersmodel_db function so always keep your import below this module.
)
from pymouse.decorators import Decorators