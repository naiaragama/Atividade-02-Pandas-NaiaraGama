import pandas as pd
import numpy as np
df = pd.read_csv('shopping_trends.csv')
df.head()
df.tail()
df.info()
df.shape
df.describe()
df.isnull().sum()
df.isna().sum()
df.Gender.value_counts()
df.columns

#renomeando as colunas
col_dic = {
    'Customer ID': 'customer_id',
    'Age': 'age',
    'Gender': 'gender',
    'Item Purchased': 'item_purchased',
    'Category': 'category',
    'Purchase Amount (USD)': 'purchase_amount_usd',
    'Location': 'location',
    'Size': 'size',
    'Color': 'color',
    'Season': 'season',
    'Review Rating': 'review_rating',
    'Subscription Status': 'subscription_status',
    'Payment Method': 'payment_method',
    'Shipping Type': 'shipping_type',
    'Discount Applied': 'discount_applied',
    'Promo Code Used': 'promo_code_used',
    'Previous Purchases': 'previous_purchases',
    'Preferred Payment Method': 'preferred_payment_method',
    'Frequency of Purchases': 'frequency_purchases'
}
df = df.rename(col_dic, axis= 1)
df.head()

df['frequency_purchases'].unique()

df.review_rating.unique()

#criando uma nova categoria para a avaliação dos clientes
df['review_rating_cat'] = pd.cut(df['review_rating'], bins=[0,2.5,4,5], labels=['ruim', 'bom', 'excelente'])
df.head()

#cores favoritas
print(df.color.value_counts())

#métodos de pagamento favoritos
print(df.payment_method.value_counts())

#categorias
print(df.category.value_counts())

#média de compras por genero
male_mean = df[df['gender'] == 'Male']['purchase_amount_usd'].mean()
female_mean = df[df['gender'] == 'Female']['purchase_amount_usd'].mean()

print(male_mean)
print(female_mean)

#valor médio total de compra
print(df.purchase_amount_usd.mean())

#verificando estações
print(df.iloc[:,8])

#quantos clientes possuem mais que 25 anos?
print(df[(df['age']>25)].head())

#clientes acima de 25 anos que compraram mais que 50 dolares
print(df[(df['age']>25)|(df['purchase_amount_usd']>50)].head())

#idade média
print(df.age.mean())

#idade mínima
print(df.age.min())

#idade máxima
print(df.age.max())

#avaliando o ticket médio de compra de acordo com avaliação
print(df.groupby('review_rating_cat')['purchase_amount_usd'].mean(numeric_only=True))


#acrescentando coluna de ticket médio de compra por cliente
df['average_ticket'] = df['purchase_amount_usd']*df['previous_purchases']
df.head()

#analisando quantidade de descontos aplicados
df.discount_applied.value_counts()

#criando função com apply para aplicar um desconto de 10% e criando uma nova coluna
def func(row):
    if row['discount_applied'] == 'Yes':
        return row['purchase_amount_usd']*0.9
    else:
        return row['purchase_amount_usd']

df['discount_10%'] = df.apply(func, axis=1)
df.head()

#plotando gráfico pizza para genero
df.groupby(['gender'],dropna=False).size().sort_values(ascending=False).plot.pie(figsize=(8,8))

#plotando gráfico barra para método de pagamento
df.groupby(['payment_method'],dropna=False).size().sort_values(ascending=False).head(5).plot.bar(figsize=(12,8),xlabel='Método pagamento',ylabel='Quantidade')

#Quais são os itens mais comprados por categoria
print(df.groupby('category')['purchase_amount_usd'].sum().plot(kind='barh'))
