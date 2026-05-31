import unittest

# Lógica de Negócios (O que será testado)
def calcular_desconto(valor, percentual):
    """
    Calcula o valor do desconto.
    Regra: O percentual deve ser entre 0 e 100.
    """
    if not (0 <= percentual <= 100):
        raise ValueError("Percentual deve estar entre 0 e 100")
    
    if valor < 0:
        raise ValueError("O valor não pode ser negativo")
        
    return valor * (percentual / 100)

def formatar_moeda(valor):
    """Formata um número para o padrão de moeda R$."""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Classe de Testes Automatizados
class TestSistemaDescontos(unittest.TestCase):

    def test_calculo_desconto_sucesso(self):
        """Testa se o cálculo de 10% de 100 retorna 10."""
        self.assertEqual(calcular_desconto(100, 10), 10.0)

    def test_calculo_desconto_zero(self):
        """Testa se o cálculo com 0% retorna 0."""
        self.assertEqual(calcular_desconto(500, 0), 0.0)

    def test_erro_percentual_invalido(self):
        """Testa se dispara erro ao passar percentual maior que 100."""
        with self.assertRaises(ValueError):
            calcular_desconto(100, 110)

    def test_erro_valor_negativo(self):
        """Testa se dispara erro ao passar valor negativo."""
        with self.assertRaises(ValueError):
            calcular_desconto(-50, 10)

    def test_formatacao_moeda(self):
        """Testa a formatação de moeda brasileira."""
        self.assertEqual(formatar_moeda(1250.5), "R$ 1.250,50")

if __name__ == "__main__":
    # Executa os testes
    unittest.main()
