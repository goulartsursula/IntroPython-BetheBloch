"""
Projeto: Interação da radiação com a matéria através da equação de Bethe-Bloch
Autores: Gabriela Gonçalves, Úrsula Goulart e Victor Soeiro.
Última atualização: 14/11/2020

Comentários:
# A estrutura desse projeto foi pensado como um módulo, separando o projeto em pequenas partes para um melhor
entendimento dele. Foi criado um arquivo utils que contém funções usadas frequentemente e para a
verificação dos tipos de dados aceitáveis. E, também, foi criado um arquivo contants que contém todos as
constantes dadas pelo PDG no projeto.

# A pasta Tests contém todos os testes de cada um dos passos dos projetos e outros, que verificação e avaliarão
a lógica utilizada para os tipos de dados aceitáveis.
"""
import matplotlib.pyplot as plt

from Bethe_Bloch.utils import *
from Bethe_Bloch.constants import *


@func_argument_decorator
def gamma(beta):
    """
    Retorna o fator de Lorentz dado a velocidade relativa de um objeto à velocidade da luz.

    :param beta: Velocidade relativa de um objeto à velocidade da luz.
    :return: Fator de Lorentz.
    """
    return 1 / np.sqrt(1 - np.power(beta, 2))


@func_argument_decorator
def get_beta(beta_gamma):
    """
    Usando a propriedade

    gamma^2 = (gamma * beta)^2 + 1

    retorna o valor de beta dado o seu produto com gamma.

    :param beta_gamma: Produto de Gamma e Beta.
    :return: Beta.
    """
    return beta_gamma / np.sqrt(np.power(beta_gamma, 2) + 1)


@func_argument_decorator
def ln_argument(beta_gamma):
    """
     Calcula o argumento do logaritmo natural da função de Bethe-Bloch.

     :param beta_gamma: O produto de beta e gamma.
     :return: O argumento do logaritmo natural da função de Bethe-Bloch
     """
    return 2 * m_e * np.power(beta_gamma, 2) / e_I


@func_argument_decorator
def brackets_argument(beta_gamma):
    return np.log(ln_argument(beta_gamma)) - np.power(get_beta(beta_gamma), 2)


@func_argument_decorator
def bethe_bloch(beta_gamma):
    return K * p * np.power(z, 2) * (Z/A) * (1/np.power(get_beta(beta_gamma), 2)) * brackets_argument(beta_gamma)


x = np.linspace(0.1, 100, 1000)
y = -bethe_bloch(x)

plt.loglog(x, y)
plt.show()
