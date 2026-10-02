from connection import Connection
import traceback

_connection = None

def handle_message(msg, node_id):

    result = _connection.test_connection()
    return result

    
    
if __name__ == "__main__":
    print("Standalone execution not supported")