from databaseHandler import itemDetails
import json
from geopy.distance import geodesic

def getItemsInRadius(radius,lat,long):
    query= itemDetails.select()

    query_result=[]

    for item in query:
        if geodesic((item.latitude,item.longitude),(lat,long)).km <=radius:
            json_result= {}
            json_result['id']= item.id
            json_result['loc']= {0:item.latitude,1:item.longitude}
            json_result['userId']= item.userid
            json_result['description']= item.description
            json_result['price']= item.price
            json_result['status']= item.status

            query_result.append(json_result)

    return json.dumps(query_result)
