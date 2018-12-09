import csv
from fractions import Fraction
import operator

Respostas = {
    "Formacao": {"Fundamental_Completo": 0, "Medio_Completo": 0, "Superior_Incompleto": 0, "Superior_Completo": 0,
                 "Graduacao": 0},
    "Problema": {"Sumario": 0, "Figura": 0, "Pagina": 0, "Espacamento": 0, "Alinhamento": 0, "Referencia": 0,
                 "Citacao": 0, "Tabela": 0, "Compreensao": 0, "Outro": 0},
    "Ambiente": {"Google": 0, "Word": 0, "Libre": 0, "FastFormat": 0, "Quip": 0, "Zoho": 0, "Only": 0, "Outro": 0},
    "Ferramenta": {"Modelo": 0, "Referencia": 0, "Tutorial": 0, "Sugestoes": 0, "Formatacao": 0, "Citacoes": 0,
                   "Compartilhar": 0, "Grafico": 0, "Sumario": 0, "Plagio": 0, "Siglas": 0, "Imagens": 0, "Outro": 0}}
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
            elif key.lower() == 'quais dos seguintes ambientes você utiliza na edição de seus trabalhos?':
                for tipo_ambiente in val.split(';'):
                    if tipo_ambiente.lower() == 'google docs':
                        Respostas['Ambiente']['Google'] += 1
                    elif tipo_ambiente.lower() == 'word':
                        Respostas['Ambiente']['Word'] += 1
                    elif tipo_ambiente.lower() == 'libre office':
                        Respostas['Ambiente']['Libre'] += 1
                    elif tipo_ambiente.lower() == 'fastformat':
                        Respostas['Ambiente']['FastFormat'] += 1
                    elif tipo_ambiente.lower() == 'quip':
                        Respostas['Ambiente']['Quip'] += 1
                    elif tipo_ambiente.lower() == 'zoho':
                        Respostas['Ambiente']['Zoho'] += 1
                    elif tipo_ambiente.lower() == 'only office':
                        Respostas['Ambiente']['Only'] += 1
                    elif tipo_ambiente.lower() == 'outros':
                        Respostas['Ambiente']['Outro'] += 1
            elif key.lower() == 'quais destas opções você gostaria que uma ferramenta de edição fornecesse como ajuda na edição de um trabalho acadêmico?':
                for ferramenta_edicao in val.split(';'):
                    if ferramenta_edicao.lower() == 'modelo de documentos':
                        Respostas['Ferramenta']['Modelo'] += 1
                    elif ferramenta_edicao.lower() == 'gerador de referências':
                        Respostas['Ferramenta']['Referencia'] += 1
                    elif ferramenta_edicao.lower() == 'tutorial interativo da ferramenta':
                        Respostas['Ferramenta']['Tutorial'] += 1
                    elif ferramenta_edicao.lower() == 'sugestões de erros':
                        Respostas['Ferramenta']['Sugestoes'] += 1
                    elif ferramenta_edicao.lower() == 'dicas de formatação':
                        Respostas['Ferramenta']['Formatacao'] += 1
                    elif ferramenta_edicao.lower() == 'instruções para citações':
                        Respostas['Ferramenta']['Citacoes'] += 1
                    elif ferramenta_edicao.lower() == 'compartilhar documento com o orientador':
                        Respostas['Ferramenta']['Compartilhar'] += 1
                    elif ferramenta_edicao.lower() == 'gerador de gráficos':
                        Respostas['Ferramenta']['Grafico'] += 1
                    elif ferramenta_edicao.lower() == 'criação automática de sumários':
                        Respostas['Ferramenta']['Sumario'] += 1
                    elif ferramenta_edicao.lower() == 'verificação de plágio':
                        Respostas['Ferramenta']['Plagio'] += 1
                    elif ferramenta_edicao.lower() == 'gerador de tabela de siglas':
                        Respostas['Ferramenta']['Siglas'] += 1
                    elif ferramenta_edicao.lower() == 'gerador de tabela de imagens':
                        Respostas['Ferramenta']['Imagens'] += 1
                    elif ferramenta_edicao.lower() == 'outros':
                        Respostas['Ferramenta']['Outro'] += 1


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


def formacao_superior_incompleto(r):
    return 'Superior_Incompleto' in r


def formacao_superior_incompleto_or_completo(r):
    return 'Superior_Incompleto' in r or 'Superior_Completo' in r


def formacao_fundamental_completo(r):
    return 'Fundamental_Completo' in r


def problema_edicao(r):
    return 'Referencia' in r or 'Citacao' in r or 'Pagina' in r


def problema_sumario(r):
    return 'Sumario' in r


def ambiente_word(r):
    return 'Word' in r


def ambiente_google_word(r):
    return 'Google' in r or 'Word' in r


def not_in_ambiente_google_word(r):
    return 'Google' not in r and 'Word' not in r


def ambiente_word_problema_sumario(r):
    return 'Word' in r and 'Sumario' in r


def ferramenta_criacao_sumario(r):
    return 'Sumario' in r


PDFormacao = ProbDist(Respostas['Formacao'])
PDProblema = ProbDist(Respostas['Problema'])
PDFormacaoProblema = joint(PDFormacao, PDProblema, ' ')
PEX2 = P(formacao_superior_incompleto, tal_que(problema_edicao, PDFormacaoProblema))
"""Imprimindo resposta da questão 2."""
# print(PEX2)


PDAmbiente = ProbDist(Respostas['Ambiente'])
PDProblemaAmbiente = joint(PDAmbiente, PDProblema, ' ')
PEX3 = P(ambiente_word, tal_que(problema_sumario, PDProblemaAmbiente))
"""Imprimindo resposta da questão 3."""
# print(PEX3)


PDFerramenta = ProbDist(Respostas['Ferramenta'])
PDProblemaAmbienteFerramenta = joint(PDProblemaAmbiente, PDFerramenta, ' ')
PEX4 = P(ambiente_word_problema_sumario, tal_que(ferramenta_criacao_sumario, PDProblemaAmbienteFerramenta))
"""Imprimindo resposta da questão 4."""
# print(PEX4)


PDFormacaoAmbiente = joint(PDFormacao, PDAmbiente, ' ')
PEX5 = P(formacao_fundamental_completo, tal_que(ambiente_google_word, PDFormacaoAmbiente))
"""Imprimindo resposta da questão 5."""
# print(PEX5)


PEX6 = P(formacao_superior_incompleto_or_completo, tal_que(not_in_ambiente_google_word, PDFormacaoAmbiente))
"""Imprimindo resposta da questão 6."""
# print(PEX6)


PEX7 = tal_que(ambiente_word, PDProblemaAmbiente)
result = {}
for key in sorted(PEX7, key=PEX7.get, reverse=True)[:2]:
    result.update({key: PEX7[key]})
"""Imprimindo resposta da questão 7."""
print(result)
