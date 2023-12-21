from dronekit import LocationGlobalRelative, Vehicle


def fly_to_location(vehicle, latitude, longitude, altitude):
	if vehicle is None:
		print("Couldn't find the vehicle")
		return
	
	target_location = LocationGlobalRelative(latitude, longitude, altitude)
	vehicle.simple_goto(target_location)
	while True:
		if vehicle.location.global_relative_frame.lat == latitude and vehicle.location.global_relative_frame.lon == longitude:
			print("Arrived to destination")
			break
