import requests
import json
import sqlite3
from KEYS import AUTH_KEY

CAT_MESSAGE = '1094389323895410738'

LAST_MESSAGE_ID = '1105839661135441962'


def retrieve_messages(message_id):
    last_message_id = None
    headers = {
        'authorization': AUTH_KEY
    }

    nr = 0
    while nr < 500:
        try:
            if last_message_id is not None:
                message_id = last_message_id
            r = requests.get(
                f'https://discord.com/api/v9/channels/1036394911450280047/messages?after={message_id}&limit=100',
                headers=headers)
            jsonn = json.loads(r.text)

            connection = sqlite3.connect('easterData0905_2.db')
            for value in jsonn:
                try:
                    connection.execute("INSERT INTO easterData (ID, USER_NAME, DESCRIPTION, TIMESTAMP) "
                                       "VALUES(?, ?, ?, ?)",
                                       (value['id'], value['embeds'][0]['title'], value['embeds'][0]['description'],
                                        value['embeds'][0]['timestamp']))
                except IndexError:
                    print('What"s the problem?', value)

            connection.commit()
            connection.close()
            last_message_id = jsonn[0]['id']
            nr += 1
        except IndexError:
            print('All messages printed!')
            break
    print('All the messages till your lucky cat are saved in database. The last message id is: ', last_message_id)


retrieve_messages(LAST_MESSAGE_ID)
