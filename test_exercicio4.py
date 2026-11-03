from unittest.mock import patch
from exercicio4 import buscar_nome, gerar_saudacao
import pytest


def test_gerar_saudacao_fluxo_padrao():
  resultado = gerar_saudacao(1)
  assert resultado == "Olá, Carlos! Seja bem-vindo."  


def test_buscar_nome_foi_chamada_com_id():
  with patch("exercicio4.buscar_nome") as mock_buscar_nome:
    mock_buscar_nome.return_value = "Carlos"

    gerar_saudacao(42)

    mock_buscar_nome.assert_called_once()  
    mock_buscar_nome.assert_called_with(42)  


def test_gerar_saudacao_com_mock_diferentes_nomes():
  with patch("exercicio4.buscar_nome") as mock_buscar_nome:
    mock_buscar_nome.return_value = "Mariana" 

    resultado = gerar_saudacao(10)

    assert resultado == "Olá, Mariana! Seja bem-vindo."
    mock_buscar_nome.assert_called_once_with(10)