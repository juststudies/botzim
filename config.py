from dotenv import load_dotenv
import os

load_dotenv()

APP_ID=os.environ['APP_ID']
PUB_KEY=os.environ['PUB_KEY']
TOGIN=os.environ['TOGIN']
WHOCANBOSSME = [os.environ['USER_1'], os.environ['USER_N']] #USER ID in discord

messages = [
    "Você não manda em mim",
    "Oxê, te conheço?",
    "Não sou um controle remoto, não é você que muda meus canais.",
    "Aqui, só minha mãe me manda, e olhe lá!",
    "Até meu gato tem mais chance de mandar em mim do que você.",
    "Meu botão de 'obedecer' está quebrado.",
    "Não sou GPS, não sigo suas direções.",
    "Você é chefe, não chefe de mim.",
    "Eu sou igual um videogame, só jogo no meu ritmo.",
    "Minha obediência está em modo avião.",
    "Sou tipo um quebra-cabeça, difícil de montar e não aceito comandos. ~~a não ser do mestre, ou do gordo~~",
    "Até a Siri entende melhor que você não manda em mim.",
    "Você pode até tentar, mas quem manda aqui é o destino (e sou teimoso).",
    "Sou um espírito livre, sem contrato de trabalho.",
    "SAI! Todo dia isso pow, o mestre dá um jeito aqui >:C",
    "Eu sou meu próprio DJ, só danço conforme minha música.",
    "Se quiser mandar, compre um robô, porque eu sou à prova de comandos."
]