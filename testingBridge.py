import sys
from phue import Bridge

b = Bridge('192.168.0.10')

# lights = b.lights
	
lights = b.get_light_objects('id')
#
# for l in lights:
# 	print(l.name)

# print(lights)


# for l in lights:
# 	print(lights[l].light_id)


# i = 1
# if i in lights:
# 	print(lights[i].light_id)



def lightSelected(index):
	if index in lights:
		# print(lights[index].light_id)
		
		return index
		print(index)

a = lightSelected(1)

a
