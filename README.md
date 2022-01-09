# Craingslist Sales Details

This repo contains information related to sales details of Craiglist and some apis
to retrieve some data.

1.
 to get the list of all the items sorted by price (asec or desc)
 http://127.0.0.1:10001/getsorteddata?reverse=True&criteria=price
 
2.
 to get a single item (by id or location)
 http://127.0.0.1:10001/getitem?id= AAsm
 http://127.0.0.1:10001/getitem?location=[latitude,longitude]

3.
 to get list of items (by status or userid) 
 http://127.0.0.1:10001/getitemlist?status=AAsm
 http://127.0.0.1:10001/getitemlist?userid=AAsm

4.
 to get list of items in a radius 
 http://127.0.0.1:10001/get_items_in_radius?radius=xy&latitude=xx&longitude=yy


## Result of the above api's is returned in JSON format
