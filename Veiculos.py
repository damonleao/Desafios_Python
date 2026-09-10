# Classe que representa um veículo
class Veiculo:

    # Método construtor
    def __init__(self, placa, marca, modelo, ano, cor):

        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    # Método que mostra a descrição do veículo
    def exibir_dados(self):
        print("-----------------------------")
        print("Placa:", self.placa)
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)
        print("Cor:", self.cor)


# Lista que vai armazenar os veículos cadastrados
veiculos = []

# Variável para controlar o while
continuar = "sim"

# Enquanto o usuário quiser cadastrar
while continuar == "sim":

    print("\n===== CADASTRO DE VEÍCULO =====")

    # Pedindo os dados ao usuário
    placa = input("Digite a placa: ")
    marca = input("Digite a marca: ")
    modelo = input("Digite o modelo: ")
    ano = input("Digite o ano: ")
    cor = input("Digite a cor: ")

    # Criando um objeto Veiculo
    veiculo = Veiculo(
        placa,
        marca,
        modelo,
        ano,
        cor
    )

    # Adicionando o veículo na lista
    veiculos.append(veiculo)

    # Perguntando se deseja cadastrar outro
    continuar = input(
        "\nDeseja cadastrar outro veículo? (sim/não): "
    ).lower()


# Exibindo o resultado final
print("\n===================================")
print("       RELATÓRIO DE VEÍCULOS")
print("===================================")

# Mostrando a quantidade de veículos cadastrados
print("Quantidade de veículos cadastrados:", len(veiculos))

# Mostrando a descrição de cada veículo
for i, veiculo in enumerate(veiculos, start=1):
    print("\nVeículo", i)
    veiculo.exibir_dados()

print("\nFim do programa!")
