from exercicio3 import analisar_numero


def test_analisar_numero_positivo_par():
  assert analisar_numero(10) == "Positivo e par"  # Teste 1[cite: 1]


def test_analisar_numero_positivo_impar():
  assert analisar_numero(7) == "Positivo e ímpar"  # Teste 2[cite: 1]


def test_analisar_numero_negativo_par():
  assert analisar_numero(-4) == "Negativo e par"  # Teste 3[cite: 1]


def test_analisar_numero_negativo_impar():
  assert analisar_numero(-3) == "Negativo e ímpar"  # Teste 4[cite: 1]


def test_analisar_numero_zero():
  assert analisar_numero(0) == "Zero e par"  # Teste 5[cite: 1]