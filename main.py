from connection import Connection
import os
import json

def main(msg):
    days = msg["payload"].get("days", 1)

    project_key = os.getenv("PROJECT_KEY")

    connection = Connection()

    jql = (
        f'project = "{project_key}" '
        f'AND updated >= -{days}d '
        f'ORDER BY updated DESC'
    )

    result = connection.search_issues(
        jql=jql,
        expand="changelog"
    )

    return {"total": result["total"]}

    
if __name__ == "__main__":
    main({})