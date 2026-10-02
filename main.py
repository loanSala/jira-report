from connection import Connection
import traceback

_connection = None

def handle_message(msg, node_id):

    global _connection

    if _connection is None:
        _connection = Connection()

    payload = msg.get("payload", {})

    if payload.get("action") == "get_issue":

        issue_key = payload.get("issue_key")

        return _connection.get_issue(issue_key)

    
    
if __name__ == "__main__":
    print("Standalone execution not supported")