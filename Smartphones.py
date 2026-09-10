# Classe que representa um Smartphone
class Smartphone:

    # Método construtor
    def __init__(self, marca, modelo, armazenamento, cor,
                 sistema_operacional, preco, fabricante, ano_fabricacao):

        self.marca = marca
        self.modelo = modelo
        self.armazenamento = armazenamento
        self.cor = cor
        self.sistema_operacional = sistema_operacional
        self.preco = preco
        self.fabricante = fabricante
        self.ano_fabricacao = ano_fabricacao

    # Método que mostra a descrição do smartphone
    def exibir_dados(self):
        print("-----------------------------")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Armazenamento:", self.armazenamento)
        print("Cor:", self.cor)
        print("Sistema Operacional:", self.sistema_operacional)
        print("Preço: R$", self.preco)
        print("Fabricante:", self.fabricante)
        print("Ano de Fabricação:", self.ano_fabricacao)


# Lista que vai armazenar os smartphones cadastrados
smartphones = []

# Variável para controlar o while
continuar = "sim"

# Enquanto o usuário quiser cadastrar
while continuar == "sim":

    print("\n===== CADASTRO DE SMARTPHONE =====")

    # Pedindo os dados ao usuário
    marca = input("Digite a marca: ")
    modelo = input("Digite o modelo: ")
    armazenamento = input("Digite o armazenamento: ")
    cor = input("Digite a cor: ")
    sistema_operacional = input("Digite o sistema operacional: ")
    preco = float(input("Digite o preço: R$ "))
    fabricante = input("Digite o fabricante: ")
    ano_fabricacao = int(input("Digite o ano de fabricação: "))

    # Criando um objeto Smartphone
    smartphone = Smartphone(
        marca,
        modelo,
        armazenamento,
        cor,
        sistema_operacional,
        preco,
        fabricante,
        ano_fabricacao
    )

    # Adicionando o smartphone na lista
    smartphones.append(smartphone)

    # Perguntando se deseja cadastrar outro
    continuar = input("\nDeseja cadastrar outro smartphone? (sim/não): ").lower()

# Exibindo o resultado final
print("\n===================================")
print("       RELATÓRIO DE SMARTPHONES")
print("===================================")

# Mostrando a quantidade de smartphones cadastrados
print("Quantidade de smartphones cadastrados:", len(smartphones))

# Mostrando a descrição de cada smartphone
for i, smartphone in enumerate(smartphones, start=1):
    print("\nSmartphone", i)
    smartphone.exibir_dados()

print("\nFim do programa!")
