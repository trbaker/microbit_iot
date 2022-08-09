import serial
import requests
import json
import time

ser = serial.Serial('/dev/cu.usbmodem143202', 115200, timeout=None)
while True:
    data_raw = ser.readline()
    # next few lines just clean up the serial data
    tempf = str(data_raw)[:7]
    tempf = tempf.replace("b'", "")
    # print to screen (for now)
    print(tempf)
    # send data to sample ArcGIS Online service
    url = 'https://services3.arcgis.com/GzteEaZqBuJ6GIYr/arcgis/rest/services/survey123_910b6ea1c50743269a5b171a91fe6cc7_fieldworker/FeatureServer/0/addFeatures'
    params={"f":"pjson","token":"","rollbackOnFailure":"false","features":'{ \
        "attributes" : { \
            "controller" : "microbit sensor 1", \
            "lat" : -94.23434, \
            "lon": -94.2342, \
            "temperature" : tempf, \
            "humidity" : 0}}'
            }
    x = requests.post(url, params=params)
    time.sleep(180)       # integer is seconds to pause
