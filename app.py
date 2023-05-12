import sqlite3

# CREATE A TABLE FOR DISCORD DATA ALL

# connection = sqlite3.connect('easterData0905_2.db')
# connection.execute('''CREATE TABLE easterData
# (ID TEXT PRIMARY KEY NOT NULL,
# USER_NAME TEXT NOT NULL,
# DESCRIPTION TEXT NOT NULL,
# TIMESTAMP TEXT NOT NULL);
# ''')
#
# connection.close()


# CREATE A TABLE FOR USER DATABASE

# connection = sqlite3.connect('user_data_new.db')
# connection.execute('''CREATE TABLE userData
# (USER_NAME TEXT PRIMARY KEY NOT NULL);
# ''')
#
# connection.close()


# connection = sqlite3.connect('user_data_new.db')
# connection.execute('''ALTER TABLE userData
# ADD Speed_Gro_Exchanged INT;
# ''')
#
# connection.close()


# CREATE A TABLE FOR Packs Bought

# connection = sqlite3.connect('packs_data_event.db')
# connection.execute('''ALTER TABLE userPacksData
# ADD Packs_Bought INT;
# ''')
# connection.commit()
# connection.close()

# connection = sqlite3.connect('packs_data_event.db')
# connection.execute('''ALTER TABLE packsData
# ADD Packs_Bought INT;
# ''')
#
# connection.close()