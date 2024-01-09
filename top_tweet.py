import pymongo

def get_top_tweets(db, field, n):
    """Retrieve and return a list of top tweets from the database based on a specified field.

    Parameters:
    - db (pymongo.database.Database): The MongoDB database connection.
    - field (str): The field to use for sorting the tweets. Accepted values are "1" for retweet count,
                  "2" for like count, and "3" for quote count.
    - n (int): The number of top tweets to retrieve.

    Returns:
    list: A list of top tweets, each represented as a dictionary containing tweet details,
          including 'id', 'date', 'content', and 'user.username'.
    """
    # if user enters 1, sort by retweet count
    if field == "1":
        field = "retweetCount"
    # user enters 2, sort by like count
    elif field == "2":
        field = "likeCount"
    # user enters 3, sort by quote count
    elif field == "3":
        field = "quoteCount"
    # return a list of tweets sorted the user input with a limit of n (n entered by user)
    # displays id, date, content, and username
    return list(db.tweets.find({}, {'id': 1, 'date': 1, 'content': 1, 'user.username': 1})
                .sort([(field, pymongo.DESCENDING)])
                .limit(n))

def get_tweet_by_id(db, tweet_id):
    """Retrieve and return details of a specific tweet from the database.

    Parameters:
    - db (pymongo.database.Database): The MongoDB database connection.
    - tweet_id (int): The unique identifier of the tweet to retrieve.

    Returns:
    dict or None: A dictionary containing details of the specified tweet if found, or
                 None if the tweet with the given ID does not exist in the database.
    """
    return db.tweets.find_one({'id': tweet_id})
