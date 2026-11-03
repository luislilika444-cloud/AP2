from unittest.mock import patch
from exercicio6 import confirmar_reserva


def test_confirmar_reserva_sucesso():
  with patch("exercicio6.verificar_assento") as mock_verificar_assento, patch(
      "exercicio6.reservar_assento"
  ) as mock_reservar_assento:

    mock_verificar_assento.return_value = True
    mock_reservar_assento.return_value = "Assento reservado"

    resultado = confirmar_reserva(12)

    assert resultado == "Assento reservado"
    mock_verificar_assento.assert_called_once_with(12)
    mock_reservar_assento.assert_called_once_with(12)


def test_confirmar_reserva_indisponivel():
  with patch("exercicio6.verificar_assento") as mock_verificar_assento, patch(
      "exercicio6.reservar_assento"
  ) as mock_reservar_assento:

    mock_verificar_assento.return_value = False

    resultado = confirmar_reserva(15)

    assert resultado == "Assento indisponível"
    mock_verificar_assento.assert_called_once_with(15)
    mock_reservar_assento.assert_not_called()


# Novo teste extra para o Exercício 6 (+1 teste)
def test_confirmar_reserva_outro_assento_sucesso():
  with patch("exercicio6.verificar_assento") as mock_verificar_assento, patch(
      "exercicio6.reservar_assento"
  ) as mock_reservar_assento:

    mock_verificar_assento.return_value = True
    mock_reservar_assento.return_value = "Assento reservado"

    resultado = confirmar_reserva(88)

    assert resultado == "Assento reservado"
    mock_verificar_assento.assert_called_once_with(88)
    mock_reservar_assento.assert_called_once_with(88)