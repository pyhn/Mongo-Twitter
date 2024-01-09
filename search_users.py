import pymongo
import re
import time

def get_search_users(db, keyword, full_info_username=None):
    """
    Retrieves user information based on a keyword search in their display names or locations.
    
    Args:
        db (pymongo.database.Database): The MongoDB database instance.
        keyword (str): The keyword used for the search within display names or locations.
        full_info_username (str, optional): If specified, narrows the search to this particular user.

    Returns:
        list[dict] or dict: A list of unique user information if full_info_username is not specified,
        or detailed user information for the specified user.
    """
    # Search for users based on keyword in displayname or location
    start_time = time.time()
    query = {
        "$or": [
            {"user.displayname": {"$regex": keyword, "$options": "i"}},
            {"user.location": {"$regex": keyword, "$options": "i"}}
        ]
    }

    # If full_info_username is specified, refine the search to that user
    if full_info_username:
        query["user.username"] = full_info_username

    users = db.tweets.find(query, {"user.username": 1, "user.displayname": 1, "user.location": 1})

    # If full information of a specific user is needed
    if full_info_username:
        for user in users:
            return user.get('user')  # Returns the full user information

    # Otherwise, compile a list of unique users
    unique_users = {}
    for user in users:
        user_info = user.get('user')
        if user_info:
            username = user_info.get('username')
            if username:  # Ensure username is not None
                displayname = user_info.get('displayname')
                location = user_info.get('location')
                unique_users[username] = {'username': username, 'displayname': displayname, 'location': location}
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Search complete. Elapsed time: {elapsed_time:.2f} seconds\n")
    return list(unique_users.values())

def get_moreInfo(db, full_info_username):
    """
    Retrieves detailed information about a specific user.
    
    Args:
        db (pymongo.database.Database): The MongoDB database instance.
        full_info_username (str): The username for which detailed information is requested.

    Returns:
        dict or None: Detailed user information if found, otherwise None.
    """
    # Find a tweet that the user has posted and get their information
    user_data = db.tweets.find_one({"user.username": full_info_username}, {"user": 1})

    # Extract the 'user' field from the found document
    if user_data and 'user' in user_data:
        return user_data['user']
    else:
        return None
