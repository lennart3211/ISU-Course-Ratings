import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("course_data.csv")

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


df = df.rename(columns={'Department(s)': 'department', 'Course Level (Undergraduate or Graduate)': 'course_level', 'Description': 'description', 'Credits/Units - Credits/Units - Min Credits/Units': 'min_credits', 'Credits/Units - Credits/Units - Max Credits/Units': 'max_credits'})
df['course_title'] = df['Subject code'] + " " + df['Catalog Number']
df = df.reset_index(names='course_id')
columns_to_keep = ['course_id', 'course_title', 'department', 'course_level', 'description', 'min_credits', 'max_credits']
df = df.drop(columns=[col for col in df.columns if col not in columns_to_keep])

df['course_materials'] = ""

order = ['course_id', 'course_title', 'department', 'course_level', 'description', 'min_credits', 'max_credits', 'course_materials']
df = df[order]

# print(df.head(10))


PASSWORD = "nco6YZv2LT7cRk14"
connection_string = f"postgresql://postgres.ptgmihcaerrkwjmfcszd:{PASSWORD}@aws-0-us-east-2.pooler.supabase.com:5432/postgres"

engine = create_engine(connection_string)

df.to_sql(
    name="Course Data",
    con=engine, 
    if_exists="replace",  
    index=False, 
)

print("Table successfully uploaded to Supabase!")