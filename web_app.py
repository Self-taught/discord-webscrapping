import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from update_user_data import calculate_easter_eggs_earned, calculate_gifts_received, calculate_gifts_sent, \
    calculate_raffle_points, calculate_reward_chest_exchanged, calculate_golden_eggs_bought, \
    calculate_mystery_seed_exchanged, calculate_ferti_plus_exchanged, calculate_speed_gro_exchanged, total_packs_bought

total_easter_eggs = calculate_easter_eggs_earned()
total_gifts_received = calculate_gifts_received()
total_gifts_sent = calculate_gifts_sent()
total_raffle_points = calculate_raffle_points()
total_reward_chest_exchanged = calculate_reward_chest_exchanged()
total_golden_eggs_bought = calculate_golden_eggs_bought()
total_mystery_seed_exchanged = calculate_mystery_seed_exchanged()
total_ferti_plus_exchanged = calculate_ferti_plus_exchanged()
total_speed_gro_exchanged = calculate_speed_gro_exchanged()
total_packs_bought = total_packs_bought()


column_data = ["USER_NAME", "Easter_Eggs_Earned", "Gifts_Received", "Gifts_Sent",
               "Raffle_Points_Earned", "Daily_Gifts_Sent", "Golden_Eggs_Bought", "Reward_Chest_Bought",
               "Iron_Ore_Exchanged", "Fairy_Garden_Exchanged", "Beta_Packs_Exchanged", "Alpha_Packs_Exchanged",
               "King_Weed_Exchanged", "Lucky_Cat_Exchanged", "Mystery_Seed_Exchanged",
               "Ferti_Plus_Exchanged", "Speed_Gro_Exchanged"]

column_data_raffle = ["USER_NAME", "Raffle_Points", "Fairy_Garden", "King_Weed", "Iron_Ore",
                      "Gold_Ore", "Alpha_Packs", "Beta_Packs",
                      "Hive_Earned", "Profit_Loss_Hive", "Profit_Loss_Percentage"]


st.set_page_config(layout="wide")
st.title('Easter 2023 Dcrops')

with st.expander("Collective Data"):
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"Total Easter Eggs Earned: {total_easter_eggs}")
        st.warning(f"Total Gifts Received: {total_gifts_received}")
        st.info(f"Total Reward Chest Exchanged: {total_reward_chest_exchanged}")
        st.success(f"Total Golden Eggs Bought: {total_golden_eggs_bought}")
        st.info(f"Total Beta Packs Bought From Shop During The Event: {total_packs_bought}")
    with col2:
        st.success(f"Total Accounts Participated in the event: 618")
        st.info(f"Total Raffle Points Earned: {total_raffle_points}")
        st.success(f"Total Mystery Seed Exchanged: {total_mystery_seed_exchanged}")
        st.warning(f"Total Ferti Plus Exchanged: {total_ferti_plus_exchanged}")
        st.info(f"Total Speed Gro Exchanged: {total_speed_gro_exchanged}")


# ....................................................................................

st.subheader("Raffle Data Analysis")

st.info('To figure out profit/loss, raffle points are considered = 1 hive.'
        ' Most people sent beta common recipies to earn raffle points which were selling at 0.25-0.27 hive. '
        '')
st.success('To Calculate hive earned and profit/loss => Current price of an item in the market X no of items won during '
           'raffle')

col_1, col_2 = st.columns(2)

with col_1:
    st.warning('Fairy Garden = 145 hive')
    st.warning('King Weed = 39.90 hive')
    st.warning('Iron Ore = 8.20 hive')

with col_2:
    st.warning('Gold Ore = 4.89 hive')
    st.warning('Alpha Pack = 7')
    st.warning('Beta Pack = 6.9 hive')



user_name_raffle = st.text_input('Find A User Data', key='user_name_raffle', placeholder="To compare two users, type user1,user2 withour any space")

def load_data_raffle():
    # Connect to the database
    conn = sqlite3.connect("user_data_new.db")
    c = conn.cursor()

    # Select the necessary columns for the current user
    c.execute(f"SELECT * from raffleData")
    rows = c.fetchall()

    # Close the connection
    conn.close()

    # Convert the data to a DataFrame
    df = pd.DataFrame(rows, columns=column_data_raffle)
    df = df.sort_values(by=["Raffle_Points"], ascending=False)

    st.dataframe(df, use_container_width=True, width=500, height=500)


def load_data_single_raffle(user_name_):
    # Connect to the database
    conn = sqlite3.connect("user_data_new.db")
    c = conn.cursor()

    # Select the necessary columns for the current user
    c.execute(f"SELECT * from raffleData WHERE USER_NAME='{user_name_}'")
    rows = c.fetchall()

    # Close the connection
    conn.close()

    # Convert the data to a DataFrame
    df = pd.DataFrame(rows, columns=column_data_raffle)
    df = df.sort_values(by=["Raffle_Points"], ascending=False)

    st.dataframe(df, use_container_width=True, width=500, height=500)


def load_data_multiple_raffle(user_name1, user_name2):
    # Connect to the database
    conn = sqlite3.connect("user_data_new.db")
    c = conn.cursor()

    # Select the necessary columns for the current user
    c.execute(f"SELECT * from raffleData WHERE USER_NAME IN ('{user_name1}', '{user_name2}')")
    rows = c.fetchall()

    # Close the connection
    conn.close()

    # Convert the data to a DataFrame
    df = pd.DataFrame(rows, columns=column_data_raffle)
    df = df.sort_values(by=["Raffle_Points"], ascending=False)

    st.dataframe(df, use_container_width=True, width=500, height=500)


