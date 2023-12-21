import time
from dronekit import Vehicle


def takeoff(vehicle, altitude):
	if vehicle is None:
		print("Couldn't find the vehicle")
		return
	
	print("Arming motors")
	vehicle.armed = True
	time.sleep(1)
	
	print(f"Taking off to {altitude} meters")
	vehicle.simple_takeoff(altitude)
	while True:
		if vehicle.location.global_relative_frame.alt >= altitude * 0.95:
			print(f"Reached altitude {altitude}")
			break
		time.sleep(1)
