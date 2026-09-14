import os
import warnings
import logging
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"
warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.ERROR)
logging.getLogger().setLevel(logging.ERROR)
from dotenv import load_dotenv
load_dotenv()

import os  
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

chave_api = os.getenv("GOOGLE_API_KEY")
mensagens = [
    SystemMessage("Traduza o texto a seguir para inglês"),
HumanMessage("Olá, como você está?"),
]
modelo = ChatGoogleGenerativeAI(model="gemini-3.6-flash", google_api_key=chave_api)
parser = StrOutputParser()
chain = modelo | parser
resposta_bruta = modelo.invoke(mensagens)
if isinstance(resposta_bruta.content, list) and len(resposta_bruta.content) > 0:
    texto_traduzido = resposta_bruta.content[0].get("text", "")
else:
    texto_traduzido = resposta_bruta.content

template_mensagem = ChatPromptTemplate.from_messages([
    ("system", "Traduza o texto a seguir para {idioma}"),
    ("user", "{texto}"),
])
# print(template_mensagem.invoke({"idioma": "inglês", "texto": "Estou bem, e você?"}))

cadeia_dinamica = template_mensagem | modelo | parser
resultado = cadeia_dinamica.invoke({"idioma": "inglês", "texto": "Estou bem, e você?"})

print("nova tradução da cadeia:", resultado)






