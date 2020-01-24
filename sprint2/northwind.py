# PART 2

# Importing sqlite3
import sqlite3

# Creating the connection
sl2_conn = sqlite3.connect('northwind_small.sqlite3')
# Creating the cursor
sl2_curs = sl2_conn.cursor()

# Creating query to see ten most expensive items in database
query = """SELECT UnitPrice, ProductName
        FROM Product
        ORDER BY UnitPrice DESC
        LIMIT 10;
        """
# Executing the query
most_expensive = sl2_curs.execute(query).fetchall()
print('ten most expensive items in database')
print(most_expensive)
print(" ")

# Creating a query to return averageage of employee based off time of hire
query2 = """SELECT HireDate, BirthDate
        From Employee
        """
# Executing query
time_hire = sl2_curs.execute(query2).fetchall()
# Creating empty list
empt_list = []
# Creating for loop to disect the string the database returned
for i in time_hire:
    x = int(i[0][0:4])-int(i[1][0:4])
    empt_list.append(x)

# Finding the average
average = sum(empt_list)/len(empt_list)
# Printing the result
print('averageage of employee based off time of hire')
print(average)
print(" ")

# Part 3

# Creating a query to return ten most expensive items joined with supplier
q = """SELECT p.UnitPrice, p.ProductName, s.CompanyName, p.ID, s.ID
    FROM Product AS p,
    Supplier AS s
    JOIN Product ON s.ID = p.SupplierID
    GROUP BY p.ProductName
    ORDER BY p.UnitPrice DESC
    LIMIT 10;
    """
# Printing the names of columns to be returned
print('ten most expensive items joined with supplier')
print(' ')
print('Unit Price, Product Name, Supplier, Product ID, Supplier ID')
print(" ")
# Executing query
expensive_supply = sl2_curs.execute(q).fetchall()
# Printing results
print(expensive_supply)
print(" ")

# Creating new query to return the largest category by uniqe products in it
q2 = """SELECT c.CategoryName, COUNT(p.CategoryID)
    FROM Product AS p,
    Category AS c
    JOIN Product ON c.ID = p.CategoryID
    GROUP BY p.CategoryID, c.CategoryName
    """
# Executing query
count = sl2_curs.execute(q2).fetchall()
# Printing results
print('the largest category by uniqe products in it')
print(count)
print(" ")
# Summerizing results
print('Based off the query the Category with max unique values is ' +
      str(count[2]))
print(" ")
