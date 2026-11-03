def classificar_nota(nota):
  if not isinstance(nota, (int, float)):
    return "Nota inválida"

  if nota < 0 or nota > 10:
    return "Nota inválida"
  elif nota >= 7:
    return "Aprovado"
  elif 5 <= nota <= 6.9:
    return "Recuperação"
  else:
    return "Reprovado"