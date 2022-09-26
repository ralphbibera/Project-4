import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "Kf4MrxBifKdgiInGG6N7bWMA46ACtFPx"

print("===============================================================================") 
print("                                    MAP QUEST")
print("                                   by: GROUP V")
print("===============================================================================") 
while True:
    #User input for the location & destination and validation of inputs.
    orig = input("\nStarting Location: ")
    if orig == "quit" or orig == "q":
        print("\nProgram Terminated.")
        break
    dest = input("Destination: ")
    print()
    if dest == "quit" or dest == "q":
        print("\nProgram Terminated.\n")
        break
    
    if (orig.isnumeric() or dest.isnumeric())== False:
        #Generation and printing of URL
        url = main_api + \
            urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
        print("URL: " + (url)+ "\n")
        #Json data request
        json_data = requests.get(url).json()
        json_status = json_data["info"]["statuscode"]
        #Successful route call
        if json_status == 0:
            print("API Status: " + str(json_status) + " = A successful route call.\n")
            #Origin information
            print("===============================================================================") 
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")   
            print((orig) + " Information:\n")
            print("Country: " + (json_data["route"]["locations"][0]["adminArea1"]))
            print("Province: " + (json_data["route"]["locations"][0]["adminArea3"]))
            print("Type: " + (json_data["route"]["locations"][0]["geocodeQuality"]))
            print("Geo Quality Code: "+(json_data["route"]["locations"][0]["geocodeQualityCode"]))
            #Destination information
            print("===============================================================================")
            print((dest) + " Information:\n")
            print("Country: " + (json_data["route"]["locations"][1]["adminArea1"]))
            print("Province: " + (json_data["route"]["locations"][1]["adminArea3"]))
            print("Type: " + (json_data["route"]["locations"][1]["geocodeQuality"]))
            print("Geo Quality Code: "+(json_data["route"]["locations"][1]["geocodeQualityCode"]))
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print("===============================================================================")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            #Printing of the directions from the origin to the destination
            print("Directions from " + (orig) + " to " + (dest))
            print()
            #GPS coordinates
            print("GPS Coordinate of Origin: \nLongitude: " +
                str(json_data["route"]["boundingBox"]["ul"]["lng"]) + ", \nLatitude: " + str(json_data["route"]["boundingBox"]["ul"]["lat"]))
            print("\nGPS Coordinate of Destination: \nLongitude: " +
                str(json_data["route"]["boundingBox"]["lr"]["lng"]) + ", \nLatitude: " + str(json_data["route"]["boundingBox"]["lr"]["lat"]))
            #Printing of travel information
            print()
            print("Trip Duration: " + (json_data["route"]["formattedTime"]))
            
            print()
            print("Kilometers: " +
                str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
            
            print()
            print("Fuel Used (Ltr): " +
                str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
            
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print("===============================================================================")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                print((each["narrative"]) + " (" +
                    str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            #Other miscellaneous information about travel
            print("===============================================================================")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print("Other Miscellaneous Information:\n")
            print("Will I encounter any toll road? " , (json_data["route"]["hasTollRoad"]))
            print("Will I encounter any bridge? " , (json_data["route"]["hasBridge"]))
            print("Will I encounter any tunnel? " , (json_data["route"]["hasTunnel"]))
            print("Will I encounter any highway? " , (json_data["route"]["hasHighway"]))
            print("Is there any access restriction? " , (json_data["route"]["hasAccessRestriction"]))
            print("Is there any seasonal closure? " , (json_data["route"]["hasSeasonalClosure"]))
            print("Is there any country cross? " , (json_data["route"]["hasCountryCross"]))
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print("===============================================================================")
        #Unsuccessful route call (error codes)
        elif json_status == 402:
            print("***Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.***")
        elif json_status == 611:
            print("***Status Code: " + str(json_status) + "; Missing an entry for one or both locations.***")
        elif json_status == 602:
            print("***Status Code: " + str(json_status) + "; The route failed, normally due to mustAvoidLinkIds options being set in a way that makes the route impossible.***")
        elif json_status == 500:
            print("***Status Code: " + str(json_status) + "; Unknown error.***")
        else:
            print("***For Staus Code: " + str(json_status) + "; Refer to: https://developer.mapquest.com/documentation/directions-api/status-codes***")
    else:
        print("***Invalid input. Input must be a string.***")
        continue