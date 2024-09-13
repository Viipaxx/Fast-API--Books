import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

uri = os.getenv('MONGO_URI')  # Recupera o URI seguro da variável de ambiente
client = MongoClient(uri)

api = client['API']  # Banco de dados
books = api['books']  # Coleção