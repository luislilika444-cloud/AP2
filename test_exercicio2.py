from exercicio2 import analisar_texto


def test_analisar_texto_cinco_palavras():
  assert analisar_texto("Esta é uma frase curta.") == 5  # Teste 1[cite: 1, 2]


def test_analisar_texto_uma_palavra():
  assert analisar_texto("Python") == 1  # Teste 2[cite: 1, 2]


def test_analisar_texto_vazio():
  assert analisar_texto("") == 0  # Teste 3[cite: 1, 2]


def test_analisar_texto_espacos_pontas():
  assert analisar_texto("   Olá mundo   ") == 2  # Teste 4[cite: 1, 2]


def test_analisar_texto_varios_espacos():
  assert analisar_texto("Frase   com   vários   espaços") == 4  # Teste 5[cite: 1, 2]