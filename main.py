import json
from top_tweet import get_top_tweets, get_tweet_by_id
from top_user import get_top_users, get_user_by_id
from search_tweet import get_keywords, search_tweets
from compose_tweet import tweet_input, compose_tweet
from search_users import get_search_users, get_moreInfo
from pymongo import MongoClient


def main():
    """
    Main function to interact with the MongoDB database and perform various actions based on user input.
    """
    client = None  # initialize client to None outside the try block

    try:
        mongodb_port = int(input("Enter the MongoDB port number: "))
        client = MongoClient('localhost', mongodb_port)
        db = client['291db']

        start_screen = """
    ██╗░░░██╗███╗░░██╗██╗░░░░░███████╗░█████╗░░██████╗██╗░░██╗██╗███╗░░██╗░██████╗░  ████████╗██╗░░██╗███████╗
    ██║░░░██║████╗░██║██║░░░░░██╔════╝██╔══██╗██╔════╝██║░░██║██║████╗░██║██╔════╝░  ╚══██╔══╝██║░░██║██╔════╝
    ██║░░░██║██╔██╗██║██║░░░░░█████╗░░███████║╚█████╗░███████║██║██╔██╗██║██║░░██╗░  ░░░██║░░░███████║█████╗░░
    ██║░░░██║██║╚████║██║░░░░░██╔══╝░░██╔══██║░╚═══██╗██╔══██║██║██║╚████║██║░░╚██╗  ░░░██║░░░██╔══██║██╔══╝░░
    ╚██████╔╝██║░╚███║███████╗███████╗██║░░██║██████╔╝██║░░██║██║██║░╚███║╚██████╔╝  ░░░██║░░░██║░░██║███████╗
    ░╚═════╝░╚═╝░░╚══╝╚══════╝╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

                        ██████╗░░█████╗░░██╗░░░░░░░██╗███████╗██████╗░  ░█████╗░███████╗
                        ██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝██╔══██╗  ██╔══██╗██╔════╝
                        ██████╔╝██║░░██║░╚██╗████╗██╔╝█████╗░░██████╔╝  ██║░░██║█████╗░░
                        ██╔═══╝░██║░░██║░░████╔═████║░██╔══╝░░██╔══██╗  ██║░░██║██╔══╝░░
                        ██║░░░░░╚█████╔╝░░╚██╔╝░╚██╔╝░███████╗██║░░██║  ╚█████╔╝██║░░░░░
                        ╚═╝░░░░░░╚════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚═╝  ░╚════╝░╚═╝░░░░░

                        ███╗░░░███╗░█████╗░███╗░░██╗░██████╗░░█████╗░██████╗░██████╗░
                        ████╗░████║██╔══██╗████╗░██║██╔════╝░██╔══██╗██╔══██╗██╔══██╗
                        ██╔████╔██║██║░░██║██╔██╗██║██║░░██╗░██║░░██║██║░░██║██████╦╝
                        ██║╚██╔╝██║██║░░██║██║╚████║██║░░╚██╗██║░░██║██║░░██║██╔══██╗
                        ██║░╚═╝░██║╚█████╔╝██║░╚███║╚██████╔╝╚█████╔╝██████╔╝██████╦╝
                        ╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝░╚═════╝░░╚════╝░╚═════╝░╚═════╝░\n"""

        print(start_screen)
        program_end = False
        while not program_end:
            print("1. Search for tweet")
            print("2. Search for user")
            print("3. List top tweets")
            print("4. List top users")
            print("5. Compose a tweet")
            print("6. Exit")
            user_choice = input("Please enter a number selection: ")
            choosing = False
            while not choosing:
                if user_choice == "1":
                    keywords = get_keywords()
                    search_tweets(db, keywords)
                    break

                elif user_choice == "2":
                    while True:
                            #User input for the keyword
                            keyword = input("Enter a Keyword to search for users (or type '-1' to return): ")
                            
                            if keyword.lower() == '-1': #Exiting if user picks -1
                                print("Exiting user search.")
                                choosing = True
                                break

                            user_summaries = get_search_users(db, keyword)
                            if not user_summaries: #If no user_summaries are found then print error message.
                                print("No users found. Try again.")
                                continue

                            print("\nFound users:")
                            for index, user in enumerate(user_summaries, start=1): 
                                username = user.get('username', 'Unknown')
                                displayname = user.get('displayname', 'Unknown')
                                location = user.get('location', 'Unknown')
                                print(f"{index}. Username: {username}, Display Name: {displayname}, Location: {location}") #Printing each users by index and incrementaion of 1.

                            user_selection = input("\nEnter a number to view full information, or type 'exit' to return: ") #Choose a index to view full information.

                            if user_selection.lower() == 'exit':
                                print("Exiting user details view.")
                                break
                            elif user_selection.isdigit() and 0 < int(user_selection) <= len(user_summaries):
                                selected_username = user_summaries[int(user_selection) - 1].get('username')
                                if selected_username: #Once we select a user it will print out all known information about this user.
                                    full_user_info = get_moreInfo(db, selected_username)
                                    if full_user_info:
                                        print("\nFull information about the user:")
                                        for key, value in full_user_info.items():
                                            print(f"{key}: {value}")
                                    else:
                                        print("Detailed user information not found.")
                                else:
                                    print("Invalid username selection.")
                            else:
                                print("Invalid input. Please enter a valid number or type 'exit' to return.")
                elif user_choice == "3":
                    # while True:
                    while True:
                        print("0. Go back")
                        print("1. Retweet Count")
                        print("2. Like Count")
                        print("3. Quote Count")
                        field = input("Please input a number option: ")
                        # if the input is valid we can continue
                        if (field == "0" or field == "1" or field == "2" or field == "3"):
                            # if the input was 0 we go back and break out of the loop
                            if (field == "0"):
                                choosing = True
                                break
                            # otherwise ask user for how many tweets they want to display
                            n = int(input("Enter the number of top tweets to display: "))
                            top_tweets = get_top_tweets(db, str(field), n)
                            count = 1
                            # iterating through the top tweets and displaying the matching ones
                            for tweet in top_tweets:
                                username = tweet['user']['username'] if 'user' in tweet and 'username' in tweet['user'] else 'Unknown'
                                print(f"{count}. ID: {tweet['_id']}, Date: {tweet['date']}, Content: {tweet['content']}, Username: {username}")
                                count += 1
                            while True:   
                                # ask the user to input a tweet to see more details 
                                tweet_selection = int(input("Enter the number of the tweet to view all fields or 0 to go back: "))
                                # if valid input, display all details
                                if tweet_selection > 0 and tweet_selection < count:
                                    selected_tweet_id = top_tweets[tweet_selection-1]['id']
                                    selected_tweet_data = get_tweet_by_id(db, selected_tweet_id)
                                    print(selected_tweet_data)
                                    # choosing = True
                                    break
                                # else 0 to go back
                                elif tweet_selection == 0:
                                    # choosing = True
                                    break
                                else:
                                    print("Invalid input, try again!!!!!")
                                    continue
                        else:
                            print("Invalid input, try again.")
                            continue

                elif user_choice == "4":
                    while True:
                        # n is the number of users to display
                        n = int(input("Enter the number of top users to display or 0 to go back: "))
                        if n >= 0:
                            # user entered 0 meaning they want to go back to main menu
                            if n == 0:
                                choosing = True
                                break
                            # otherwise get the top users list with limit of n   
                            top_users = get_top_users(db, n)
                            count = 1
                            # iterating throug the users and printing them
                            for user in top_users:
                                print(f"{count}. Username: {user['username']}, Display Name: {user['displayname']}, Followers Count: {user['followersCount']}")
                                count += 1

                            while True:
                                # asking the user to see more details of a displayed user
                                user_id = int(input("Enter the number of the user to view full details or 0 to go back: "))
                                # 0 means to go back to the other menu
                                if user_id == 0:
                                    choosing = True
                                    break

                                # if the id they chose is greater than 0 and less than the size of the list, it is a valid input  
                                if user_id > 0 and user_id < count:
                                    # getting the user id from the list
                                    selected_user_id = top_users[user_id-1]['_id']
                                    # getting the data of the specified id
                                    selected_user_data = get_user_by_id(db, selected_user_id)
                                    print(selected_user_data)  # Displaying the user details
                                    choosing = True
                                    break
                                else:
                                    print("User not found.")
                        else:
                            print("Invalid input, please try again.")

                elif user_choice == '5':
                    tweet_content = tweet_input()
                    username = "291user"
                    compose_tweet(db, tweet_content, username)
                    break
                elif user_choice == '6':
                    program_end = True
                    print("System Exiting...")
                    break

                else:
                    print("Invalid input, try again.\n")
                    break
    finally:
        # Close the MongoDB connection if it was established
        if client is not None:
            client.close()

if __name__ == "__main__":
    main()
