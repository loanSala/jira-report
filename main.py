from connection import Connection
import os
import json

def main(msg):
    print("Received:")
    print(json.dumps(msg, indent=2))

    connection = Connection()

    return {
        "project": os.getenv("PROJECT_KEY"),
        "jira_url_exists": bool(os.getenv("JIRA_URL")),
        "jira_pat_exists": bool(os.getenv("JIRA_PAT"))
    }

    
if __name__ == "__main__":
    main({})