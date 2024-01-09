import time 

def search_tweets(db, keywords):
    batch_size = 25
    start_time = time.time()
    collection = db.tweets

    if len(keywords) < 1:
        print("No Input, Returning to Menu.\n")
        return
    else:
        text_search_string = ' '.join(f'"{keyword}"' for keyword in keywords)
        search_query = {"$text": {"$search": text_search_string}}
    # retrieve all tweets that match the search query
    result = collection.find(search_query, {"_id": 1, "date": 1, "content": 1, "user.username": 1})

    # display the matching tweets with IDs
    matching_tweets = list(result)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Search complete. Elapsed time: {elapsed_time:.2f} seconds\n")

    if len(matching_tweets) == 0:
        print("No Results, Returning to Menu.\n")
        return

    # calculate the total number of batches
    total_batches = (len(matching_tweets) + batch_size - 1) // batch_size

    page = 1

    while True:
        # calculate the start and end indices for the current batch
        start_index = (page - 1) * batch_size
        end_index = min(start_index + batch_size, len(matching_tweets))

        for i in range(start_index, end_index):
            tweet_number = i + 1
            tweet = matching_tweets[i]
            print(f"[Tweet No. {tweet_number}]:\nID: {tweet['_id']}, Date: {tweet['date']}, Content: {tweet['content']}, Username: {tweet['user']['username']}\n")

        print(f"Page {page}/{total_batches}")

        # ask the user if they want to see the next batch
        user_input = input("Do you want to see the next page? (y/n): ").lower()

        if user_input != 'y' or page == total_batches:
            break  # exit the while loop if the user doesn't want to see the next batch or if it's the last batch
        else:
            page += 1  # move to the next page for the next batch

    # ensure the user enters a valid integer within the bounds of the displayed tweet results
    while True:
        try:
            selected_index = int(input("Enter the number of the tweet you want to view (or enter 0 to go back): ")) - 1

            if selected_index == -1:
                print("Returning to Menu.")
                return
            elif 0 <= selected_index < len(matching_tweets):
                # retrieve and display the selected tweet with all fields
                selected_tweet = collection.find_one({"_id": matching_tweets[selected_index]['_id']})
                print("\n=============[Start of selected tweet]=============\n")
                for key, value in selected_tweet.items():
                    print(f"{key}: {value}")
                print("\n==============[End of selected tweet]==============\n")
                break
            else:
                print("Invalid selection. Please enter a number within the bounds.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_keywords():
    text_input = input("Enter keywords separated by spaces to filter tweets [or enter to exit]: ").strip().lower()
    keywords = list(text_input.split())
    print(keywords)
    return keywords