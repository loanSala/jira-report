from connection import Connection
import os
import json

def main(msg):
    connection = Connection()
    return connection.test_connection()

    
if __name__ == "__main__":
    main({})