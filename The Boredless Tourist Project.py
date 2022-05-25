# Destination bank that can be expanded on worldwide using a library
destinations = ['Paris, France',
'Shanghai, China',
'Los Angeles, USA',
'Sao Paulo, Brazil',
'Cairo, Egypt']

# Example of User inputted information to match them to an attraction in their destination of choice. Consists of Traveler Name, Destination of choice, and Interests of the traveler
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index


def get_traveler_location(traveler):
  traveler_destination = test_traveler[1]
  traveler_destination_index = destinations.index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

attractions = [[], [], [], [], []]

# This function allows administrators to add new attractions for each destination in the destinations library. Each is added along with their corresponding interests for that particular attraction.
# More attractions and interests for each attraction can be added using a library
def add_attraction(destination, attraction):
  try:
     destination_index = get_destination_index(destination)
  except:
    destinations.append(destination)
    destination_index = get_destination_index(destination)
  attractions[destination_index].append(attraction)

add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Los Angeles, USA", ["Crossroads of the World", ["historical site", "monument"]])
add_attraction('Los Angeles, USA', ['Descanso Gardens', ['garden']])
add_attraction('Los Angeles, USA', ['Los Angeles Zoo', ['zoo']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Paris, France", ["Beach In Dieppe", ["beach"]])
add_attraction("Paris, France", ["Jardin des Plantes", ["garden", "historical site"]])
add_attraction("Paris, France", ["Paris Zoological Park", ["zoo"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["monument", "art"]])
add_attraction("Shanghai, China", ["Jinshan City Beach", ["beach"]])
add_attraction("Shanghai, China", ["Jade Buddha Temple", ["monument", "historical site", "art"]])
add_attraction("Shanghai, China", ["Shanghai Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site", "monument"]])
add_attraction("Sao Paulo, Brazil", ["Bonete Beach, Ilhabela", ["beach"]])
add_attraction("Sao Paulo, Brazil", ["Museu de Arte de São Paulo (MASP)", ["museum", "art"]])
add_attraction("Sao Paulo, Brazil", ["Jardim Botânico de São Paulo", ["garden"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum", "art"]])
add_attraction("Cairo, Egypt", ["International Park", ["garden", "historical site"]])
add_attraction("Cairo, Egypt", ["nearby Ras Abu Galoum, Dahab", ["beach"]])
add_attraction("Cairo, Egypt", ["Cairo Zoo", ["zoo"]])


# This Function matches user's interests to interests of attractions in the destination they plan to visit
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []

  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]

    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ['art'])

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)

  interests_string = "Hi "
  interests_string += traveler[0]
  interests_string += ", we think you'll like these places around "
  interests_string += traveler[1] + ": "
  for i in range(len(traveler_attractions)):
    if traveler_attractions[-1] == traveler_attractions[i]:
      interests_string += traveler_attractions[i] + "."
    elif traveler_attractions[0] == []:
        interests_string += "Sadly, no attractions found."
    else:
      interests_string += traveler_attractions[i] + ", "
  return interests_string


# Example of finally testing function: When given an array with traveler's name, destination they'd like to visit, and their interests, the function will return a statement with recommendations for attractions to visit that match their interests in their destination of choice!
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])

# print(smills_france)         <------ This example prints out the Arc De Triomphe as an attraction for Dereck Smill to visit on his Paris trip given that he's interested in monuments!

Name = input("Type Traveler Name here: ")
Destination = input("""Input destination of choice here
ONLY ACCEPTS:
'Paris, France',
'Shanghai, China',
'Los Angeles, USA',
'Sao Paulo, Brazil',
'Cairo, Egypt')
CASE SENSITIVE: """ )
Interests = input("Type Interests here (only accepts: beach, art, museum, historical site, monument, garden, and zoo) CASE SENSITIVE: ")

test = get_attractions_for_traveler([Name, Destination, [Interests]])
print(test)
