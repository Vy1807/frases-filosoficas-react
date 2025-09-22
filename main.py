#Logica padrão do site: 
'''
O usuário abre o link e se depara com a página inicial.
Essa página inicial terá um botão, uma caixa de texto com destaque e o nome do site em cima.
A funcionalidade principal é clicar no botão e receber uma frase nova a cada clique.
'''
import os
from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def cliquePrincipal():
    frases = {
        "Socrates": "A vida não examinada não vale a pena ser vivida.",
        "Platão": "Tente mover o mundo - o primeiro passo será mover a si mesmo.",
        "Platão": "Não espere por uma crise para descobrir o que é importante em sua vida.",
        "Platão": "O que faz andar o barco não é a vela enfunada, mas o vento que não se vê...",
        "Aristóteles": "O ignorante afirma, o sábio duvida, o sensato reflete.",
        "Sócrates" : "Só sei que nada sei.",
        "Platão" : "Onde não há igualdade, a amizade não perdura.",
        "Aristóteles" : "O homem é por natureza um animal político.",
        "René Descartes" : "Penso, logo existo.",
        "Immanuel Kant" : "Aja de tal forma que a máxima de sua ação possa ser universalizada.",
        "Friedrich Nietzsche" : "Aquilo que não me mata, me fortalece.",
        "Jean-Paul Sartre" : "A existência precede a essência.",
        "Simone de Beauvoir" : "Não se nasce mulher, torna-se mulher.",
        "Confúcio" : "Não importa o quão devagar você vá, desde que você não pare.",
        "Lao-Tsé" : "Uma jornada de mil quilômetros começa com um único passo.",
        "Sêneca" : "Enquanto adiamos, a vida se apressa.",
        "Epicuro" : "A morte não é nada para nós, pois, quando existimos, não existe a morte, e quando existe a morte, não existimos mais.",
        "Marco Aurélio" : "A felicidade da sua vida depende da qualidade dos seus pensamentos.",
        "Santo Agostinho" : "A medida do amor é amar sem medida.",
        "Tomás de Aquino" : "Cuidado com o homem de um só livro.",
        "Nicolau Maquiavel" : "Os fins justificam os meios.",
        "Thomas Hobbes" : "O homem é o lobo do homem.",
        "John Locke" : "Onde não há lei, não há liberdade.",
        "Voltaire" : "Não concordo com uma palavra do que dizes, mas defenderei até a morte o teu direito de dizê-la.",
        "Jean-Jacques Rousseau" : "O homem nasce livre, e por toda a parte encontra-se a ferros.",
        "Blaise Pascal" : "O coração tem razões que a própria razão desconhece.",
        "Baruch Spinoza" : "Não se lamente, não critique, mas compreenda.",
        "David Hume" : "A beleza das coisas existe no espírito de quem as contempla.",
        "Karl Marx" : "Os filósofos apenas interpretaram o mundo de diferentes maneiras; o que importa é transformá-lo.",
        "Søren Kierkegaard" : "A vida só pode ser compreendida, olhando-se para trás; mas só pode ser vivida, olhando-se para a frente.",
        "Arthur Schopenhauer" : "A vida é uma constante oscilação entre a ânsia de querer e o tédio de possuir.",
        "Heráclito" : "Ninguém pode entrar duas vezes no mesmo rio.",
        "Parmênides" : "O ser é e o não-ser não é.",
        "Demócrito" : "Tudo o que existe no universo é fruto do acaso e da necessidade.",
        "Francis Bacon" : "Saber é poder.",
        "Montesquieu" : "A liberdade é o direito de fazer tudo o que as leis permitem.",
        "John Stuart Mill" : "Sobre seu próprio corpo e mente, o indivíduo é soberano.",
        "Edmund Burke" : "Para que o mal triunfe, basta que os bons não façam nada.",
        "Georg Hegel" : "A história se repete, a primeira vez como tragédia e a segunda como farsa.",
        "Ludwig Wittgenstein" : "Sobre aquilo de que não se pode falar, deve-se calar.",
        "Martin Heidegger" : "A linguagem é a morada do ser.",
        "Albert Camus" : "A única questão filosófica realmente séria é o suicídio.",
        "Michel Foucault" : "O poder está em toda parte.",
        "Hannah Arendt" : "A essência dos Direitos Humanos é o direito a ter direitos.",
        "Ayn Rand" : "A menor minoria na Terra é o indivíduo. Aqueles que negam os direitos individuais não podem se dizer defensores das minorias.",
        "Bertrand Russell" : "O problema com o mundo é que os estúpidos são excessivamente confiantes, e os inteligentes são cheios de dúvidas.",
        "Karl Popper" : "Nenhuma quantidade de experimentos pode provar que estou certo; um único experimento pode provar que estou errado.",
        "Noam Chomsky" : "Se não acreditamos na liberdade de expressão para as pessoas que desprezamos, não acreditamos nela de forma alguma.",
        "Zygmunt Bauman" : "Vivemos em tempos líquidos. Nada foi feito para durar.",
        "Slavoj Žižek" : "Prefiro não ter o que quero do que ter o que não quero.",
        "Friedrich Nietzsche" : "Torna-te quem tu és.",
        "Platão" : "Tente mover o mundo – o primeiro passo será mover a si mesmo.",
        "Sócrates" : "Uma vida não examinada não vale a pena ser vivida.",
        "Aristóteles" : "A excelência é uma arte conquistada pelo treino e pelo hábito.",
        "Albert Camus" : "No meio do inverno, eu finalmente aprendi que havia em mim um verão invencível.",
        "Simone de Beauvoir" : "Que nada nos defina. Que nada nos sujeite. Que a liberdade seja a nossa própria substância.",
        "Jean-Paul Sartre" : "O inferno são os outros.",
        "René Descartes" : "A dúvida é a origem da sabidoria.",
        "Sêneca" : "A pressa é inimiga da perfeição.",
        "Epicuro" : "Não estrague o que você tem desejando o que não tem.",
        "Marco Aurélio" : "Você tem poder sobre sua mente, não sobre eventos externos. Perceba isso e você encontrará a força.",
        "Lao-Tsé" : "Aquele que conhece os outros é sábio; aquele que conhece a si mesmo é iluminado.",
        "Confúcio" : "Exige muito de ti e espera pouco dos outros. Assim, evitarás muitos aborrecimentos.",
        "Immanuel Kant" : "A experiência sem teoria é cega, mas a teoria sem experiência é mero jogo intelectual.",
        "Maquiavel" : "É melhor ser temido do que amado, se não se pode ser ambos.",
        "John Locke" : "A leitura fornece ao espírito materiais para o conhecimento, mas só o pensar faz nosso o que lemos.",
        "Voltaire" : "O preconceito é uma opinião sem julgamento.",
        "Thomas Hobbes" : "A curiosidade é a luxúria da mente.",
        "Jean-Jacques Rousseau" : "A paciência é amarga, mas seu fruto é doce.",
        "Baruch Spinoza" : "A paz não é a ausência de guerra, é uma virtude, um estado de espírito, uma disposição para a benevolência, confiança e justiça.",
        "Arthur Schopenhauer" : "O destino embaralha as cartas, e nós jogamos.",
        "Søren Kierkegaard" : "A angústia é a vertigem da liberdade.",
        "Heráclito" : "A única coisa que é constante é a mudança.",
        "Francis Bacon" : "A esperança é um bom café da manhã, mas uma péssima ceia.",
        "Montesquieu" : "Uma injustiça feita a um é uma ameaça feita a todos.",
        "David Hume" : "Um homem sábio adequa suas crenças às evidências.",
        "Karl Marx" : "A religião é o ópio do povo.",
        "Ludwig Wittgenstein" : "Os limites da minha linguagem significam os limites do meu mundo.",
        "Martin Heidegger" : "Todo homem nasce como muitos homens e morre como um só.",
        "Michel Foucault" : "O saber é o mais velho inimigo da fé.",
        "Hannah Arendt" : "O perdão é a chave para a ação e a liberdade.",
        "Ayn Rand" : "A pergunta não é quem vai me deixar; é quem vai me impedir.",
        "Bertrand Russell" : "Nunca morreria pelas minhas crenças, pois eu poderia estar errado.",
        "Noam Chomsky" : "A propaganda está para a democracia assim como o cassetete está para o estado totalitário.",
        "Zygmunt Bauman" : "A incerteza é o habitat natural da vida humana.",
        "Friedrich Nietzsche" : "Não existem fatos, apenas interpretações.",
        "Platão" : "A opinião é o meio-termo entre o conhecimento e a ignorância.",
        "Sócrates" : "Conhece-te a ti mesmo.",
        "Aristóteles" : "A felicidade é o sentido e o propósito da vida, o único objetivo e finalidade da existência humana.",
        "Albert Camus" : "A liberdade não é nada além de uma chance de ser melhor.",
        "Simone de Beauvoir" : "Viver é envelhecer, nada mais.",
        "Jean-Paul Sartre" : "O homem está condenado a ser livre.",
        "René Descartes" : "Para examinar a verdade, é necessário, uma vez na vida, colocar todas as coisas em dúvida, tanto quanto possível.",
        "Sêneca" : "Não é porque as coisas são difíceis que não ousamos; é porque não ousamos que elas são difíceis.",
        "Epicuro" : "O justo é o mais isento de perturbação; o injusto é o mais cheio de perturbação.",
        "Marco Aurélio" : "A melhor vingança é ser diferente daquele que te injuriou.",
        "Lao-Tsé" : "Domine os outros e seja forte. Domine a si mesmo e seja poderoso.",
        "Confúcio" : "O homem superior é modesto em seu discurso, mas excede em suas ações.",
        "Immanuel Kant" : "A ciência é o conhecimento organizado; a sabidoria é a vida organizada.",
        "Maquiavel" : "Nunca tente vencer pela força o que pode ser vencido pelo engano.",
        "John Locke" : "O que te preocupa, te escraviza.",
        "Voltaire" : "O senso comum não é tão comum.",
        "Thomas Hobbes" : "O lazer é a mãe da filosofia.",
        "Jean-Jacques Rousseau" : "A natureza nunca nos engana; somos sempre nós que nos enganamos.",
    }
    chave = (random.choice(list(frases.keys())))
    valor = (frases[chave])

    body = {
        "chave": chave,
        "valor": valor
    }

    return jsonify(body)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
