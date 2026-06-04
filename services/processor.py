from services.reader import parcing

def create_summary_table(parced_df):
    summary_df = parced_df.groupby(['Материал', 'Ед.изм'], as_index=False)['количество'].sum()
    summary_df.rename(columns={'количество': 'Общее количество'}, inplace=True)
    summary_df = summary_df[['Материал', 'Общее количество', 'Ед.изм']]

    return summary_df

def create_smeta_materials(df):
    working_df = df.copy()

    working_df['Сумма_строки'] = working_df['количество'] * working_df['Цена']

    # Группируем по материалу и агрегируем данные:
    # - суммируем количество
    # - суммируем суммы по строкам (для расчёта общей суммы)
    aggregated = working_df.groupby('Материал', as_index=False).agg({
        'количество': 'sum',
        'Сумма_строки': 'sum'
    })
    aggregated['Цена за ед.'] = aggregated['Сумма_строки'] / aggregated['количество']
    aggregated.rename(
        columns={
            'количество': 'Количество',
            'Сумма_строки': 'Сумма'
        },
        inplace=True
    )

    final_columns = ['Материал', 'Количество', 'Цена за ед.', 'Сумма']
    result_df = aggregated[final_columns]

    return result_df

def smeta(df):
    temp_df = df.copy()
    result = (temp_df['количество'] * temp_df['Цена']).sum()
    return result
