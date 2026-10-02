import os
from connection import Connection
from dotenv import load_dotenv
import json

def main(msg):
    load_dotenv()
    project_key = os.getenv("PROJECT_KEY")
    print("Received:")
    print(json.dumps(msg, indent=2))

    connection = Connection()

    return {
        "success": True,
        "received": msg
    }
        

    

if __name__ == "__main__":
    main({})