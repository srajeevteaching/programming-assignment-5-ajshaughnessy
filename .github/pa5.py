# Programmers: Aidan
# Course: CS151, Dr. Rajeev
# Programming Assignment: 5
# Program Inputs: [What information do you request from the user?]
# Program Outputs: [What information do you display for the user?]

# Problem The files 2016_09.csv and 2016_10.csv contain data for taxi trips in the city of Chicago for the months of
# September and October of 2016 (respectively) in comma-separated values format. Each line contains the values in the
# following order:

# Taxi's id number Date and time of the start of the trip in month/day/year hour:minute format Date and time of the end
# of the trip in month/day/year hour:minute format Duration of trip in seconds Distance of the trip in miles Cost of
# the trip Payment type ("Cash" or "Credit Card") Taxi company Pickup location latitude (-90 to 90) Pickup location
# longitude (-180 to 180) Dropoff location latitude (-90 to 90) Dropoff location longitude (-180 to 180) Write a
# program which, given the name of a file in the above format, loads the file into a list of lists and is able to
# perform the following tasks:

# Output the average cost for cash and (separately) credit card payments. Output the count of all trips that started or
# ended on a user-given date. Output to a file (name provided by the user) the information for all trips with a pickup
# or dropoff location that is within a given distance of a given location. Each outputted line should be in the same
# format as the input file. The distance is inputted by the user in miles. The location is inputted by the user as a
# latitude and longitude. The distance between two locations (lat1, lon1) and (lat2, lon2) can be calculated using the
# formula distance = arccos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2)) * 3,959 miles.

# Input Validation: Your program must work for any file with the above format without any modification. If an
# unavailable file is given as input, your program should print an error message and end normally. Your program must
# work for any file of specified format without modification to your code (not just the two files provided). Your
# program should also ensure user-inputted latitude and longitude (floats) are in their respective valid intervals.
# Lastly, you should ensure user-inputted distance (float) is a positive value.

# Function decomposition Your program should have at least the following functions. You may have additional helper
# functions.

# A function that, given a filename, loads the data and returns it as a list of lists.

# For each of the three tasks in the instructions section, a function that does the calculation, taking inputs as
# parameters and returns the corresponding value (if applicable). These three functions should not use input/output.

# For each of the three tasks in the instructions section, a function that gathers and validates all necessary inputs
# from the user, calls the corresponding functions (from Item 2) and presents the results to the user. These three
# functions should use input/output operations.

# A function that, given four floating point parameters (corresponding to the latitude and longitude of two locations)
# uses the formula given in Item 3 of the problem statement to return the distance between the given points. Use the
# math.radians function to convert the lat/lon degrees to radians before calling the math module's trigonometric
# functions. Test your function with the coordinates of Baltimore (+39.2904, -76.6122) and Washington DC
# (+38.9072, -77.0369). The result should be 34.92485 miles.

# A main function to drive the program. Allow the user to choose one of the three operations described in the
# instructions. After completing the chosen option, the program should loop, allowing the user to choose another
# operation or to end the program.

import math

data_list = []

def read_file(name):
    try:
        with open(name, "r") as f:
            for line in f:
                li_list = line.split(",")
                data_list.append(li_list)
    except:
        print("Invalid, try again.")
        exit

def cash_average():
    count = 0.0
    suM = 0.0
    for i in data_list:
        if i[6] == "Cash":
            suM += float(i[5])
            count += 1
    avg = suM / count
    return avg

def card_average():
    count = 0.0
    suM = 0.0
    for i in data_list:
        if i[6] == "Credit Card":
            suM += float(i[5])
            count += 1
    avg = suM / count
    return avg

def find_date(date):
    count = 0
    for i in data_list:
        if i[1].startswith(date) or i[2].startswith(date):
            count += 1
    return count

def distance(lat1, lon1, lat2, lon2):
    return math.acos(
        math.sin(float(lat1)) * math.sin(float(lat2)) + math.cos(float(lat1)) * math.cos(float(lat2)) * math.cos(
            float(lon1) - float(lon2))) * 3959

def find_near(fname, distance, lat, lon):
    file_li = []
    for i in data_list:
        dis1 = distance(i[8], i[9], lat, lon)
        dis2 = distance(i[8], i[9], lat, lon)
        if distance >= dis1 or distance >= dis2:
            file_li.append(",".join(i))
    try:
        file_line = "\n".join(file_li)
        with open(fname, "w") as fi:
            fi.write(file_line)
    except:
        print("Error")

if __name__ == "__main__":
    read_file(input("Enter the file name: "))
    while True:
        print("1 for avg. cash payments")
        print("2 for avg. card payments")
        print("3 for total number of travels in a certain date")
        print("4 for list the travels near a point ")
        print("anything else to exit")
        f = input("enter an option")
        if f == "1":
            print("Average cash payments of the months is : $", cash_average())
        elif f == "2":
            print("Average card payments of the months is : $", card_average())
        elif f == "3":
            date = input("enter a date in proper format: ")
            print("Total travels on the date is: ", find_date(date))
        elif f == "4":
            lat = float(input("Latitude: "))
            if lat > 90 or lat < -90:
                print("Invalid latitude")
                continue
            lon = float(input("Longitude: "))
            if lon > 180 or lon < -180:
                print("Invalid longitude")
                continue
            try:
                distance = int(input("Distance: "))
            except:
                print("Distance is integer")
                continue
            if distance < 0:
                print("Invalid distance")
                continue
            fname = input("Enter the file name to be created: ")
            find_near(fname, distance, lat, lon)
        else:
            print("Ending program")
            break
