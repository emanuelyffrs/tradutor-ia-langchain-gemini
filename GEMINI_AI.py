import os; GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
from ia_tradutora import modelo, mensagens; resposta = modelo.invoke(mensagens)
