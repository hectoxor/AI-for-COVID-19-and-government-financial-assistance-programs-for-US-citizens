label_encoders = {}
label_encoders = {}
for column_name in df_copy.columns:
    label_encoders[column_name] = LabelEncoder()
    df_copy[column_name] = label_encoders[column_name].fit_transform(df_copy[column_name])
    label_map=dict(zip(label_encoders[column_name].classes_, label_encoders[column_name].transform(label_encoders[column_name].classes_)))
    if '?' in label_map.keys():
        df_copy[column_name] = df_copy[column_name].replace(label_map['?'], np.NaN)
df_copy.head()
