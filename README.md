# Mongo-Twitter

## Description

This Python script provides a simple command-line interface for interacting with a MongoDB database to perform various actions related to Twitter data. It leverages multiple modules (`top_tweet.py`, `top_user.py`, `search_tweet.py`, `compose_tweet.py`, `search_users.py`) to carry out operations such as searching for tweets, searching for users, listing top tweets, listing top users, and composing tweets. The interactions are text-based and guided by the console menu. This script has been tested on collections with more than 400 000 documents. (Original JSON too large to add to repository).

## Prerequisites

1. **MongoDB Server:** Ensure that you have MongoDB installed and running on your machine.

2. **Python Modules:** Install the required Python modules by running the following command:
   ```bash
   pip install pymongo
   ```

## Usage

1. **Run the Script:**
   ```bash
   python main.py
   ```
   Follow the on-screen prompts to interact with the system.

2. **Enter MongoDB Port:**
   - Input the MongoDB port number when prompted.

3. **Main Menu:**
   - The main menu displays several options for interacting with the Twitter data stored in MongoDB.

4. **Options:**
   - **Search for tweet (Option 1):** Enter keywords to search for tweets containing the specified keywords.

   - **Search for user (Option 2):** Enter a keyword to search for users. View summarized information and select a user to see detailed information.

   - **List top tweets (Option 3):** Choose from options to list top tweets based on retweet count, like count, or quote count. View tweet details.

   - **List top users (Option 4):** Enter the number of top users to display. View summarized information and select a user to see detailed information.

   - **Compose a tweet (Option 5):** Enter the content for a new tweet, and it will be stored in the database.

   - **Exit (Option 6):** Exit the program.

## Modules

- **`top_tweet.py`:** Provides functions to retrieve top tweets from the database based on various criteria.

- **`top_user.py`:** Provides functions to retrieve top users from the database.

- **`search_tweet.py`:** Provides functions to search for tweets based on keywords.

- **`compose_tweet.py`:** Provides functions to input and compose a new tweet, storing it in the database.

- **`search_users.py`:** Provides functions to search for users based on a keyword and view summarized and detailed information.

## Database Structure

- The script interacts with a MongoDB database named `291db`.

- Collections:
  - `tweets`: Stores tweet data.
  - `users`: Stores user data.
## Authors
- Reimark Ronabio, Andrew Chan, Kevin Yu
