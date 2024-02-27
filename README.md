# SEA Data Collection App

## Summary of Features Implemented:

### 1. Interactive Challenge
Users can engage in a language challenge by entering a phrase in their native language. The app provides a dropdown for users to select the corresponding Southeast Asian language. The entered phrase is then translated into English, fostering an interactive and educational element.

### 2. Community Leaderboards
A dynamic leaderboard showcases the top contributors based on the number of contributions made. This feature encourages healthy competition and recognizes the most active participants within the community.

### 4. Storytelling Platform
Users are encouraged to contribute short stories, anecdotes, or cultural narratives. This creates a platform for users to share and celebrate the richness of their cultures, fostering a sense of community and diversity.

### 8. Seasonal Campaign
A dedicated section prompts users to share their favorite Southeast Asian holiday traditions or memories. This feature adds a seasonal and thematic element to the app, creating engagement around specific cultural topics.

### Database and Data Download
User contributions are stored in a SQLite database ('user_data.db'). Users can download their contributions in CSV format for personal records or further analysis.

## Technologies Used:

- **Streamlit:** The main framework for building the web application, providing a simple and efficient way to create interactive interfaces with Python.
- **SQLite:** A lightweight and embedded database used to store user contributions.
- **Pandas:** A data manipulation library in Python used to handle and process data, particularly for creating DataFrames for leaderboard display and CSV creation.

## User Interaction Guide:

1. **Language Challenge:**
   - Enter a phrase in your native language.
   - Select the corresponding Southeast Asian language from the dropdown.
   - View the translated phrase in English.

2. **Submit Contribution:**
   - Enter your username and contribute a story or anecdote.
   - Click the "Submit Contribution" button.

3. **Seasonal Campaign:**
   - Share your favorite Southeast Asian holiday tradition or memory.
   - Click the "Submit Seasonal Contribution" button.

4. **View Leaderboard:**
   - Explore the "Top Contributors" section to see the most active participants.

5. **Download Contributions:**
   - Enter your username.
   - Click the "Download My Contributions" button to download your contributions in CSV format.
