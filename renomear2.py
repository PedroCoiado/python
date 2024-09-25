import os


# Para criar uma funçãoem python iremos ultilizar o comando 
# def (definição)
def mudarNome(ar_or, nv_ar):
    """ 
    A função mudarNome, altera o nome de um arquivo.
    O usuário deve passar o nome original e novo nome.
    Args:
        ar_or(str): O nome de origem do arquivo
        nv_ar(str): Arquivo com novo nome
    Returns:
        Retorna uma mensagem de confirmação
    """
    os.rename(ar_or,nv_ar)
    msg = "O nome do arquivo foi alterado"
    return msg

arquivo_original = input("Digite o nome do arquivo que sera renomeado")
novo_arquivo = input("Digite o novo nome arquivo")
rs = mudarNome(arquivo_original, novo_arquivo)    
print(rs)
