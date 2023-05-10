import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(layout="wide")
st.title('Easter 2023 Dcrops')
st.subheader("Find a single user or compare two users data")
user_name = st.text_input('Find A User Data', key='user_name', placeholder="To compare two users, type user1,user2 withour any space")


# Columns = USER_NAME, Easter_Eggs_Earned, Gifts_Received, Gifts_Sent, "
#               f"Raffle_Points_Earned, Daily_Gifts_Sent, Golden_Eggs_Bought, Reward_Chest_Bought,"
#               f"Iron_Ore_Exchanged, Fairy_Garden_Exchanged, Beta_Packs_Exchanged, Alpha_Packs_Exchanged,"
#               f"King_Weed_Exchanged FROM userData

def load_data():
    # Connect to the database
    conn = sqlite3.connect("user_data_new.db")
    c = conn.cursor()

    # Select the necessary columns for the current user
    c.execute(f"SELECT * from userData")
    rows = c.fetchall()

    # Close the connection
    conn.close()

    # Convert the data to a DataFrame
    df = pd.DataFrame(rows, columns=["USER_NAME", "Easter_Eggs_Earned", "Gifts_Received", "Gifts_Sent",
                                     "Raffle_Points_Earned", "Daily_Gifts_Sent", "Golden_Eggs_Bought", "Reward_Chest_Bought",
                                     "Iron_Ore_Exchanged", "Fairy_Garden_Exchanged", "Beta_Packs_Exchanged", "Alpha_Packs_Exchanged",
                                     "King_Weed_Exchanged"])

    st.dataframe(df, use_container_width=True, width=500, height=500)


def load_data_single(user_name):
    # Connect to the database
    conn = sqlite3.connect("user_data_new.db")
    c = conn.cursor()

    # Select the necessary columns for the current user
    c.execute(f"SELECT * from userData WHERE USER_NAME='{user_name}'")
    rows = c.fetchall()

    # Close the connection
    conn.close()

    # Convert the data to a DataFrame
    df = pd.DataFrame(rows, columns=["USER_NAME", "Easter_Eggs_Earned", "Gifts_Received", "Gifts_Sent",
                                     "Raffle_Points_Earned", "Daily_Gifts_Sent", "Golden_Eggs_Bought",
                                     "Reward_Chest_Bought",
                                     "Iron_Ore_Exchanged", "Fairy_Garden_Exchanged", "Beta_Packs_Exchanged",
                                     "Alpha_Packs_Exchanged",
                                     "King_Weed_Exchanged"])

    st.dataframe(df, use_container_width=True, width=500, height=500)


def load_data_multiple(user_name1, user_name2):
    # Connect to the database
    conn = sqlite3.connect("user_data_new.db")
    c = conn.cursor()

    # Select the necessary columns for the current user
    c.execute(f"SELECT * from userData WHERE USER_NAME IN ('{user_name1}', '{user_name2}')")
    rows = c.fetchall()

    # Close the connection
    conn.close()

    # Convert the data to a DataFrame
    df = pd.DataFrame(rows, columns=["USER_NAME", "Easter_Eggs_Earned", "Gifts_Received", "Gifts_Sent",
                                     "Raffle_Points_Earned", "Daily_Gifts_Sent", "Golden_Eggs_Bought",
                                     "Reward_Chest_Bought",
                                     "Iron_Ore_Exchanged", "Fairy_Garden_Exchanged", "Beta_Packs_Exchanged",
                                     "Alpha_Packs_Exchanged",
                                     "King_Weed_Exchanged"])

    st.dataframe(df, use_container_width=True, width=500, height=500)


if user_name:
    if ',' in user_name:
        users = user_name.split(',')
        print(users)
        load_data_multiple(users[0], users[1])
    else:
        print(user_name)
        load_data_single(user_name)
else:
    load_data()

st.text('The daily gifts sent are 32 max for those who sent daily. For others, it"s No. of Missed days = 32 - days sent you sent gift.')