# -*- coding: utf-8 -*-
"""demo_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HQTXywuCZVLNNOL2uqNzwDMDSMLtAIY_
"""
# Importing sqlite3
import sqlite3

# When working in notebook was used to reset
# sl_conn.close()

# Creating a new connection to demo_data
sl_conn = sqlite3.connect('demo_data.sqlite3')

# Creating a cursor
sl_curs = sl_conn.cursor()

# Creating the demo table
create_demo_table = """
CREATE TABLE demo (
  s VARCHAR(1),
  x INT,
  y INT
);
"""

# Executing the demo table
sl_curs.execute(create_demo_table)

# Creating list of tuples to be inserted into table
test2 = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]

# Using a for loop and INSERT INTO to add the list of values
for i in test2:
    insert_var = '''
    INSERT INTO demo
    (s,x,y)
    VALUES ''' + str(i[0:]) + ';'
    sl_curs.execute(insert_var)

# Creating a querie to view total rows of table
querie = """SELECT COUNT(*) FROM demo"""
# Executing querie
total_rows = sl_curs.execute(querie).fetchall()
# Printing the results
print('total rows of table')
print(total_rows)
print(' ')

# Creating a querie to test how many rows where x and y are at least 5
querie2 = """SELECT COUNT(*)
          FROM demo
          WHERE x >= 5
          AND y >=5;
          """
# Executing querie
x_y_rows = sl_curs.execute(querie2).fetchall()
# Printing the results
print('how many rows where x and y are at least 5')
print(x_y_rows)
print(' ')


# Creating a querie to test the unique values of y
querie3 = """SELECT COUNT(DISTINCT y)
          FROM demo
          """
# Exicuting querie
uniqe_vales = sl_curs.execute(querie3).fetchall()
# Printing the results
print('the unique values of y')
print(uniqe_vales)
