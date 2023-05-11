import sqlite3
import re
from datetime import date as date_n


def nr_gifts_received(user_name):
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    nr = 0
    pattern = "@[a-zA-Z0-9\.\-]+ opened (\d+) Golden Egg sent by "

    for row in cursor:
        if re.search(pattern, row[2]):
            match = re.search(pattern, row[2])
            received = int(match.group(1))
            nr += received

    connection.close()
    print(nr)
    return nr


def update_gifts_received():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute('SELECT USER_NAME from userData')

    for row in cursor:
        print(row[0])
        nr_gifts = nr_gifts_received(row[0])
        connection.execute(f'UPDATE userData '
                           f'SET Gifts_Received = {nr_gifts} '
                           f'WHERE USER_NAME = "{row[0]}"')

    connection.commit()
    connection.close()


def gifts_sent(user_name):
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    nr = 0
    pattern = "@([a-zA-Z0-9\.\-]+) sent their daily Golden Eggs to [a-zA-Z0-9@, ]+"

    for row in cursor:
        if re.search(pattern, row[2]):
            nr += 3

    connection.close()
    print(nr)
    return nr


def update_gifts_sent():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute('SELECT USER_NAME from userData')

    for row in cursor:
        print(row[0])
        nr_gifts_sent = gifts_sent(row[0])
        connection.execute(f'UPDATE userData '
                           f'SET Gifts_Sent = {nr_gifts_sent} '
                           f'WHERE USER_NAME = "{row[0]}"')

    connection.commit()
    connection.close()


def golden_eggs_bought(user_name):
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    nr = 0
    pattern = "@[a-zA-Z0-9\.\-]+ bought (\d+) Golden Egg for themselves [a-zA_Z0-9,: ]+"

    for row in cursor:
        if re.search(pattern, row[2]):
            match = re.search(pattern, row[2])
            received = int(match.group(1))
            nr += received

    connection.close()
    print(nr)
    return nr


def update_golden_eggs_bought():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute('SELECT USER_NAME from userData')

    for row in cursor:
        print(row[0])
        nr_golden_eggs_bought = golden_eggs_bought(row[0])
        connection.execute(f'UPDATE userData '
                           f'SET Golden_Eggs_Bought = {nr_golden_eggs_bought} '
                           f'WHERE USER_NAME = "{row[0]}"')

    connection.commit()
    connection.close()


def gifts_exchanged_reward_chest(user_name):
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    nr = 0
    pattern = f"[a-zA-Z0-9\.\-]+ exchanged  \d+ Easter Egg for (\d+) Reward Chest"

    for row in cursor:
        if re.search(pattern, row[2]):
            match = re.search(pattern, row[2])
            reward_chest = int(match.group(1))
            nr += reward_chest

    print(nr)
    connection.close()
    return nr


# gifts_exchanged_reward_chest('somethingfunny')


def update_reward_chest_bought():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute('SELECT USER_NAME from userData')

    for row in cursor:
        print(row[0])
        nr_reward_chest = gifts_exchanged_reward_chest(row[0])
        connection.execute(f'UPDATE userData '
                           f'SET Reward_Chest_Bought = {nr_reward_chest} '
                           f'WHERE USER_NAME = "{row[0]}"')

    connection.commit()
    connection.close()


def easter_eggs_earned(user_name):
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    nr = 0
    pattern = "@?[a-zA-Z0-9\.\-]+ [a-zA-Z0-9 ]+ and earned (\d+) Easter Egg[:|\.]"

    for row in cursor:
        if re.search(pattern, row[2]):
            match = re.search(pattern, row[2])
            earned = int(match.group(1))
            nr += earned
    connection.close()
    print(nr)
    return nr


def update_easter_egg_data():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute("SELECT * from userData")

    for row in cursor:
        print(row[0])
        eggs_value = easter_eggs_earned(row[0])
        connection.execute(f'UPDATE userData '
                           f'SET Easter_Eggs_Earned = {eggs_value} '
                           f'WHERE USER_NAME = "{row[0]}"')

    connection.commit()
    connection.close()


def raffle_points_earned(user_name):
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    nr = 0
    pattern = "@[a-zA-Z0-9\.\-]+ got (\d+?.?\d*) points for the raffle by adding the following cards to the event collection: "

    for row in cursor:
        if re.search(pattern, row[2]):
            match = re.search(pattern, row[2])
            earned = float(match.group(1))
            nr += earned
    connection.close()
    print(nr)
    return nr


