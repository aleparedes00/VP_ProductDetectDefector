import pandas as pd

data_shoes = 'ASH16.json'
ropa = 'DONDUP16.json'
df = pd.read_json(data_shoes)
df_ropa = pd.read_json(ropa)

df_attributes = df['attributes']
df_attributes_id = df_attributes['id']
print('')