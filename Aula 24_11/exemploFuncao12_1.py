"""Mais exemplo de função com dicionário"""


def funcao_carro(carro):
    # 'nome_dict'['chave']
    print(
        f"""
    Nome: {carro["nome"]}
    Ano: {carro["ano"]}
    Marca: {carro["marca"]}
    Cor: {carro["cor"]}
    Modelo: {carro["modelo"]}
    Placa: {carro["placa"]}
    Chassi: {carro["chassi"]}
    Tipo do combustível: {carro["tipo_combustivel"]}
        """
    )


meu_carro = {
    "nome": "Betina",
    "ano": 1995,
    "marca": "BMW",
    "cor": "Vinho",
    "modelo": "zica",
    "placa": "45AB7D",
    "chassi": 12345,
    "tipo_combustivel": "gasolina pura",
}

funcao_carro(meu_carro)
