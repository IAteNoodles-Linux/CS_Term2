# Return names of places more than 7 characters long

def COUNTNOW(PLACES):
    for place in PLACES:
        if len(place) > 7:
            print(place)

if __name__ == '__main__':
    print("Enter a list of places: \t\t\t\tTo exit, press enter...")
    places = []
    while True:
        place = input("Enter a place: ")
        if place == '':
            break
        places.append(place)
    COUNTNOW(places)
