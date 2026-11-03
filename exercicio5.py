def verificar_senha(senha):
  if not isinstance(senha, str):
    return False
  tem_tamanho = len(senha) >= 8
  tem_numero = any(char.isdigit() for char in senha)
  tem_letra = any(char.isalpha() for char in senha)
  return tem_tamanho and tem_numero and tem_letra


def criar_conta(nome, senha):
  if verificar_senha(senha):
    return "Conta criada com sucesso"
  return "Senha inválida"