#!/usr/bin/python3

import cgi
import img
import cont
import network

print("content-type: text/html")
print()
mydata=cgi.FieldStorage()

service = mydata.getvalue("service")
subser= mydata.getvalue("subser")

#---- Images Services ----
if service == "img":
    img.img_serv(subser,mydata)
    
#--- Container Service ----
if service == "cont":
    cont.cont_serv(subser,mydata)
      
#--- Network Service ---
if service == "net":
    network.net_serv(subser,mydata)