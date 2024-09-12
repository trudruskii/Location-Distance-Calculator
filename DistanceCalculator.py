# SpencerP6.py
# Programmer: Andrew Spencer
# Email: aspencer22@cnm.edu
# Date: 09/12/2024
# Purpose: Ths program allows users to calculate the distance between two geographical points.
# The distance is calculated using the Haversine formula
# Python Version: 3.12.5

# Imports
import math  # Import the math module to access radians, sin and cos functions
import time  # Import the time module to create more user interactivity
import Assignments.Reusable.Goodbye as gb  # Import my Goodbye module to display a goodbye message


# Function Definitions
def display_header():
    print('Welcome to the Geographical Distance Calculator.')
    print('This program will calculate the distance between two geographical points for you.')
    print('To start, enter your first set of coordinates below.\n')


def get_location():
    # Get the first set of coordinates
    latitude = float(input('Enter the latitude of the first point in decimal degrees: '))
    longitude = float(input('Enter the longitude of the first point in decimal degrees: '))
    return latitude, longitude


def distance(first_set_coords, second_set_coords):
    # Unpack the tuples into variables
    lat1, lon1 = first_set_coords
    lat2, lon2 = second_set_coords
    # Convert latitude and longitude to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    # Calculate the distance between the two points using the Haversine formula
    dist = 6371.01 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))
    return dist

def display_results(d):
    print(f'The distance between the two points is: {d} km')



# Main
display_header()

# Start loop to determine if user wants to calculate another distance after each calculation
do_another = 'y'
while do_another.strip()[0] == 'y':
    # Get first set of coordinates by creating variable to store the returned tuple for latitude and longitude
    first_location = get_location()
    # Get the second set of coordinates by creating variable to store the returned tuple for latitude and longitude
    second_location = get_location()
    # Create variable to store the returned distance from the distance function by using indices from the stores tuples
    calculate_distance = distance(first_location, second_location)
    # Display results
    display_results(calculate_distance)
    # Ask user if they want to do another and use lower() to make sure the input is lowercase for case sensitivity
    do_another = input('Do you want to calculate the distance between two more points? (y/n) ').lower()
    if do_another[0] == 'n':
        # use break to end the loop
        break

# Goodbye message
time.sleep(1.5)
print('\nThanks for using the Geographical Distance Calculator.')
gb.Goodbye()