if user_name_raffle:
    if ',' in user_name_raffle:
        users = user_name_raffle.split(',')
        print(users)
        load_data_multiple_raffle(users[0], users[1])
    else:
        print(user_name_raffle)
        load_data_single_raffle(user_name_raffle)
else:
    load_data_raffle()

# ....................................................................................

st.subheader("Find a single user or compare two users data")
user_name = st.text_input('Find A User Data', key='user_name', placeholder="To compare two users, type user1,user2 "
                                                                           "without any space")

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
    df = pd.DataFrame(rows, columns=column_data)
    df = df.sort_values(by=["Easter_Eggs_Earned"], ascending=False)

    st.dataframe(df, use_container_width=True, width=500, height=500)


def load_data_single(user_name_):
    # Connect to the database
    conn = sqlite3.connect("user_data_new.db")
    c = conn.cursor()

    # Select the necessary columns for the current user
    c.execute(f"SELECT * from userData WHERE USER_NAME='{user_name_}'")
    rows = c.fetchall()

    # Close the connection
    conn.close()

    # Convert the data to a DataFrame
    df = pd.DataFrame(rows, columns=column_data)
    df = df.sort_values(by=["Easter_Eggs_Earned"], ascending=False)

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
    df = pd.DataFrame(rows, columns=column_data)
    df = df.sort_values(by=["Easter_Eggs_Earned"], ascending=False)

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


def load_charts():
    # Connect to the database
    conn = sqlite3.connect("user_data_new.db")
    c = conn.cursor()

    # Select the necessary columns for the current user
    c.execute(f"SELECT * from userData")
    rows = c.fetchall()

    # Close the connection
    conn.close()

    # Top 20 Easter Eggs Earners
    df_easter_eggs = pd.DataFrame(rows, columns=column_data)
    df_easter_eggs = df_easter_eggs.sort_values(by=["Easter_Eggs_Earned"], ascending=False)
    df_easter_eggs = df_easter_eggs.head(20)

    fig = plt.figure(figsize=(28, 12))
    # make bar plot with matplotlib
    plt.bar('USER_NAME', 'Easter_Eggs_Earned', data=df_easter_eggs)
    plt.xlabel("USER_Name", size=15)
    plt.ylabel("Easter_Eggs_Earned", size=15)
    plt.title("Top 20 Easter Eggs Earner", size=24)
    st.pyplot(fig)

    # Top 20 Reward Chest Exchanged
    # Convert the data to a DataFrame
    df_reward_chest = pd.DataFrame(rows, columns=column_data)
    df_reward_chest = df_reward_chest.sort_values(by=["Reward_Chest_Bought"], ascending=False)
    df_reward_chest = df_reward_chest.head(20)

    fig = plt.figure(figsize=(26, 12))
    # make bar plot with matplotlib
    plt.bar('USER_NAME', 'Reward_Chest_Bought', data=df_reward_chest)
    plt.xlabel("USER_Name", size=15)
    plt.ylabel("Reward_Chest_Exchanged", size=15)
    plt.title("Top 20 Reward Chest Exchangers", size=24)
    st.pyplot(fig)

    # Top 20 Gifts Received
    # Convert the data to a DataFrame
    df_gifts_received = pd.DataFrame(rows, columns=column_data)
    df_gifts_received = df_gifts_received.sort_values(by=["Gifts_Received"], ascending=False)
    df_gifts_received = df_gifts_received.head(20)

    fig = plt.figure(figsize=(26, 12))
    # make bar plot with matplotlib
    plt.bar('USER_NAME', 'Gifts_Received', data=df_gifts_received)
    plt.xlabel("USER_Name", size=15)
    plt.ylabel("Gifts_Received", size=15)
    plt.title("Top 20 Gift_Receiver", size=24)
    st.pyplot(fig)

    # Top 20 Golden Eggs Bought
    # Convert the data to a DataFrame
    df_golden_eggs = pd.DataFrame(rows, columns=column_data)
    df_golden_eggs = df_golden_eggs.sort_values(by=["Golden_Eggs_Bought"], ascending=False)
    df_golden_eggs = df_golden_eggs.head(20)

    fig = plt.figure(figsize=(26, 12))
    # make bar plot with matplotlib
    plt.bar('USER_NAME', 'Golden_Eggs_Bought', data=df_golden_eggs)
    plt.xlabel("USER_Name", size=15)
    plt.ylabel("Golden_Eggs_Bought", size=15)
    plt.title("Top 20 Golden_Eggs_Buyer", size=24)
    st.pyplot(fig)

    # Top 20 Raffle Points Standings
    # Convert the data to a DataFrame
    df_raffle_points = pd.DataFrame(rows, columns=column_data)
    df_raffle_points = df_raffle_points.sort_values(by=["Raffle_Points_Earned"], ascending=False)
    df_raffle_points = df_raffle_points.head(20)

    fig = plt.figure(figsize=(28, 12))
    # make bar plot with matplotlib
    plt.bar('USER_NAME', 'Raffle_Points_Earned', data=df_raffle_points)
    plt.xlabel("USER_Name", size=15)
    plt.ylabel("Raffle_Points_Earned", size=15)
    plt.title("Top 20 Raffle_Points_Standings", size=24)
    st.pyplot(fig)


with st.expander("Chart Fun"):
    load_charts()