def raffle_points_golden_eggs(user_name):
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    nr = 0
    pattern = "@[a-zA-Z0-9\.\-]+ bought (\d+) Golden Egg for @[a-zA_Z0-9]+"

    for row in cursor:
        if re.search(pattern, row[2]):
            match = re.search(pattern, row[2])
            received = float(match.group(1))
            nr += received

    connection.close()
    print(nr)
    return nr


def update_raffle_points():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute("SELECT USER_NAME from userData")

    for row in cursor:
        print(row[0])
        raffle_points_1 = raffle_points_earned(row[0])
        raffle_points_2 = raffle_points_golden_eggs(row[0])
        raffle_points = raffle_points_1 + raffle_points_2
        connection.execute(f'UPDATE userData '
                           f'SET Raffle_Points_Earned = {raffle_points} '
                           f'WHERE USER_NAME = "{row[0]}"')

    connection.commit()
    connection.close()


def update_raffle_points_golden():
    connection = sqlite3.connect('old_data/user_data.db')
    cursor = connection.execute("SELECT USER_NAME from userData")

    nr = 0

    for row in cursor:
        print(row[0])
        raffle_points = raffle_points_golden_eggs(row[0])
        nr += raffle_points

    print(nr)
    connection.close()


def nr_days(d1, d2):
    return (d2 - d1).days


# date_1 = date_n(2023, 4, 9)
date_2 = date_n(2023, 5, 11)


# print(nr_days(date_1, date_2))


def golden_eggs_program_joined(user_name):
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    pattern = "@([a-zA-Z0-9\.\-]+) just got added to the Good Egg Program! You can now receive golden eggs from others and earn 5% extra CROP from all your actions!"

    for row in cursor:
        if re.search(pattern, row[2]):
            joined_date = row[3]
            pattern_2 = "(\d+)-(\d+)-(\d+)"
            match = re.search(pattern_2, joined_date)
            date_joined = date_n(int(match.group(1)), int(match.group(2)), int(match.group(3)))
            nr_of_days_joined = nr_days(date_joined, date_2) + 1
            print(nr_of_days_joined * 3)
            return nr_of_days_joined * 3

    connection.close()

golden_eggs_program_joined('predatork4')


def update_golden_eggs_sent_daily():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute('SELECT * from userData')

    for row in cursor:
        print('name', row[0])
        nr_days_joined = golden_eggs_program_joined(row[0])
        if nr_days_joined is None:
            nr_days_joined = 0
        print('nr days joined', nr_days_joined)
        print('gifts sent', row[3])
        if nr_days_joined != 0 and nr_days_joined == row[3]:
            print('sent daily', row[0])
            full_days = 33
            connection.execute(f'UPDATE userData '
                               f'SET Daily_Gifts_Sent = {full_days} '
                               f'WHERE USER_NAME = "{row[0]}"')
        elif nr_days_joined != 0 and nr_days_joined != row[3]:
            final = row[3] / 3
            connection.execute(f'UPDATE userData '
                               f'SET Daily_Gifts_Sent = {final} '
                               f'WHERE USER_NAME = "{row[0]}"')
        elif nr_days_joined == 0:
            zero_days = 0
            connection.execute(f'UPDATE userData '
                               f'SET Daily_Gifts_Sent = {zero_days} '
                               f'WHERE USER_NAME = "{row[0]}"')

    connection.commit()
    connection.close()


def gifts_exchanged_iron(user_name):
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    nr = 0
    pattern = f"[a-zA-Z0-9\.\-]+ exchanged  \d+ Golden Ticket for (\d+) Iron Ore"

    for row in cursor:
        if re.search(pattern, row[2]):
            match = re.search(pattern, row[2])
            iron_ore = int(match.group(1))
            nr += iron_ore

    print(nr)
    connection.close()
    return nr


def update_gift_iron():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute('SELECT USER_NAME from userData')

    for row in cursor:
        print(row[0])
        nr_iron_ore = gifts_exchanged_iron(row[0])
        connection.execute(f'UPDATE userData '
                           f'SET Iron_Ore_Exchanged = {nr_iron_ore} '
                           f'WHERE USER_NAME = "{row[0]}"')

    connection.commit()
    connection.close()


def gifts_exchanged_fairy(user_name):
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    nr = 0
    pattern = f"[a-zA-Z0-9\.\-]+ exchanged  \d+ Golden Ticket for (\d+) Fairy Garden"

    for row in cursor:
        if re.search(pattern, row[2]):
            match = re.search(pattern, row[2])
            iron_ore = int(match.group(1))
            nr += iron_ore

    print(nr)
    connection.close()
    return nr


# gifts_exchanged_fairy('looftee')


