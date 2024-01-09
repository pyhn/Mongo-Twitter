import pymongo
from datetime import datetime, timezone, timedelta
def compose_tweet(db, content, username):
    """
    Composes a new tweet and inserts it into the MongoDB collection.

    Parameters:
    - db (pymongo.database.Database): The MongoDB database containing the 'tweets' collection.
    - content (str): The content of the tweet.
    - username (str): The username of the tweet's author. (set to 291user in main.py)

    Returns:
    None

    Prints a success message if the tweet is successfully inserted into the database.
    Prints an error message if there is an issue with the insertion.

    Note:
    - The function uses a predefined tweet template with various fields.
    - The 'date' field is set to the current time in the Mountain Daylight Time (MDT) timezone.
    - The MDT time is formatted to match the desired format ("%Y-%m-%dT%H:%M:%S-06:00").
    - The tweet is inserted into the 'tweets' collection of the specified MongoDB database.

    """
    collection = db.tweets

    tweet_template = {
        "url": None,
        "date": None,
        "content": None,
        "renderedContent": None,
        "id": None,
        "user": {
            "username": None,
            "displayname": None,
            "id": None,
            "description": None,
            "rawDescription": None,
            "descriptionUrls": None,
            "verified": None,
            "created": None,
            "followersCount": None,
            "friendsCount": None,
            "statusesCount": None,
            "favouritesCount": None,
            "listedCount": None,
            "mediaCount": None,
            "location": None,
            "protected": None,
            "linkUrl": None,
            "linkTcourl": None,
            "profileImageUrl": None,
            "profileBannerUrl": None,
            "url": None
        },
        "outlinks": None,
        "tcooutlinks": None,
        "replyCount": None,
        "retweetCount": None,
        "likeCount": None,
        "quoteCount": None,
        "conversationId": None,
        "lang": None,
        "source": None,
        "sourceUrl": None,
        "sourceLabel": None,
        "media": None,
        "retweetedTweet": None,
        "quotedTweet": None,
        "mentionedUsers": None
    }

    new_tweet = tweet_template.copy()
    new_tweet["content"] = content
   
    # Define the MDT timezone with an offset of -6 hours
    mdt_timezone = timezone(timedelta(hours=-6))

    # Get the current time in MDT
    current_mdt_time = datetime.now(mdt_timezone)

    # Format the MDT time to match the desired format
    formatted_date_string = current_mdt_time.strftime("%Y-%m-%dT%H:%M:%S-06:00")

    # Assuming new_tweet is a dictionary
    new_tweet["date"] = formatted_date_string
    new_tweet["user"]["username"] = username

    try:
        # Insert the tweet into the database
        result = collection.insert_one(new_tweet)

        if result.inserted_id:
            print("Tweet successfully inserted.")
        else:
            print("Failed to insert the tweet.")
    except Exception as e:
        print(f"Error: {e}")

def tweet_input():
    """
    Retrieves user input for composing a tweet.

    Parameters:
    None

    Returns:
    str: The content of the tweet entered by the user.
    """
    text = input("Compose your tweet: ")
    return text

