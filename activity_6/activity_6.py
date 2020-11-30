import numpy as np
import ttg
import pandas as pd
from itertools import combinations


class Factorial2K:
    def __init__(self, valores_experimentos, num_variaveis):
        self.valores_experimentos = valores_experimentos
        self.num_variaveis = num_variaveis

    def calculate_q_values(self):
        tabela_verdade = self.get_table_truth()
        matriz_entradas = self.valores_experimentos
        r = matriz_entradas.shape[0]

        matriz_entradas = matriz_entradas.mean(axis=0)

        dict_qs = {}

        for column in tabela_verdade.columns:
            dict_qs["q" + column] = sum(
                (tabela_verdade[column] * matriz_entradas) / 2 ** num_variaveis
            )

        self.q_values = dict_qs

    def get_table_truth(self):
        lista_variaveis = []

        for a in range(self.num_variaveis):
            lista_variaveis.append(str(a))

        tabela_verdade = ttg.Truths(lista_variaveis)

        df_variaveis = pd.DataFrame(tabela_verdade.as_pandas())
        df_modificado = df_variaveis.replace(0, -1)

        colunas = df_modificado.columns

        n = 2

        while n <= num_variaveis:
            combinacoes = combinations(colunas, r=n)

            for combinacao in combinacoes:

                nome_multi = combinacao[0]
                multi = df_modificado[combinacao[0]].values

                for j in range(1, len(combinacao)):
                    nome_multi += combinacao[j]
                    multi *= df_modificado[combinacao[j]].values

                df_modificado[nome_multi] = multi

            n += 1

        return df_modificado

    def get_sst(self):
        soma_valores = sum([valor ** 2 for valor in self.q_values.values()])

        return (2 ** self.num_variaveis) * soma_valores

    def get_sse(self):
        valores_experimentos = self.valores_experimentos

        qtd_valores = valores_experimentos.shape[1]
        media_valores_experimentos = valores_experimentos.mean(axis=0)
        valores_experimentos = valores_experimentos.T

        valor_sse = 0

        for i in range(qtd_valores):
            valores_erros = valores_experimentos[i] - media_valores_experimentos[i]
            valor_sse += sum([valor ** 2 for valor in valores_erros])

        return valor_sse

    def get_porcao_variacao(self):
        valor_sst = self.get_sst()
        dict_valores = {}

        for q, valor in self.q_values.items():
            dict_valores[q] = (2 ** num_variaveis * valor ** 2) / valor_sst

        return dict_valores

    def get_q_values(self):
        return self.q_values


if __name__ == "__main__":
    num_variaveis = 3
    """
    valores_experimentos = np.array([[15,45,25,75],
                                    [18,48,28,75],
                                    [12,51,19,81]])
    """
    valores_experimentos = np.array([[14, 22, 10, 34, 46, 58, 50, 86]])

    factorial2K = Factorial2K(valores_experimentos, num_variaveis)
    factorial2K.calculate_q_values()
    
    print("Valores de Q:", factorial2K.get_q_values())
    print("SST:", factorial2K.get_sst())
    print("Porção Variação:", factorial2K.get_porcao_variacao())
    print("SSE:", factorial2K.get_sse())