def update_gift_fairy():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute('SELECT USER_NAME from userData')

    for row in cursor:
        print(row[0])
        nr_fairy = gifts_exchanged_fairy(row[0])
        connection.execute(f'UPDATE userData '
                           f'SET Fairy_Garden_Exchanged = {nr_fairy} '
                           f'WHERE USER_NAME = "{row[0]}"')

    connection.commit()
    connection.close()


def gifts_exchanged_beta_packs(user_name):
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    nr = 0
    pattern = f"[a-zA-Z0-9\.\-]+ exchanged  \d+ Golden Ticket for (\d+) Beta Pack"

    for row in cursor:
        if re.search(pattern, row[2]):
            match = re.search(pattern, row[2])
            iron_ore = int(match.group(1))
            nr += iron_ore

    print(nr)
    connection.close()
    return nr


def update_gift_beta_packs():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute('SELECT USER_NAME from userData')

    for row in cursor:
        print(row[0])
        nr_beta_packs = gifts_exchanged_beta_packs(row[0])
        connection.execute(f'UPDATE userData '
                           f'SET Beta_Packs_Exchanged = {nr_beta_packs} '
                           f'WHERE USER_NAME = "{row[0]}"')

    connection.commit()
    connection.close()


def gifts_exchanged_alpha_packs(user_name):
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    nr = 0
    pattern = f"[a-zA-Z0-9\.\-]+ exchanged  \d+ Golden Ticket for (\d+) Alpha Pack"

    for row in cursor:
        if re.search(pattern, row[2]):
            match = re.search(pattern, row[2])
            iron_ore = int(match.group(1))
            nr += iron_ore

    print(nr)
    connection.close()
    return nr


def update_gift_alpha_packs():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute('SELECT USER_NAME from userData')

    for row in cursor:
        print(row[0])
        nr_alpha = gifts_exchanged_alpha_packs(row[0])
        connection.execute(f'UPDATE userData '
                           f'SET Alpha_Packs_Exchanged = {nr_alpha} '
                           f'WHERE USER_NAME = "{row[0]}"')

    connection.commit()
    connection.close()


def gifts_exchanged_king_weed(user_name):
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    nr = 0
    pattern = f"[a-zA-Z0-9\.\-]+ exchanged  \d+ Golden Ticket for (\d+) King Weed"

    for row in cursor:
        if re.search(pattern, row[2]):
            match = re.search(pattern, row[2])
            iron_ore = int(match.group(1))
            nr += iron_ore

    print(nr)
    connection.close()
    return nr


def update_gift_king_weed():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute('SELECT USER_NAME from userData')

    for row in cursor:
        print(row[0])
        nr_king_weed = gifts_exchanged_king_weed(row[0])
        connection.execute(f'UPDATE userData '
                           f'SET King_Weed_Exchanged = {nr_king_weed} '
                           f'WHERE USER_NAME = "{row[0]}"')

    connection.commit()
    connection.close()


def gifts_exchanged_lucky_cat(user_name):
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    nr = 0
    pattern = f"[a-zA-Z0-9\.\-]+ exchanged  \d+ Golden Ticket for (\d+) Lucky Cat"

    for row in cursor:
        if re.search(pattern, row[2]):
            match = re.search(pattern, row[2])
            lucky_cat = int(match.group(1))
            nr += lucky_cat

    print(nr)
    connection.close()
    return nr


def update_gift_lucky_cat():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute('SELECT USER_NAME from userData')

    for row in cursor:
        print(row[0])
        nr_lucky_cat = gifts_exchanged_lucky_cat(row[0])
        connection.execute(f'UPDATE userData '
                           f'SET Lucky_Cat_Exchanged = {nr_lucky_cat} '
                           f'WHERE USER_NAME = "{row[0]}"')

    connection.commit()
    connection.close()


def gifts_exchanged_mystery_seed(user_name):
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    nr = 0
    pattern = f"[a-zA-Z0-9\.\-]+ exchanged  \d+ Easter Egg for (\d+) Mystery Seed"

    for row in cursor:
        if re.search(pattern, row[2]):
            match = re.search(pattern, row[2])
            mystery_seed = int(match.group(1))
            nr += mystery_seed

    print(nr)
    connection.close()
    return nr


def update_gift_mystery_seed():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute('SELECT USER_NAME from userData')

    for row in cursor:
        print(row[0])
        nr_mystery_seed = gifts_exchanged_mystery_seed(row[0])
        connection.execute(f'UPDATE userData '
                           f'SET Mystery_Seed_Exchanged = {nr_mystery_seed} '
                           f'WHERE USER_NAME = "{row[0]}"')

    connection.commit()
    connection.close()


