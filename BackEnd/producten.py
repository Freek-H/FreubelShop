import mariadb
import json
import decimal

import os
import io
import PIL.Image as Image
from array import array

def vindalleproducten():
    #return '[{"name":"a","description":"b","img":"c"}]'
    mydb = mariadb.connect(
        host="localhost",  #port erbij indien mac
        user="root",
        password="",
        database="webshopusers"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM producten")
    rijen = [x for x in mycursor]
    naam = [x[0] for x in mycursor.description[0:3]]
    freubelItems = []
    for rij in rijen:
        freubelItem = {}
        # vul de dictionary met als key de kolomnaam
        # en als waarde de tabel entry van de huidige rij.
        for prop, val in zip(naam, rij):
            freubelItem[prop] = val
        freubelItems.append(freubelItem)
    jsonstring = json.dumps(freubelItems)
    return jsonstring

#def readimage(path):
#    count=os.stat(path).st_size / 2
#    with open(path, "rb") as f:
#        return bytearray(f.read())

def vindNonStandardGegevens():
    mydb = mariadb.connect(
        host="localhost",  #port erbij indien mac
        user="root",
        password="",
        database="webshopusers"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM producten")
    rijen = [x for x in mycursor]
    naam = [x[0] for x in mycursor.description]
    freubelItems = []
    for rij in rijen:
        freubelItem = {}
        # vul de dictionary met als key de kolomnaam
        # en als waarde de tabel entry van de huidige rij.
        for prop, val in zip(naam, rij):
            #print(type(val),val)
            if isinstance(val, (str, int, float, bool, type(None))):
                freubelItem[prop] = val
            elif isinstance(val, decimal.Decimal):
                freubelItem[prop] = float(val)
                #print(freubelItem)
            elif isinstance(val, bytes):
                continue
                #freubelItem[prop] = str(val)#('utf-8')
                # python/flask/backend-side image conversion - maar dat kan niet, want json.dumps() support geen img
                #image = Image.open(io.BytesIO(val))
                #freubelItem[prop] = image
            else:
                print(type(val))

        freubelItems.append(freubelItem)
    #print(freubelItems)
    jsonstring = json.dumps(freubelItems,skipkeys=True)
    #print(jsonstring)
    return jsonstring


#print(vindNonStandardGegevens())
vindNonStandardGegevens()