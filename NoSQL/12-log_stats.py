#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in MongoDB """


from pymongo import MongoClient


def loggedStats():
    """ Provides some stats about Nginx logs stored in MongoDB """
# Connect to the MongoDB server
client = MongoClient()

# Access the logs database and nginx collection
db = client['logs']
collection = db['nginx']

# Get the total number of logs
total_logs = collection.count_documents({})

# Print the number of logs
print(f"Total logs: {total_logs} logs")

# Get the count of logs for each HTTP method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in methods}

# Print the count of logs for each HTTP method
print("Methods:")
for method in methods:
    print(f"\t{method}: {method_counts[method]} logs")

# Get the count of logs with method=GET and path=/status
status_logs = collection.count_documents({"method": "GET", "path": "/status"})

# Print the count of logs with method=GET and path=/status
print(f"method=GET, path=/status: {status_logs} logs")