def gifts_exchanged_ferti_plus(user_name):
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    nr = 0
    pattern = f"[a-zA-Z0-9\.\-]+ exchanged  \d+ Easter Egg for (\d+) Ferti-Plus"

    for row in cursor:
        if re.search(pattern, row[2]):
            match = re.search(pattern, row[2])
            mystery_seed = int(match.group(1))
            nr += mystery_seed

    print(nr)
    connection.close()
    return nr


def update_gift_ferti_plus():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute('SELECT USER_NAME from userData')

    for row in cursor:
        print(row[0])
        nr_ferti_plus = gifts_exchanged_ferti_plus(row[0])
        connection.execute(f'UPDATE userData '
                           f'SET Ferti_PLus_Exchanged = {nr_ferti_plus} '
                           f'WHERE USER_NAME = "{row[0]}"')

    connection.commit()
    connection.close()


def gifts_exchanged_speed_gro(user_name):
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    nr = 0
    pattern = f"[a-zA-Z0-9\.\-]+ exchanged  \d+ Easter Egg for (\d+) Speed-Gro"

    for row in cursor:
        if re.search(pattern, row[2]):
            match = re.search(pattern, row[2])
            mystery_seed = int(match.group(1))
            nr += mystery_seed

    print(nr)
    connection.close()
    return nr


def update_gift_speed_gro():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute('SELECT USER_NAME from userData')

    for row in cursor:
        print(row[0])
        nr_speed_gro = gifts_exchanged_speed_gro(row[0])
        connection.execute(f'UPDATE userData '
                           f'SET Speed_Gro_Exchanged = {nr_speed_gro} '
                           f'WHERE USER_NAME = "{row[0]}"')

    connection.commit()
    connection.close()


def get_everything(user_name):
    connection = sqlite3.connect('old_data/easterData26.db')
    cursor = connection.execute(f"SELECT * from easterData WHERE USER_NAME='@{user_name}'")

    nr = 0

    for row in cursor:
        print('ID: ', row[0])
        print('Username: ', row[1])
        print('Description: ', row[2])
        print('Timestamp ', row[3])
        nr += 1

    print(nr)
    connection.close()


def total_user():
    connection = sqlite3.connect('easterData0905_2.db')
    cursor = connection.execute(f"SELECT USER_NAME from easterData")
    total_accounts = set()
    pattern = "@([0-9a-zA-Z\.\-]+)"
    for row in cursor:
        match = re.search(pattern, row[0])
        total_accounts.add(match.group(1))
    connection.close()
    print(total_accounts)
    print(len(total_accounts))
    connection2 = sqlite3.connect('user_data_new.db')
    for account in total_accounts:
        connection2.execute('INSERT INTO userData (USER_NAME) VALUES(?)', (account,))
        print(account)

    connection2.commit()
    connection2.close()


def calculate_easter_eggs_earned():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute("SELECT Easter_Eggs_Earned from userData")

    total_points = 0

    for row in cursor:
        total_points += row[0]

    connection.close()
    return total_points


def calculate_gifts_received():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute("SELECT Gifts_Received from userData")

    total_points = 0

    for row in cursor:
        total_points += row[0]

    connection.close()
    return total_points


def calculate_gifts_sent():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute("SELECT Gifts_Sent from userData")

    total_points = 0

    for row in cursor:
        total_points += row[0]

    connection.close()
    return total_points


def calculate_raffle_points():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute("SELECT Raffle_Points_Earned from userData")

    total_points = 0

    for row in cursor:
        total_points += row[0]

    connection.close()
    return total_points


def calculate_golden_eggs_bought():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute("SELECT Golden_Eggs_Bought from userData")

    total_points = 0

    for row in cursor:
        total_points += row[0]

    connection.close()
    return total_points


def calculate_reward_chest_exchanged():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute("SELECT Reward_Chest_Bought from userData")

    total_points = 0

    for row in cursor:
        total_points += row[0]

    connection.close()
    return total_points


def calculate_mystery_seed_exchanged():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute("SELECT Mystery_Seed_Exchanged from userData")

    total_points = 0

    for row in cursor:
        total_points += row[0]

    connection.close()
    return total_points


def calculate_ferti_plus_exchanged():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute("SELECT Ferti_PLus_Exchanged from userData")

    total_points = 0

    for row in cursor:
        total_points += row[0]

    connection.close()
    return total_points


def calculate_speed_gro_exchanged():
    connection = sqlite3.connect('user_data_new.db')
    cursor = connection.execute("SELECT Speed_Gro_Exchanged from userData")

    total_points = 0

    for row in cursor:
        total_points += row[0]

    connection.close()
    return total_points
