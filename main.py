import argparse
import os
from connection import Connection
from dotenv import load_dotenv
import json

def main():
    load_dotenv()
    project_key = os.getenv("PROJECT_KEY")
    parser = argparse.ArgumentParser(description="Generate Jira report")
    parser.add_argument("--days", type=int, default=1, help="Number of days to look back")
    parser.add_argument("--all", action="store_true", help="Fetch all issues in the configured project without an updated-date filter")
    args = parser.parse_args()

    connection = Connection()
    if args.all:
        jql_query = f'project = "{project_key}" ORDER BY status ASC, key ASC'
    else:
        jql_query = f'project = "{project_key}" AND updated >= -{args.days}d ORDER BY updated DESC'
    if args.all:
        result = connection.search_issues(jql_query, expand="changelog")
        while len(result["issues"]) < result["total"]:
            page = connection.search_issues(
                jql_query,
                expand="changelog",
                start_at=len(result["issues"]),
            )
            result["issues"].extend(page["issues"])
    else:
        result = connection.search_issues(jql_query, expand="changelog")

    print(json.dumps(result, indent=2))

    return result

if __name__ == "__main__":
    main()