import csv
from fractions import Fraction

Respostas = {
    "Formacao": {"Fundamental_Completo": 0, "Medio_Completo": 0, "Superior_Incompleto": 0, "Superior_Completo": 0,
                 "Graduacao": 0},
    "Problema": {"Sumario": 0, "Figura": 0, "Pagina": 0, "Espacamento": 0, "Alinhamento": 0, "Referencia": 0,
                 "Citacao": 0, "Tabela": 0, "Compreensao": 0, "Outro": 0}}
with open('respostas.csv', 'r', encoding='utf-8', errors='ignore') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        for key, val in row.items():
            if key.lower() == 'qual sua formação acadêmica?':
                if val.lower() == 'ensino fundamental completo':
                    Respostas['Formacao']['Fundamental_Completo'] += 1
                elif val.lower() == 'ensino médio completo':
                    Respostas['Formacao']['Medio_Completo'] += 1
                elif val.lower() == 'ensino superior incompleto':
                    Respostas['Formacao']['Superior_Incompleto'] += 1
                elif val.lower() == 'ensino superior completo':
                    Respostas['Formacao']['Superior_Completo'] += 1
                elif val.lower() == 'pós-graduação':
                    Respostas['Formacao']['Graduacao'] += 1
            elif key.lower() == 'quais dos seguintes problemas você possui no momento da edição de trabalhos acadêmicos?':
                for tipo_problema in val.split(';'):
                    if tipo_problema.lower() == 'criação de sumários':
                        Respostas['Problema']['Sumario'] += 1
                    elif tipo_problema.lower() == 'criação de lista de figuras':
                        Respostas['Problema']['Figura'] += 1
                    elif tipo_problema.lower() == 'numeração de páginas':
                        Respostas['Problema']['Pagina'] += 1
                    elif tipo_problema.lower() == 'espaçamento do texto':
                        Respostas['Problema']['Espacamento'] += 1
                    elif tipo_problema.lower() == 'alinhamento do texto':
                        Respostas['Problema']['Alinhamento'] += 1
                    elif tipo_problema.lower() == 'criar referências':
                        Respostas['Problema']['Referencia'] += 1
                    elif tipo_problema.lower() == 'fazer citações':
                        Respostas['Problema']['Citacao'] += 1
                    elif tipo_problema.lower() == 'criar tabelas':
                        Respostas['Problema']['Tabela'] += 1
                    elif tipo_problema.lower() == 'não compreender a ferramenta':
                        Respostas['Problema']['Compreensao'] += 1
                    elif tipo_problema.lower() == 'outros':
                        Respostas['Problema']['Outro'] += 1


def tal_que(predicado, espaco):
    """Os resultados no espaco amostral para os quais o predicado é verdadeiro. Se espaço e um conjunto ,
    retorna um subconjunto {resultado , ...}
    Se espaco e ProbDist , retorna um ProbDist{resultado , frequencia}"""
    if isinstance(espaco, ProbDist):
        return ProbDist({o: espaco[o] for o in espaco if predicado(o)})
    else:
        return {o for o in espaco if predicado(o)}


def P(evento, espaco):
    """A probabilidade de um evento , dado um espaco amostral de resultados
    equiprovaveis.
    evento: uma colecao de resultados , ou um predicado.
    espaco: um conjunto de resultados ou a distribuicao de probabilidade
    na forma de pares {resultado: frequencia}."""
    if callable(evento):
        evento = tal_que(evento, espaco)
    if isinstance(espaco, ProbDist):
        return sum(espaco[o] for o in espaco if o in evento)
    else:
        return Fraction(len(evento & espaco), len(espaco))


class ProbDist(dict):
    """Uma distribuicao de probablidade; um mapeamento {resultado:probabilidade}"""

    def __init__(self, mapping=(), **kwargs):
        self.update(mapping, **kwargs)
        total = sum(self.values())
        for outcome in self:
            self[outcome] = self[outcome] / total
            assert self[outcome] >= 0


def joint(A, B, sep=''):
    """A probabilidade conjunta de duas distribuições de probabilidade
        independentes.
    Resultado é todas as entradas da forma {a+sep+b: P(a)*P(b)}"""
    return ProbDist({a + sep + b: A[a] * B[b]
                     for a in A
                     for b in B})


def sexo_m(r):
    return 'Sexo_M' in r


def superior_incompleto(r):
    return 'Superior_Incompleto' in r


def problema_edicao(r):
    return 'Referencia' in r or 'Citacao' in r or 'Pagina' in r


PDFormacao = ProbDist(Respostas['Formacao'])
PDProblema = ProbDist(Respostas['Problema'])
PDFormacaoProblema = joint(PDFormacao, PDProblema, ' ')
PEX2 = P(superior_incompleto, tal_que(problema_edicao, PDFormacaoProblema))
"""Imprimindo resposta da questão 2"""
print(PEX2)