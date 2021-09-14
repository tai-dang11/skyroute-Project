from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Build your program below:
landmark_string = ""
for letter, landmark in landmark_choices.items():
	landmark_string += "{0} - {1}\n".format(letter, landmark)
		
	
def greet():
	print("Hi there and welcome to SkyRoute!")
	print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)
	

#handle setting the selected origin and destination points.
def set_start_and_end(start_point, end_point):
	if start_point != None:
		change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
		if change_point == "b":
			start_point = get_start()
			end_point = get_end()
		elif change_point == "o":
			start_point = get_start()
		elif change_point == "d":
			end_point == get_end()
		else:
			print("ops, that isn't 'o', 'd', or 'b'...")
			set_start_and_end(start_point, end_point)
	else:
		start_point = get_start()
		end_point = get_end()
	return start_point, end_point

#used to request an origin from the user.	
def get_start():
	start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
	if start_point_letter in [k for k in landmark_choices.keys()]:
		start_point = landmark_choices[start_point_letter]
		return start_point
	else:
		print("Sorry, that's not a landmark we have data on. Let's try this again...")
		get_start()


#request an end from the user
def get_end():
	end_point_letter = input("Where are you headed? Type in the corresponding letter: ")
	if end_point_letter in [k for k in landmark_choices.keys()]:
		end_point = landmark_choices[end_point_letter]
		return end_point
	else:
		print("Sorry, that's not a landmark we have data on. Let's try this again...")
		get_end()

def get_route(start_point, end_point):
	routes = []
	start_stations = vc_landmarks[start_point]
	end_stations = vc_landmarks[end_point]
	for start_station in start_stations:
		for end_station in end_stations:
			if stations_under_construction != None:
				metro_system = get_active_stations()
			else:
				metro_system = vc_metro
			route = bfs(metro_system, start_station, end_station)
			if stations_under_construction != None:
				possible_route = dfs(metro_system, start_station, end_station)
				if possible_route == None:	
					return None
			if route != None:
				routes.append(route)
	shortest_route = min(routes, key = len)
	return shortest_route
	
def show_landmarks():
	see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
	if see_landmarks == "y":
		print(landmark_string)
		
		
def goodbye():
	print("Thanks for using SkyRoute!")	


#get and set the origin and destination
#call search to get the recommended route
#allow users to search for another route
def new_route(start_point = None, end_point = None):
	start_point, end_point = set_start_and_end(start_point, end_point)
	shortest_route = get_route(start_point, end_point)
	if shortest_route != None:
		shortest_route_string = '\n'.join(shortest_route)
		print("the shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
	else:
		print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point, end_point))
	again = input("Would you like to see another route? Enter y/n: ")
	if again == "y":
		show_landmarks()
		new_route(start_point, end_point)

stations_under_construction = []
#not constructed station
def get_active_stations():
	updated_metro = vc_metro
	for station_under_construction in stations_under_construction:
		for current_station, neighboring_stations in vc_metro.items():
			# if current not construct station, remove construct connecting stations
			if current_station != station_under_construction:
				updated_metro[current_station] -= set(stations_under_construction)
			else:
				updated_metro[current_station] = set([])
	return updated_metro


	
def skyroute():
	greet()
	new_route()
	goodbye()

skyroute()
