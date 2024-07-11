# LH_CD_GIOVANNI_BIANCHINI_DE_BARROS

![Language](https://img.shields.io/badge/Language-Python-blue) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/giovannibianchinidebarros/javascript-piano/graphs/commit-activity)

## Desafio Cientista de Dados - Indicium 2024

Este é meu projeto para o Processo Seletivo do Programa **Lighthouse** da Indicium.

Este projeto utiliza técnicas de aprendizado de máquina para prever a avaliação de um filme no IMDB com base em várias características, como gênero, elenco, diretor, sinopse, ano de lançamento, duração, número de votos e arrecadação. Ele também conta com um sistema de recomendação de filmes.

### EDA (Exploração de Dados)

Durante a análise exploratória de dados, observamos vários pontos importantes:

- **Gêneros de Filmes**: Ação e Aventura tendem a ter melhores resultados de bilheteria, seguidos por Animação e Sci-Fi. Filmes de Drama, embora sejam mais comuns no conjunto de dados, enfrentam mais dificuldades para alcançar sucesso comercial.
- **Classificações Etárias**: Filmes voltados para o público em geral tendem a ter uma bilheteria maior.
- **Número de Votos e Faturamento**: Há uma correlação entre o número de votos recebidos e o faturamento, sugerindo que filmes com maior bilheteria tendem a receber mais votos no IMDb.
- **Influência do Diretor e Elenco**: A direção e o elenco influenciam consideravelmente na avaliação e no faturamento dos filmes.

### Recomendação de Filmes:

Foi criado um sistema de recomendação de filmes usando TfidfVectorizer e cosine_similarity.

Se uma pessoa falar que gostou de um filme específico, esse sistema retorna filmes similares, considerando gênero, elenco e descrição.

Esse teste encontra-se no arquivo **LH_CD_GIOVANNI_BIANCHINI_DE_BARROS.ipynb**

Como exemplo se selecionamos o filme **"The Avengers"** será recomendado:

      Captain America: Civil War
      Arrival
      Captain America: The Winter Soldier
      Serenity
      Iron Man
      Avengers: Infinity War
      The Day the Earth Stood Still
      Avengers: Endgame
      Interstellar

### Sobre a coluna Overview (sinopse do filme)

A coluna Overview apresenta informações úteis sobre o filme e podemos incluir uma análise de palavras e temas mais comuns no processo de aprendizado de maquina.

Da mesmo forma, verificamos que é possível inferir o gênero do filme a partir da coluna "Overview", utilizando técnicas de NLP. Eu fiz um teste com TfidfVectorizer para criar um modelo que tenta prever o Gênero a partir do texto.

### Modelo de Machine Learning

Foi criado um modelo de machine learning para prever a nota de um filme. O pipeline inclui:

- **Preprocessamento dos Dados**: Normalização de características numéricas, vetorização de texto (overview), e codificação one-hot para categorias.
- **Modelo de Regressão**: Utilizando a regressão linear para prever o sucesso dos filmes.

As variáveis foram tratadas da seguinte forma:

- Coluna Series_Title: </br>
  foi removido da análise

- Coluna Overview:</br>
  utilizado TfidfVectorizer para analizar texto.

- Colunas Genre, Star1, Star2, Star3, Star4:</br>
  Um filme pode ter pode ter de um a três gêneros.</br>
  Além disso, um ator na coluna Star1 poderia aparecer na Star2 em um outro filme.</br>
  por isso utilizei MultiLabelBinarizer na Coluna Genre e em uma concatenação das colunas Star\*</br>

- Colunas Certificate e Director:</br>
  são variáveis categóricas, por isso foi utilizado OneHotEncoder

- Colunas Released_Year, Runtime, Meta_score, No_of_Votes, Gross:</br>
  variáveis quantitativas, foi utilizado o utilizado StandardScaler

## Requisitos

Certifique-se de ter o Python 3.7+ instalado. Instale os pacotes necessários usando o `requirements.txt`.

## Instalação

Siga as instruções abaixo para configurar o ambiente e executar o projeto.

1. Clonar o Repositório:

```
git clone <URL do seu repositório>
cd nome-do-repositório
```

2. Instalar Dependências. Eu recomendo usar um ambiente virtual:

```
python -m venv venv
venv/scripts/activate
pip install -r requirements.txt
```

3. Para ver a análise exploratória (EDA) abra o jupyter lab e navegue até o arquivo **LH_CD_GIOVANNI_BIANCHINI_DE_BARROS.ipynb**

```
jupyter-lab
```

4. Para testar o modelo criado use o arquivo **predict.py** ou **predict.ipynb**. Se quiser testar com filmes diferentes basta substituir os dados no dicionário dentro de um desses arquivos:

```
# Dados de entrada como um dicionário
data = {
    'Series_Title': 'The Shawshank Redemption',
    'Released_Year': '1994',
    'Certificate': 'A',
    'Runtime': '142 min',
    'Genre': 'Drama',
    'Overview': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
    'Meta_score': 80.0,
    'Director': 'Frank Darabont',
    'Star1': 'Tim Robbins',
    'Star2': 'Morgan Freeman',
    'Star3': 'Bob Gunton',
    'Star4': 'William Sadler',
    'No_of_Votes': 2343110,
    'Gross': '28,341,469'
}
```

## Estrutura do Projeto

- **modelo_imdb.py**: Modelo desenvolvido pelo aprendizado de máquina.
- **README.md**: Documentação do projeto.
- **requirements.txt**: Lista de dependências do Python necessárias para o projeto.
- **LH_CD_GIOVANNI_BIANCHINI_DE_BARROS.ipynb**: Relatórios das análises estatísticas e EDA feito no Jupyter Notebook.
- **LH_CD_GIOVANNI_BIANCHINI_DE_BARROS.pdf**: Relatórios das análises estatísticas e EDA salvo em PDF.
- **predict.py**: código para utilizar o modelo criado e fazer previsões de notas.
- **predict.ipynb**: Igual o código acima, mas em formato do Jupyter Notebook.

## Autor

### Giovanni Bianchini de Barros

[![Linkedin](https://img.shields.io/badge/-giovannibianchinidebarros-blue?style=flat-square&logo=Linkedin&logoColor=white&link=LINK-DO-SEU-LINKEDIN)](https://www.linkedin.com/in/giovannibianchinidebarros/)
[![GitHub](https://img.shields.io/badge/-giovannibianchinidebarros-black?style=flat-square&logo=GitHub&logoColor=white&link=LINK-DO-SEU-GITHUB)](https://github.com/giovannibianchinidebarros)
