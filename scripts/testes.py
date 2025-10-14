import pandas as pd

df = pd.DataFrame({
    'BAIRRO': ['Centro', 'Jardim América', 'Vila São João']
})

print(df['BAIRRO'].str.upper())