# Dicionário de Dados - Monitoramento de Voos (2025)

Este documento detalha os metadados e a qualidade dos dados após o processo de extração e limpeza inicial.

| Variável | Tipo | Descrição | % Nulos | Anomalias Encontradas |
| :--- | :--- | :--- | :--- | :--- |
| `ICAO Empresa Aérea` | Texto | Código de 3 letras da companhia (padrão ICAO). | 0% | Presença de espaços em branco (ruído de string) antes da limpeza. |
| `Número Voo` | Texto/Int | Identificador numérico da linha aérea. | 0% | Lido inicialmente como objeto devido à formatação do CSV. |
| `Código Autorização (DI)` | Texto | Categoria da autorização de voo da ANAC. | 0% | Continha o valor "0" que representava operações fora do escopo de análise. |
| `Código Tipo Linha` | Texto | Classificação: 'N' (Nacional) ou 'I' (Internacional). | 0% | Continha siglas diversas que foram filtradas para manter apenas o core business (N/I). |
| `ICAO Aeródromo Origem` | Texto | Código identificador do aeroporto de partida. | 0% | Dados consistentes após remoção de duplicatas. |
| `ICAO Aeródromo Destino` | Texto | Código identificador do aeroporto de chegada. | 0% | Dados consistentes após remoção de duplicatas. |
| `Partida Prevista` | Data/Hora | Horário planejado para decolagem (fuso local). | 2.6% | Strings com frações de segundo excessivas (ex: .100000) impediam a conversão direta. |
| `Partida Real` | Data/Hora | Horário efetivo da decolagem. | 3.7% | Nulos concentrados em voos com situação "CANCELADO". |
| `Chegada Prevista` | Data/Hora | Horário planejado para o pouso. | 2.6% | Erros de formatação de string idênticos à Partida Prevista. |
| `Chegada Real` | Data/Hora | Horário efetivo do pouso. | 3.7% | Valores nulos correlacionados a voos não realizados. |
| `Situação Voo` | Texto | Status operacional (REALIZADO, CANCELADO, etc). | 0% | Categorias "NÃO INFORMADO" identificadas em pequena escala. |
| `Código Justificativa` | Texto | Motivo de atrasos ou cancelamentos. | 100% | Campo originalmente vazio no dataset bruto, preenchido como "N/A" na limpeza. |

---
