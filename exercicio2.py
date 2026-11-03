def analisar_texto(texto):
  if not texto or not texto.strip():
    return 0
  palavras = texto.strip().split()
  return len(palavras)