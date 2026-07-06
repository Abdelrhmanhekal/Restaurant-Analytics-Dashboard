import pandas as pd
import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=.;'
    'DATABASE=Restaurant_Final;'
    'Trusted_Connection=yes;'
)

csv_files = [
    r'C:\Users\IT\Desktop\Execl shees\Data - Analyst\Excel - Analyst\Data Fields (Excel) Mostafa Hamed\Resturant_Data +10 million -20260514T120404Z-3-001\Resturant_Data +10 million\restaurant1.csv',
    r'C:\Users\IT\Desktop\Execl shees\Data - Analyst\Excel - Analyst\Data Fields (Excel) Mostafa Hamed\Resturant_Data +10 million -20260514T120404Z-3-001\Resturant_Data +10 million\restaurant2.csv',
    r'C:\Users\IT\Desktop\Execl shees\Data - Analyst\Excel - Analyst\Data Fields (Excel) Mostafa Hamed\Resturant_Data +10 million -20260514T120404Z-3-001\Resturant_Data +10 million\restaurant3.csv',
    r'C:\Users\IT\Desktop\Execl shees\Data - Analyst\Excel - Analyst\Data Fields (Excel) Mostafa Hamed\Resturant_Data +10 million -20260514T120404Z-3-001\Resturant_Data +10 million\restaurant4.csv',
    r'C:\Users\IT\Desktop\Execl shees\Data - Analyst\Excel - Analyst\Data Fields (Excel) Mostafa Hamed\Resturant_Data +10 million -20260514T120404Z-3-001\Resturant_Data +10 million\restaurant5.csv',
    r'C:\Users\IT\Desktop\Execl shees\Data - Analyst\Excel - Analyst\Data Fields (Excel) Mostafa Hamed\Resturant_Data +10 million -20260514T120404Z-3-001\Resturant_Data +10 million\restaurant6.csv',
    r'C:\Users\IT\Desktop\Execl shees\Data - Analyst\Excel - Analyst\Data Fields (Excel) Mostafa Hamed\Resturant_Data +10 million -20260514T120404Z-3-001\Resturant_Data +10 million\restaurant7.csv',
]

cursor = conn.cursor()

for file in csv_files:
    print(f'جاري رفع: {file.split(chr(92))[-1]}')
    df = pd.read_csv(file, encoding='utf-8-sig')
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
conn.close()