# Craingslist Sales Details

This repo contains information related to sales details of Craiglist and some apis
to retrieve some data.

1.
 to get the list of all the items sorted by price (asec or desc)
 http://127.0.0.1:10001/getsorteddata?reverse=True&criteria=price
 
2.
 to get a single item (by id or location)
 http://127.0.0.1:10001/getitem?id=542204653f37951d5c000036
 http://127.0.0.1:10001/getitem?location=[37.37657636848912,-121.92350465218554]

3.
 to get list of items (by status or userid) 
 http://127.0.0.1:10001/getitemlist?status=removed
 http://127.0.0.1:10001/getitemlist?userid=53f6c9c96d1944af0b00000b

4.
 to get list of items in a radius 
 http://127.0.0.1:10001/get_items_in_radius?radius=1&latitude=36.16622315108078&longitude=-115.14207467773902


## Result of the above api's is returned in JSON format
