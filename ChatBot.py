import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

chave_api = "c68d33300baedbcb147bc99ceb670107"
analise = SentimentIntensityAnalyzer()

def sugerir_filmes():
      frase = input("Como está se sentindo agora?")
      emocao = analise.polarity_scores(frase)['compound']
      #retorna um valor que coincide com o sentimento da pessoa naquele momento
      print(emocao)

      if emocao <= -0.5:
         genero =  "18" #romance
      elif emocao >= 0 and emocao <=0:
         genero = "107" #drama
      elif emocao >= 0.5:
         genero = "70" #comedia
      else:
         genero = "27" #terrorb

sugerir_filmes()
#chamando a função de sugestão