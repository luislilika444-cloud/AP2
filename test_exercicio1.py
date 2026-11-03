from exercicio1 import classificar_nota


def test_classificar_nota_aprovado():
  assert classificar_nota(8) == "Aprovado"  # Teste 1: Nota 8: aprovado[cite: 1]


def test_classificar_nota_recuperacao():
  assert classificar_nota(6) == "Recuperação"  # Teste 2: Nota 6: recuperação[cite: 1]


def test_classificar_nota_reprovado():
  assert classificar_nota(4) == "Reprovado"  # Teste 3: Nota 4: reprovado[cite: 1]


def test_classificar_nota_dez_aprovado():
  assert classificar_nota(10) == "Aprovado"  # Teste 4: Nota 10: aprovado[cite: 1]


def test_classificar_nota_negativa_invalida():
  assert classificar_nota(-1) == "Nota inválida"  # Teste 5: Nota -1: inválida[cite: 1]


def test_classificar_nota_maior_dez_invalida():
  assert classificar_nota(11) == "Nota inválida"  # Teste 6: Nota 11: inválida[cite: 1]

def test_classificar_nota_limite_recuperacao():
  assert classificar_nota(5) == "Recuperação"