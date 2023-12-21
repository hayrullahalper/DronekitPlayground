from dronekit import connect, Vehicle

def connect_drone(connection_string):
    try:
        return connect(connection_string, wait_ready=True)
    except Exception as e:
        print(f"Bağlantı hatası: {e}")
        return None
