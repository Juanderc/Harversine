from flask import Flask, request, Blueprint, jsonify
import math #module of math
import re #module to get matches
import logging #module to save the historial
api_bp = Blueprint("api_bp",__name__) 

#Function to create, format and write the historial
def Writer(args):
    logging.basicConfig(filename="distances.log",filemode='w', format=('%(asctime)s - %(message)s'))
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info(args)


#harversine method
#https://en.wikipedia.org/wiki/Haversine_formula

#This is a decorator to validate the input data
def validate(f):
    def wrapper():
        args = request.args.get("coordenates") #Receive the argument by url
        coordenate = args.split(", ") #split a list with ',' by separator to take the latitude and longitude
        if len(coordenate[0]) < 9: #Evaluate the length of the latitude and return error if less than 9
            return jsonify({"Error":"Invalid latitude"}),400
        else: #else return the haversine function passing the main coordinate and the user coordinate
            return f(55.69103,37.41301, float(coordenate[0]), float(coordenate[1]))
    return wrapper

@api_bp.route("/distance",methods=['GET'])
@validate
def harversine(lat1,long1,lat2,long2):
    #map use a function in every element of a list, and convert it in radians, because
    #the method of harversine say it.
    lat1,long1,lat2,long2 = map(math.radians, [lat1,long1,lat2,long2]) 
    slat = lat2 - lat1 # latitude subtraction
    slong = long2 - long1 # longitude subtraction
    R = 6372 # earth radius

    #---------Harversine--Method------
    D = (math.sin(slat/2))**2 + (math.cos(lat1)) * (math.cos(lat2)) * (math.sin(slong/2))**2
    distance = 2 * R * math.asin(math.sqrt(D))
    #---------------------------------

    #-----------Return-in-meters------
    if re.findall("^0",str(distance)): #it find an occurrency of 0 from the start
        Writer("{} m" .format(distance * 1000))
        return jsonify({"Distance": "{} m" .format(distance * 1000)}) #It use jsonify to format the data
    #----------Return-in-kilometres---
    else:
       Writer("{} km" .format(distance))
       return jsonify({"Distance": "{} km" .format(distance)})



