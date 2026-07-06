import pandas as pd
import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=.;'
    'DATABASE=Restaurant_Final;'
    'Trusted_Connection=yes;'
)

json_files = [
    r'C:\Users\IT\Desktop\Execl shees\Data - Analyst\Excel - Analyst\Data Fields (Excel) Mostafa Hamed\Resturant_Data +10 million -20260514T120404Z-3-001\json\restaurant_json1.json',
    r'C:\Users\IT\Desktop\Execl shees\Data - Analyst\Excel - Analyst\Data Fields (Excel) Mostafa Hamed\Resturant_Data +10 million -20260514T120404Z-3-001\json\restaurant_json2.json'
]

cursor = conn.cursor()

for file in json_files:
    print(f'جاري رفع: {file.split(chr(92))[-1]}')
    df = pd.read_json(file, encoding='utf-8-sig')
    for chunk_start in range(0, len(df), 5000):
        chunk = df.iloc[chunk_start:chunk_start+5000]
        rows = [tuple(row) for row in chunk.itertuples(index=False)]
        cursor.executemany(
            "INSERT INTO dbo.Restaurant_Final VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            rows
        )
        conn.commit()
        print(f'  تم رفع {chunk_start + len(chunk):,} صف')
    print(f'✅ خلص: {file.split(chr(92))[-1]}')

print('كل الداتا اتحملت!')
conn.clos