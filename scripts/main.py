import sys

from connect_drone import connect_drone
from takeoff import takeoff
from land import land
from fly_to_location import fly_to_location

if __name__ == "__main__":
	# Bağlantı bilgilerini belirtin
	connection_string = sys.argv[1] #main.py 'udp:127.0.0.1:14550'  # Örnek bağlantı adresi
	
	# Drone'a bağlan
	vehicle = connect_drone(connection_string)
	
	# Kalkış
	takeoff(vehicle, 10)  # 10 metre yükseğe kalkış
	
	# Belirli bir konuma gitme
	fly_to_location(vehicle, 47.6097, -122.3331, 20)  # Örnek bir konuma gitme (enlem, boylam, yükseklik)
	
	# İniş
	land(vehicle)
	
	# Bağlantıyı kapat
	if vehicle is not None:
		vehicle.close()
