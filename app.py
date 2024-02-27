# app.py

import streamlit as st
import pandas as pd
import sqlite3

def initialize_db():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_contributions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            contribution TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_contribution(username, contribution):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_contributions (username, contribution) VALUES (?, ?)', (username, contribution))
    conn.commit()
    conn.close()

def get_user_contributions(username):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user_contributions WHERE username=?', (username,))
    contributions = cursor.fetchall()
    conn.close()
    return contributions

def download_contributions(username, contributions):
    df = pd.DataFrame(contributions, columns=['ID', 'Username', 'Contribution', 'Timestamp'])
    #df.to_csv(f'{username}_contributions.csv', index=False)

def get_leaderboard():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT username, COUNT(*) as contributions_count
        FROM user_contributions
        GROUP BY username
        ORDER BY contributions_count DESC
        LIMIT 5
    ''')
    leaderboard = cursor.fetchall()
    conn.close()
    return leaderboard

def main():
    st.title("SEA Data Collection App")

    initialize_db()

    # Feature 1: Interactive Challenge
    st.header("Language Challenge")
    phrase = st.text_input("Enter a phrase in your native language:")
    if phrase:
        st.selectbox("What SEA language is this?",['Burmese', 'Khmer', 'Lao', 'Thai', 'Vietnamese', 'Indonesian', 'Malay', 'Tagalog', 'Cebuano', 'Ilocano', 'Javanese', 'Sundanese', 'Bisaya', 'Hiligaynon', 'Waray', 'Chamorro', 'Lakota', 'Tetum', 'Batak', 'Karen', 'Hmong', 'Malagasy', 'Acehnese', 'Minangkabau', 'Buginese', 'Makassarese', 'Toraja', 'Dayak', 'Iban', 'Kadazan', 'Dusun', 'Murut', 'Bidayuh', 'Melanau', 'Kelabit', 'Ibanag', 'Tausug', 'Maguindanao', 'Maranao', 'Yakan', 'Moro', 'Chavacano', 'Igorot', 'Aeta', 'Manobo', 'Bikol', 'Ilonggo', 'Pangasinan', 'Kapampangan', 'Yami', 'Saisiyat', 'Atayal', 'Bunun', 'Tsou', 'Paiwan', 'Puyuma', 'Rukai', 'Truku', 'Amis', 'Sediq', 'Kavalan', 'Thao', 'Ketagalan', 'Saaroa']
         )
        st.success(f"Translated Phrase (English): {phrase.lower()}")

    # User input for contribution
    username = st.text_input("Enter your username:")
    contribution = st.text_area("Contribute something (story, anecdote, etc.):")

    # Submit button
    if st.button("Submit Contribution"):
        if username and contribution:
            # Feature 2: Insert contribution into the database
            insert_contribution(username, contribution)
            st.success("Contribution submitted successfully!")

    # Feature 8: Seasonal Campaign
    st.header("Seasonal Campaign")
    st.write("Share your favorite SEA holiday tradition or memory:")
    seasonal_contribution = st.text_area("Contribute to the seasonal campaign:")

    if st.button("Submit Seasonal Contribution"):
        if username and seasonal_contribution:
            insert_contribution(username, seasonal_contribution)
            st.success("Seasonal contribution submitted successfully!")

    # Feature 2: Display Leaderboard
    st.header("Top Contributors")
    leaderboard = get_leaderboard()
    if leaderboard:
        st.table(pd.DataFrame(leaderboard, columns=['Username', 'Contributions Count']))
    else:
        st.write("No contributions yet.")
    # User-specific contributions and download button
    if username:
        st.header(f"Your Contributions, {username}:")
        user_contributions = get_user_contributions(username)
        st.table(pd.DataFrame(user_contributions, columns=['ID', 'Contribution', 'Timestamp']))

        # Feature 4: Download button
        if st.button("Download My Contributions"):
            download_contributions(username, user_contributions)
            st.success(f"Contributions downloaded as {username}_contributions.csv")

if __name__ == "__main__":
    main()
