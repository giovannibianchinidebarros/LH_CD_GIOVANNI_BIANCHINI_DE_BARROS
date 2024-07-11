import numpy as np
import pandas as pd
import joblib


# Função para padronizar os itens da coluna Certificate
def padronizar_Certificate(cert):
    # Classificação Livre, Todos os públicos.
    if cert in ['U', 'G', 'TV-G']:
        return 'G'
    # Parental Guidance. Orientação dos pais sugerida.
    elif cert in ['PG', 'GP', 'TV-PG', '12A', '12', 12, 'UA', 'U/A']:
        return 'PG'
    # Parents Strongly Cautioned. Conteúdo inapropriado para crianças menores de 13 anos.
    elif cert in ['PG-13', 'TV-13', 'TV-14', '13', '14', '15', '16', 13, 14, 15, 16]:
        return 'PG-13'
    # Mature Audience Only. Apenas para adultos.
    elif cert in ['R', 'A', 'TV-MA', 'NC-17', '17', '18', 17, 18]:
        return 'R'
    # Unrated, Passed, Approved, NAN, outros. Filmes sem classificação.
    else:
        return 'Unrated'


# Função para dividir os gêneros em listas
def split_genres(X):
    X = X.copy()
    X['Genre'] = X['Genre'].apply(lambda x: x.split(', '))
    return X


# Função para agrupar elenco em uma lista
def combine_cast(X):
    X = X.copy()
    X['Elenco'] = X[['Star1', 'Star2', 'Star3', 'Star4']].values.tolist()
    return X.drop(columns=['Star1', 'Star2', 'Star3', 'Star4'])


# Função para o pre-processamento dos dados a testar (Utiliza as 3 funções acima):
def preprocess(new_df):
    new_df = new_df.copy()

    if new_df['Released_Year'].dtype == 'object':
        new_df['Released_Year'] = pd.to_numeric(
            new_df['Released_Year'], errors='coerce')
        mode_value = new_df['Released_Year'].mode()[0]
        new_df['Released_Year'] = new_df['Released_Year'].fillna(mode_value)
        new_df['Released_Year'] = new_df['Released_Year'].astype(int)

    if new_df['Runtime'].dtype == 'object':
        new_df['Runtime'] = new_df['Runtime'].apply(
            lambda x: x.replace(' min', '') if isinstance(x, str) else x)
        new_df['Runtime'] = new_df['Runtime'].astype(int)

    if new_df['Gross'].dtype == 'object':
        new_df['Gross'] = new_df['Gross'].str.replace(',', '')
        new_df['Gross'] = new_df['Gross'].astype(float)

    # Função definida anteriormente para padronizar classificação (Certificate)
    new_df['Certificate'] = new_df['Certificate'].apply(
        lambda cert: padronizar_Certificate(cert))
    # Função definida anteriormente para dividir gêneros
    new_df = split_genres(new_df)
    # Função definida anteriormente para combinar elenco
    new_df = combine_cast(new_df)

    return new_df


# Função para transformar gêneros e elenco com o MultiLabelBinarizer ajustado
def transform_genres_and_cast(X):
    X = X.copy()
    genres_transformed = mlb_genre.transform(X['Genre'])
    cast_transformed = mlb_cast.transform(X['Elenco'])

    genres_df = pd.DataFrame(genres_transformed, columns=mlb_genre.classes_)
    cast_df = pd.DataFrame(cast_transformed, columns=mlb_cast.classes_)

    X.reset_index(drop=True, inplace=True)
    genres_df.reset_index(drop=True, inplace=True)
    cast_df.reset_index(drop=True, inplace=True)

    return pd.concat([X.drop(columns=['Genre', 'Elenco']), genres_df, cast_df], axis=1)


# Carregar o modelo e os binarizadores salvos
loaded_model, mlb_genre, mlb_cast = joblib.load('modelo_imdb.pkl')


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


# Converter o dicionário para DataFrame
test_df = pd.DataFrame([data])


# Função para o pre-processamento dos dados a testar:
test_df = preprocess(test_df)


# Fazer previsões usando o modelo carregado
predictions = loaded_model.predict(test_df)


# Exibir as previsões
print("Previsões:", predictions)
