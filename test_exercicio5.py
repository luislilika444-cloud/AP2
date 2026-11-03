from unittest.mock import patch
from exercicio5 import criar_conta, verificar_senha
import pytest


def test_verificar_senha_direta():
  assert verificar_senha("SenhaForte123") is True  
  assert verificar_senha("curta1") is False  


def test_criar_conta_chamada_verificar_senha():
  with patch("exercicio5.verificar_senha") as mock_verificar_senha:
    mock_verificar_senha.return_value = True

    criar_conta("Ana", "senha12345")

    mock_verificar_senha.assert_called_once() 
    mock_verificar_senha.assert_called_with("senha12345")  


def test_criar_conta_com_mock_senha_valida():
  with patch("exercicio5.verificar_senha") as mock_verificar_senha:
    mock_verificar_senha.return_value = True  

    resposta = criar_conta("Bruno", "mocked_pass")
    assert resposta == "Conta criada com sucesso"


def test_criar_conta_com_mock_senha_invalida():
  with patch("exercicio5.verificar_senha") as mock_verificar_senha:
    mock_verificar_senha.return_value = False 

    resposta = criar_conta("Carla", "123")
    assert resposta == "Senha inválida"