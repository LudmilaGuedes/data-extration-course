# Portfólio de Extração e Preparação de Dados

**Aluno:** Ludmila Guedes da Costa
**Curso:** Ciência de Dados & IA | IBEMEC
**Semestre:** 2026.1
**Disciplina:** Extração e Preparação de Dados (IBM8915)
**Professor:** Luís Aramis

---

# 📋 Data Extraction & Feature Engineering Course

Este repositório contém o conjunto de entregas práticas desenvolvidas ao longo da disciplina de **Big Data & Cloud Computing**. O objetivo é demonstrar competências em todo o ciclo de vida da engenharia de dados, desde a extração bruta de fontes heterogêneas até a preparação avançada de atributos para modelos de Machine Learning.

---

## Índice de Projetos

### 🔹 Módulo 1: Extração e Análise Exploratória (Raw Data)
Foco na obtenção de dados de diversas fontes e compreensão inicial do comportamento das variáveis.

| Lab | Atividade | Competências Demonstradas |
| :--- | :--- | :--- |
| **Lab 01** | [Extração de Arquivos Planos](./notebooks/lab_01.ipynb) | Uso de `pandas` para leitura de múltiplos formatos (CSV/Excel). |
| **Lab 02** | [Extração via SQL](./notebooks/lab_02.ipynb) | Conexão com bancos de dados relacionais via `SQLAlchemy`. |
| **Lab 03** | [Análise Exploratória (EDA)](./notebooks/lab_03.ipynb) | Aplicação de estatística descritiva e visualização com histogramas. |

### 🔹 Módulo 2: Limpeza e Tratamento de Dados (Data Cleaning)
Técnicas robustas para lidar com inconsistências e lacunas nos dados reais.

| Lab | Atividade | Competências Demonstradas |
| :--- | :--- | :--- |
| **Lab 04** | [Dados Ausentes](./notebooks/lab_04.ipynb) | Identificação e visualização estratégica de dados faltantes. |
| **Lab 05** | [Imputação Univariada e Multivariada](./notebooks/lab_05.ipynb) | Estratégias de preenchimento ou descarte de dados `NaN`. |
| **Lab 06** | [Tratamento de Cardinalidade](./notebooks/lab_06.ipynb) | Agrupamento de categorias raras e gestão de alta cardinalidade. |

### 🔹 Módulo 3: Engenharia de Atributos (Feature Engineering)
Transformação de dados brutos em variáveis preditivas de alto valor.

| Lab | Atividade | Competências Demonstradas |
| :--- | :--- | :--- |
| **Lab 07** | [Encoders de Categóricas](./notebooks/lab_07.ipynb) | Codificação de variáveis para algoritmos matemáticos. |
| **Lab 08** | [Binning e Discretização](./notebooks/lab_08.ipynb) | Transformação de variáveis numéricas contínuas em intervalos. |
| **Lab 09** | [Engenharia do Tempo (Datetime)](./notebooks/lab_09.ipynb) | Decomposição de datas em componentes sazonais e temporais. |
| **Lab 10** | [Criação de Variáveis Numéricas](./notebooks/lab_10.ipynb) | Desenvolvimento de novas métricas a partir de colunas existentes. |
| **Lab 11** | [Tratamento de Outliers](./notebooks/lab_11.ipynb) | Detecção e tratamento integrado de valores atípicos. |

---

## Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Manipulação de Dados:** `Pandas`, `Numpy`
* **Processamento:** `Scikit-Learn`, `Feature-engine`
* **Conectores:** `SQLAlchemy`
* **Visualização:** `Matplotlib`, `Seaborn`

---

## Como Executar

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/LudmilaGuedes/data-extration-course.git](https://github.com/LudmilaGuedes/data-extration-course.git)
