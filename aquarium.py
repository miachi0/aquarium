import requests
import html
import datetime

# get temperature data from sensor
r = requests.get('https://api.particle.io/v1/devices/33003b000b47373336373936/temperature?access_token=1c476acb47bd0b944a031e2859ef7160e4b72a66')
print(r)
print(r.json())
print("temperature result")
print(r.json()["result"])
temp = ("%2.f" % r.json()['result'])
print()


()

#get conductivity data from sensor
r = requests.get('https://api.particle.io/v1/devices/33003b000b47373336373936/conductivity?access_token=1c476acb47bd0b944a031e2859ef7160e4b72a66')
print("conductivity")
cond = ("%.2f" % r.json()["result"])
print(cond)
print()

# get pH data from sensor
requests.get('https://api.particle.io/v1/devices/33003b000b47373336373936/conductivity?access_token=1c476acb47bd0b944a031e2859ef7160e4b72a66')
print("ph")
print(r.json()["result"])
ph = ("%.2f" % r.json()["result"])
print()

# get time
now = datetime.datetime.now()
date_stamp = now.strftime("%Y-%b-%d %H:%M")

# update aquarium.csv file
f = open('/var/www/html/aquarium/aquarium.csv', 'a')      
f.write(date_stamp + ',' + temp + ',' + cond + ',' + ph + '\n')
f.close()



f = open('/var/www/html/aquarium/aquarium.html','w')

message = """
<h1>Environmental Controls</h1>

<p>The temperature of the aquarium is %s </p>
<p>The conductivity of the aquarium is %s </p>
<p>The ph of the aquarium is %s </p>

<p>Follow these links to see more graphs</p>
<p><a href="aquarium_temp.html">Temperature graph</a></p>

""" % (html.escape(temp), html.escape(cond), html.escape(ph))

f.write(message)
f.close()
print("finished")





