from connection import Connection
import traceback

_connection = None

def handle_message(msg, node_id):

    global _connection

    try:

        if _connection is None:
            _connection = Connection()

        payload = msg.get("payload", {})

        if payload.get("action") == "get_issue":

            issue_key = payload.get("issue_key")

            issue = _connection.get_issue(issue_key)

            return {
                "key": issue["key"],
                "summary": issue["fields"]["summary"],
                "status": issue["fields"]["status"]["name"],
                "assignee": (
                    issue["fields"]["assignee"]["displayName"]
                    if issue["fields"]["assignee"]
                    else "Unassigned"
                ),
                "priority": (
                    issue["fields"]["priority"]["name"]
                    if issue["fields"].get("priority")
                    else "N/A"
                )
            }

        return {
            "error": "Unknown action"
        }

    except Exception as e:

        return {
            "error": str(e),
            "traceback": traceback.format_exc()
        }
    
    
if __name__ == "__main__":
    print("Standalone execution not supported")