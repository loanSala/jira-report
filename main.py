from connection import Connection
import traceback

_connection = None

def handle_message(msg, node_id):

    global _connection

    try:

        if _connection is None:
            _connection = Connection()

        result = _connection.test_connection()

        return result

    except Exception as e:

        return {
            "error": str(e),
            "traceback": traceback.format_exc()
        }

    
if __name__ == "__main__":
    print("Standalone execution not supported")