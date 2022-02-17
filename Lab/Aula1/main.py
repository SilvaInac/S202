from pato import Pato
from leao import Leao
from zoo import Zoologico

pato = Pato(nome="duck", idade=1, genero="M", corBico="Laranja")

leao = Leao(nome="dalva", genero="F", idade=2, selvagem=False)

animais = [pato, leao]

zoo = Zoologico(animais=animais)

print(zoo.getAnimais())