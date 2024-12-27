def formata_float_str_moeda(valor: float) ->str:
    valor = float(valor)
    return f'R$ {valor:,.2f}'

