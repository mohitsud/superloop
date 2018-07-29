### THIS MODULE RENDERS THE TEMPLATES FROM THE JINJA2 FILES
### AND PACKAGES THEM INTO A LIST OF LISTS. THIS IS STORED IN THE 
### GLOBAL VARIABLE CALL INITIALIZE.CONFIGURATION.

from jinja2 import Environment, FileSystemLoader
from parse_commands import parse_commands
import initialize

def render_config(template,node_object):

	env = Environment(loader=FileSystemLoader('.'))
	baseline = env.get_template(template)
	print("THE FOLLOWING CODE WILL BE PUSHED:")

	for index in initialize.element:
		f = open("config.conf", "w") 
		config_list = []
		config = baseline.render(nodes = node_object[index])
		print ("{}".format(node_object[index]['hostname']) + "#")
		f.write(config) 
		f.close 
		print("{}".format(config))
		f = open("config.conf", "r") 
		init_config = f.readlines()

		for config_line in init_config:
			strip_config = config_line.strip('\n')
			config_list.append(strip_config)		

		initialize.configuration.append(config_list)

	return None

