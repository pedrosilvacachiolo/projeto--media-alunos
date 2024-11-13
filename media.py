# main.py

# Função principal para calcular a média das notas
def calcular_media():
    # Recebe as 3 notas do aluno
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    # Calcula a média aritmética
    media = (nota1 + nota2 + nota3) / 3
    
    # Exibe a média
    print(f"A média do aluno é: {media:.2f}")

# Chama a função para calcular e exibir a média
if __name__ == "__main__":
    calcular_media()
