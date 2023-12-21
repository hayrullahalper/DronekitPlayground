import time
from dronekit import Vehicle, VehicleMode


def land(vehicle):
	if vehicle is None:
		print("Drone bağlı değil!")
		return
	
	print("Landing")
	vehicle.mode = VehicleMode("LAND")
	time.sleep(5)
	
	print("Disarming motors")
	vehicle.armed = False
