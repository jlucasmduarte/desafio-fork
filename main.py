"""
Desafio: Criar uma calculadora estatística simples em Python

Tarefa:
Implemente as funções abaixo para calcular média, mediana e moda de uma lista de números.

Instruções:
1. Faça o fork deste repositório no seu GitHub.
2. Clone o seu fork para sua máquina.
3. Complete as funções abaixo.
4. Teste o código executando: python calculadora_estatistica.py
5. Envie um Pull Request com a sua solução.

💡 Dica: não use bibliotecas externas como numpy ou statistics.
"""

# Função para calcular a média
def calcular_media(lista):
    # TODO: implementar a soma dos elementos e dividir pelo tamanho da lista
    if not lista:
        return 0
    return sum(lista) / len(lista)


# Função para calcular a mediana
def calcular_mediana(lista):
    # TODO: ordenar a lista e encontrar o elemento do meio
    # 💡 Dica: se o tamanho for par, tire a média dos dois elementos centrais
    # 1. Ordenar a lista
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    
    # 2. Verificar se o número de elementos é ímpar ou par
    if n % 2 == 1:
        # Se ímpar, a mediana é o elemento do meio
        indice_meio = n // 2
        mediana = lista_ordenada[indice_meio]
    else:
        # Se par, a mediana é a média dos dois elementos do meio
        indice1 = n // 2 - 1
        indice2 = n // 2
        mediana = (lista_ordenada[indice1] + lista_ordenada[indice2]) / 2
        
    return mediana


# Função para calcular a moda
def calcular_moda(lista):
    # TODO: encontrar o valor que mais aparece
    # 💡 Dica: use um dicionário para contar as ocorrências
    if not lista:
        return "A lista de dados está vazia."

    # Usar um dicionário para armazenar a contagem de frequência de cada elemento
    contagem_frequencia = {}
    for elemento in lista:
        if elemento in contagem_frequencia:
            contagem_frequencia[elemento] += 1
        else:
            contagem_frequencia[elemento] = 1

    # Encontrar a frequência máxima
    frequencia_maxima = 0
    for elemento in contagem_frequencia:
        if contagem_frequencia[elemento] > frequencia_maxima:
            frequencia_maxima = contagem_frequencia[elemento]
            
    # Encontrar todos os elementos que têm a frequência máxima (caso bimodal/multimodal)
    modas = []
    for elemento in contagem_frequencia:
        if contagem_frequencia[elemento] == frequencia_maxima:
            modas.append(elemento)
            
    return modas


def main():
    try:
        numeros = [10, 20, 20, 30, 40, 40, 40, 50]

        print("📊 Calculadora Estatística")
        print(f"Lista de números: {numeros}")
        print(f"Média: {calcular_media(numeros)}")
        print(f"Mediana: {calcular_mediana(numeros)}")
        print(f"Moda: {calcular_moda(numeros)}")

    except Exception as e:
        print(f"⚠️ Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()
