from connection import Connection
import traceback

_connection = None

def handle_message(msg, node_id):

    global _connection

    try:

        if _connection is None:
            _connection = Connection()

        payload = msg.get("payload", {})

        days = payload.get("days", 1)

        return {
            "status": "received",
            "days": days
        }

    except Exception as e:

        return {
            "error": str(e),
            "traceback": traceback.format_exc()
        }

    
if __name__ == "__main__":
    print("Standalone execution not supported")