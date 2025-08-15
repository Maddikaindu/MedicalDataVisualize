import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

df= pd.read_csv("medical_examination.csv")
print(df.head())
for col in ['height','weight']:
        df[col]=pd.to_numeric(df[col],errors='coerce')
        df.dropna(subset=['height','weight'],inplace=True)
BMI=df['weight']/((df['height']/100)**2)
df['overweight'] = (BMI >25).astype(int)
df['cholesterol']=(df['cholesterol']>1).astype(int)
df['gluc']=(df['gluc']>1).astype(int)
print(df[['overweight','cholesterol','gluc']].head())
def draw_cat_plot():
    df_cat=pd.melt(df,id_vars=['cardio'],value_vars=['cholesterol','gluc','smoke','alco','active','overweight'],var_name='variable',value_name='value')
    df_cat=df_cat.groupby(['cardio','variable','value']).size().reset_index(name='Total')
    fig=sns.catplot(data=df_cat,x='variable',y='Total',hue='value',col='cardio',kind='bar')
    fig.savefig("catplot.png")
    plt.show()
    return fig
def draw_heat_map():
    for col in ['ap_lo','ap_hi','height','weight']:
        df[col]=pd.to_numeric(df[col],errors='coerce')
    df.dropna(subset=['ap_lo','ap_hi','height','weight'],inplace=True)
    df_heat=df[
        (df['ap_lo']<=df['ap_hi'] ) & 
        (df['height']>=df['height'].quantile(0.025) )& 
        (df['height']<=df['height'].quantile(0.975) ) &
        (df['weight']>= df['weight'].quantile(0.025) )&
        (df['weight']<=df['weight'].quantile(0.975))
        ]
    corr=df_heat.corr()
    mask=np.triu(np.ones(corr.shape,dtype=bool))
    fig, ax = plt.subplots(figsize=(12, 6)) 
    sns.heatmap(corr, mask=mask, ax=ax, annot=True, fmt=".1f")
    fig.savefig("heatmap.png") 
    plt.show()
    return fig









