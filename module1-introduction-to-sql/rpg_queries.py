import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

# creating a query to return total amount of characters
query_char_total = '''SELECT character_id
FROM charactercreator_character;'''

curs.execute(query_char_total)
total = curs.fetchall()
print('total character count is ' + str(len(total)))

# creating a query to return how many of each specific subclass
"""
query_subclass = '''
                  select((SELECT COUNT(charactercreator_cleric))
                         (SELECT COUNT(charactercreator_fighter))
                         (SELECT COUNT(charactercreator_mage))
                         (SELECT COUNT(charactercreator_their)))
                 '''

curs.execute(query_subclass)
total_subclass = curs.fetchone()
total_subclass
"""

# creating a query to return total amount of items
query_item_total = '''SELECT item_id
FROM armory_item;'''

curs.execute(query_item_total)
item_total = curs.fetchall()
print('total item count is ' + str(len(item_total)))

# creating a query to return amount of items that are weapons
query_weapon = '''SELECT name
FROM armory_item, armory_weapon
WHERE item_id = item_ptr_id;'''

curs.execute(query_weapon)
weapon_total = curs.fetchall()
print(str(len(weapon_total)) + ' is the amount of items that are weapons '
      + str(len(item_total) - len(weapon_total))
      + ' is the amount of items that are not weapons. ')

# creating a query to return how many items each character has (first 20)
query_char_items = '''SELECT cc.character_id, cc.name AS character_name, COUNT(ai.item_id)
FROM charactercreator_character AS cc,
armory_item AS ai,
charactercreator_character_inventory AS cci
WHERE cc.character_id = cci.character_id
AND ai.item_id = cci.item_id
GROUP BY cc.name
ORDER BY cc.name
LIMIT 20;'''

curs.execute(query_char_items)
char_items_total = curs.fetchall()
print('the char id, char name, and item counts of first 20 characters is'
      + str(char_items_total))

# creating a query to return how many weapons each character has (first 20)
query_char_weapon_count = '''SELECT cc.character_id, cc.name AS character_name, COUNT(aw.item_ptr_id) AS weapon_count
FROM charactercreator_character AS cc,
armory_item AS ai,
charactercreator_character_inventory AS cci,
armory_weapon AS aw
WHERE cc.character_id = cci.character_id
AND ai.item_id = cci.item_id
AND ai.item_id = aw.item_ptr_id
GROUP BY cc.name
ORDER BY cc.name
LIMIT 20;'''

curs.execute(query_char_weapon_count)
char_weapon_total = curs.fetchall()
print('weapon count for each character ' + str(char_weapon_total))

# average number of items each char has

d = []
for i in char_items_total:
    key,test,val = i
    d.append(val)
test = sum(d)/len(d)
print('The average number of items each character has is ' + str(test))

# average number of weapons each char has

d = []
for i in char_weapon_total:
    key,test,val = i
    d.append(val)
test = sum(d)/len(d)
print('The average number of weapons each character has is ' + str(test))
