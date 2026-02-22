import pandas as pd


def parcing(file):
    # Читаем листы
    sheets = pd.read_excel(file, sheet_name=['Материалы', 'Цены'], engine='openpyxl')
    
    materials_df = sheets['Материалы']
    prices_df = sheets['Цены']
    
    # Переименовываем столбцы для единообразия
    materials_df.columns = ['материал', 'количество']
    prices_df.columns = ['материал', 'цена']
    # Объединяем по столбцу «материал»
    result = pd.merge(materials_df, prices_df, on='материал', how='inner')
    return result