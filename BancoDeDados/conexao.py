import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath((__file__)))
DB_PATH = os.path.join(BASE_DIR,'Motoboy-Finacias.db')

def get_conexao():
    return sqlite3.connect(DB_PATH)