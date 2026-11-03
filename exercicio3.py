def analisar_numero(numero):
  paridade = "par" if numero % 2 == 0 else "ímpar"

  if numero > 0:
    sinal = "Positivo"
  elif numero < 0:
    sinal = "Negativo"
  else:
    return "Zero e par"

  return f"{sinal} e {paridade}"

