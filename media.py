# main.py

def calcular_media():
    # Recebe as 3 notas do aluno
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    def caucular_media_ponderada(nota1, nota2, nota3)
    #cauculando a media ponderada
    peso1, peso2, peso3 = 1, 1, 2
    media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
    return media 
    
    # Exibe a média
    print(f"A média do aluno é: {media:.2f}")
    
    # Verificação de aprovação
    if media >= 6.0:
        print("Aprovado")
    elif media >= 5.0:
        print("Recuperação")
    else:
        print("Reprovado")

if __name__ == "__main__":
    calcular_media()
