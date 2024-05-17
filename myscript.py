import psycopg2
import matplotlib.pyplot as mp
import numpy as np

con = psycopg2.connect("dbname=naz225 user=postgres password=postgres host=localhost port=2024")
cur = con.cursor()

cur.execute("SELECT x, y FROM lab_view.fn ORDER BY x;")

arr = cur.fetchall()

cur.close()
cur.close()

x,y = np.array(arr).T

mp.plot(x,y)

mp.title('sine wave')
mp.xlabel('x')
mp.ylabel('y = sin(x)')

mp.grid(True, which='both')
mp.axhline(y=0, color='k')

mp.show()