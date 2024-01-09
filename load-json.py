import subprocess
import time
from pymongo import MongoClient

def create_text_index(mongodb_port):
    """
    Establishes a connection to a MongoDB server, selects the '291db' database,
    and creates a text index on the 'content' field in the 'tweets' collection.

    Parameters:
    - mongodb_port (int): The port number of the MongoDB server.

    Returns:
    None
    """
    # establishing connection to MongoDB server as save as client
    client = MongoClient('localhost', mongodb_port)
    # selecting the database named 291db
    db = client['291db']
    # get tweets collection
    collection = db.tweets
    # create a text index on the 'content' field
    collection.create_index([("content", "text")], default_language="none")


def main():
    """
    Imports data from a JSON file into a MongoDB database, drops the existing 'tweets'
    collection if it exists, and creates a text index on the 'content' field.

    Parameters:
    None

    Returns:
    None

    """
    json_file = input("Enter the JSON file name: ")
    mongodb_port = int(input("Enter the MongoDB port number: "))

    # record the start time
    start_time = time.time()
    
    result = subprocess.run([
        'mongoimport',
        '--host', 'localhost',
        '--port', str(mongodb_port),
        '--db', '291db',
        '--collection', 'tweets',
        '--drop',  # Drop the collection if it exists
        '--file', json_file,
    ], check=True, stderr=subprocess.PIPE)

    # record the end time
    end_time = time.time()

    create_text_index(mongodb_port)

    # calculate the elapsed time
    elapsed_time = end_time - start_time
    print(f"Data import complete. Elapsed time: {elapsed_time:.2f} seconds\n")

if __name__ == "__main__":
    main()
