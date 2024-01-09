def get_top_users(db, n):
    """Retrieve and return a list of top users based on follower count.

    Parameters:
    - db (pymongo.database.Database): The MongoDB database connection.
    - n (int): The number of top users to retrieve.

    Returns:
    list: A list of top users, each represented as a dictionary containing user details,
          including 'username', 'displayname', and 'followersCount'.
    """
    return list(db.tweets.aggregate([
        {"$group": {
            "_id": "$user.username",
            "username": {"$first": "$user.username"},
            "displayname": {"$first": "$user.displayname"},
            "followersCount": {"$max": "$user.followersCount"}
        }},
        {"$sort": {"followersCount": -1}},
        {"$limit": n}
    ]))

def get_user_by_id(db, username):
    """Retrieve and return details of a specific user from the database.

    Parameters:
    - db (pymongo.database.Database): The MongoDB database connection.
    - username (str): The username of the user to retrieve.

    Returns:
    dict or None: A dictionary containing details of the specified user if found, or
                 None if the user with the given username does not exist in the database.
    """
    return db.tweets.find_one({'user.username': username}, {'user': 1})
