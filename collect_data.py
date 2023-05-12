import requests
import json
import sqlite3
import re
from KEYS import AUTH_KEY

CAT_MESSAGE = '1094389323895410738'

LAST_MESSAGE_ID = '1106100401624854559'


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


# retrieve_messages(LAST_MESSAGE_ID)


First_Beta_Pack = "https://discord.com/channels/830913369401065472/833367792916889650/1094372531558952980"
Last_Beta_Pack = "https://discord.com/channels/830913369401065472/833367792916889650/1106099522456801383"


def beta_packs_bought(message_id):
    last_message_id = None
    headers = {
        'authorization': AUTH_KEY
    }

    nr = 0

    while nr < 100:
        try:
            if last_message_id is not None:
                message_id = last_message_id
            r = requests.get(
                f'https://discord.com/api/v9/channels/833367792916889650/messages?after={message_id}&limit=100',
                headers=headers)
            jsonn = json.loads(r.text)

            pattern = "@([a-zA-Z0-9\.\-]+) bought \d+ \+ \d+[a-zA-Z\(\)\= ]+(\d+) packs! Paid:"

            connection = sqlite3.connect('packs_data_event.db')

            try:
                for value in jsonn:
                    match = re.search(pattern, value['content'])
                    user_name = match.group(1)
                    packs_bought = int(match.group(2))
                    connection.execute("INSERT INTO packsData (ID, USER_NAME, DESCRIPTION, TIMESTAMP, PACKS_BOUGHT) "
                                       "VALUES(?, ?, ?, ?, ?)",
                                       (value['id'], user_name, value['content'], value['timestamp'], packs_bought))
            except AttributeError:
                print('What"s the problem?', value['content'])

            connection.commit()
            connection.close()

            last_message_id = jsonn[0]['id']

            print(jsonn)
            nr += 1
            if last_message_id == "1106099522456801383":
                print('Last message reached.', last_message_id)
                break
        except IndexError:
            print("All messages printed, the last message id is: ", last_message_id)
            break


# beta_packs_bought("1094372531558952980")