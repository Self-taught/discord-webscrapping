import requests
import json
import sqlite3
import re
from KEYS import AUTH_KEY

pr_fairy_garden = 145
pr_king_weed = 39.90
pr_iron_ore = 8.20
pr_gold_ore = 4.89
pr_alpha_packs = 7
pr_beta_packs = 6.9

all_data = []


# , user_Name_Raffle
def raffle_data(message_id):
    last_message_id = None
    headers = {
        'authorization': AUTH_KEY
    }

    nr = 0
    msg_nr = 1

    while nr < 10:
        try:
            if last_message_id is not None:
                message_id = last_message_id
            r = requests.get(
                f'https://discord.com/api/v9/channels/830913369401065476/messages?after={message_id}&limit=100',
                headers=headers)
            jsonn = json.loads(r.text)

            connection = sqlite3.connect('user_data_new.db')
            try:
                for value in jsonn:
                    if value['author']['username'] == 'dCrops':
                        raffle_message = value['embeds'][0]['description']
                        each_message = raffle_message.split("\n")
                        for m in each_message:
                            print(msg_nr, m)
                            connection.execute("INSERT INTO raffleDataAll (NR, Message) VALUES (?, ?)", (msg_nr, m))
                            msg_nr += 1
                        # for m in raffle_message:
                        #     print(m)
                connection.commit()
                connection.close()


            #         packs_bought = int(match.group(2))
            #         connection.execute("INSERT INTO packsData (ID, USER_NAME, DESCRIPTION, TIMESTAMP, PACKS_BOUGHT) "
            #                            "VALUES(?, ?, ?, ?, ?)",
            #                            (value['id'], user_name, value['content'], value['timestamp'], packs_bought))
            except AttributeError:
                print('What"s the problem?', value)

            nr += 1

            last_message_id = jsonn[0]['id']
        #
        #     print(jsonn)
        #     if last_message_id == "1106099522456801383":
        #         print('Last message reached.', last_message_id)
        #         break
        except IndexError:
            print("All messages printed, the last message id is: ")
            break;

    print(all_data)
    return all_data


first_message_id = "https://discord.com/channels/830913369401065472/830913369401065476/1110532212761317486"


# raffle_data('1110532212761317486')


def add_user_name_raffle():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute('SELECT * FROM userData')

    for row in cursor:
        if row[4] > 0:
            connection.execute('INSERT INTO raffleData (USER_NAME, Raffle_Points) '
                               'VALUES (?, ?)',
                               (row[0], row[4])
                               )
            print(f'{row[0]}: {row[4]}')
    connection.commit()
    connection.close()


def add_data():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute("SELECT * FROM raffleData")

    total = 0
    # pr_fairy_garden = 145
    # pr_king_weed = 39.90
    # pr_iron_ore = 8.20
    # pr_gold_ore = 4.89
    # pr_alpha_packs = 7
    # pr_beta_packs = 6.9

    for users in cursor:
        print(users[0])
        print(users[1])
        # if users[10] > 0 :
        p_user = (abs(users[9])/users[1]) * 100
        p_user = round(p_user, 2)
        if users[9] > 0:
            p_percnt = f'{p_user}%'
        elif users[9] < 0:
            p_percnt = f'-{p_user}%'
        print(p_user)
        print(p_percnt)
        # p_hive = users[9] - users[1]
        # total_hive_earned = (pr_fairy_garden * float(users[2])) + (pr_king_weed * float(users[3])) + (pr_iron_ore * float(users[4])) + \
        #                     (pr_gold_ore * float(users[5])) + (pr_alpha_packs * (users[6])) + (pr_beta_packs * float(users[7]))
        # current_prize = prizes(users[0])

        connection.execute(f"UPDATE raffleData "
                           f"SET Profit_Loss_Percentage = ? "
                           f"WHERE USER_NAME = ?", (p_percnt, users[0]))
        # print(users[0], ":", current_prize)
        # total += total_hive_earned

    # print(total)
    connection.commit()
    connection.close()


def prizes(user_raffle):
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute("SELECT Message FROM raffleDataAll")

    nr = 0
    for row in cursor:
        pattern = "@([a-zA-Z0-9.-]+) won 1X ([a-zA-Z ]+)!"

        match = re.search(pattern, row[0])
        user_name = match.group(1)
        prize = match.group(2)
        if user_name == user_raffle and prize == "Beta Pack":
            nr += 1
            print(user_name, ":", prize)

    connection.close()
    print(nr)
    return nr


add_data()

# def profit_loss():
