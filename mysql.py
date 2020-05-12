import pandas as pd
import pymysql


conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '111111',
    db = 'hyj',
    port=3306,
    charset = 'utf8'
                       )

df = pd.read_sql('select *  from user',conn)
print(df.head())


df.to_excel(r'F:\python\excel\mysql.xlsx',index=False,header=True,columns=None)
print("导出完成")
