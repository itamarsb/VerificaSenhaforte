def senha_forte(senha: str) -> bool:
    """
    Verifica se uma senha é forte:
    - Pelo menos 8 caracteres
    - Contém pelo menos um número
    - Contém pelo menos um caractere que não seja número (letra ou símbolo)
    """
    if len(senha) < 8:
        print("A senha deve conter pelo menos 8 caracteres.")
        return False

    tem_numero = any(caractere.isdigit() for caractere in senha)
    tem_nao_numero = any(not caractere.isdigit() for caractere in senha)

    if not tem_numero:
        print("A senha deve conter pelo menos um número.")
        return False
    if not tem_nao_numero:
        print("A senha deve conter pelo menos uma letra ou caractere especial.")
        return False

    return True


def solicitar_senha():
    print("Digite uma senha forte (ou 'sair' para encerrar):")
    while True:
        senha = input("Senha: ").strip()
        if senha.lower() == 'sair':
            print("Encerrando o programa.")
            break
        if senha_forte(senha):
            print("Senha válida e forte!")
            break
        else:
            print("Tente novamente.\n")


# Executa o programa
if __name__ == "__main__":
    solicitar_senha()
