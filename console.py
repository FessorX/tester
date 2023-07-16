#!/usr/bin/python3
"""
This is the console
"""
import cmd
import json
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
	"""Console command prompt to access models"""
	prompt = '(hbnb) '
	my_dict = {
		"BaseModel": BaseModel,
		"User": User,
		"State": State,
		"City": City,
		"Amenity": Amenity,
		"Place": Place,
		"Review": Review
			}

	def do_nothing(self, arg):
		""" Does nothing """
		pass

	def do_quit(self, arg):
		""" Close program and saves data safely """
		return True

	def do_EOF(self, arg):
		""" Using Ctrl+D Close program and saves data safely """
		print("")
		return True

	def emptyline(self):
		""" Overrides the empty line method """
		pass

	def do_create(self, arg):
		""" Creates a new instance of the basemodel class
		Structure: create [class name]
		"""
		if not arg:
			print("** class name missing **")
			return
		tokens = shlex.split(arg)
		if tokens[0] not in HBNBCommand.my_dict.keys():
			print("** class doesn't exist **")
			return
		new_instance = HBNBCommand.my_dict[tokens[0]]()
		new_instance.save()
		print(new_instance.id)

	def do_show(self, arg):
		"""
		Prints the string representation of an instance
		based on the class name and id
		Structure: show [class name] [id]
		"""
		tokens = shlex.split(arg)
		if len(tokens) == 0:
			print("** class name missing **")
			return
		if tokens[0] not in HBNBCommand.my_dict.keys():
			print("** class doesn't exist **")
			return
		if len(tokens) <= 1:
			print("** instance id missing **")
			return
		storage.reload()
		objects_dict = storage.all()
		key = tokens[0] + "." + tokens[1]
		if key in objects_dict:
			obj_instance = str(objects_dict[key])
			print(obj_instance)
		else:
			print("** no instance found **")

	def do_destroy(self, arg):
		"""
		Deletes an instance based on the class name and id
		(saves the changes into the JSON file)
		Structure: destroy [class name] [id]
		"""
		tokens = shlex.split(arg)
		if len(tokens) == 0:
			print("** class name missing **")
			return
		if tokens[0] not in HBNBCommand.my_dict.keys():
			print("** class doesn't exist **")
			return
		if len(tokens) <= 1:
			print("** instance id missing **")
			return
		storage.reload()
		objects_dict = storage.all()
		key = tokens[0] + "." + tokens[1]
		if key in objects_dict:
			del objects_dict[key]
			storage.save()
		else:
			print("** no instance found **")

	def do_all(self, arg):
		"""
		Prints all string representation of all instances
		based or not on the class name
		Structure: all [class name] or all
		"""
		# prints the whole file
		storage.reload()
		my_json = []
		objects_dict = storage.all()
		if not arg:
			for key in objects_dict:
				my_json.append(str(objects_dict[key]))
			print(json.dumps(my_json))
			return
		token = shlex.split(arg)
		if token[0] in HBNBCommand.my_dict.keys():
			for key in objects_dict:
				if token[0] in key:
					my_json.append(str(objects_dict[key]))
			print(json.dumps(my_json))
		else:
			print("** class doesn't exist **")

	def do_update(self, arg):
		"""
		Updates an instance based on the class name and
		id by adding or updating attribute
		(save the change into the JSON file).
		Structure: update [class name] [id] [arg_name] [arg_value]
		"""
		if not arg:
			print("** class name missing **")
			return
		tokens = shlex.split(arg)
		storage.reload()
		objects_dict = storage.all()
		if tokens[0] not in HBNBCommand.my_dict.keys():
			print("** class doesn't exist **")
			return
		if (len(tokens) == 1):
			print("** instance id missing **")
			return
		try:
			key = tokens[0] + "." + tokens[1]
			objects_dict[key]
		except KeyError:
			print("** no instance found **")
			return
		if (len(tokens) == 2):
			print("** attribute name missing **")
			return
		if (len(tokens) == 3):
			print("** value missing **")
			return
		my_instance = objects_dict[key]
		if hasattr(my_instance, tokens[2]):
			data_type = type(getattr(my_instance, tokens[2]))
			setattr(my_instance, tokens[2], data_type(tokens[3]))
		else:
			setattr(my_instance, tokens[2], tokens[3])
		storage.save()

	def do_update2(self, arg):
		"""
		Updates an instance based on the class name and
		id by adding or updating attribute
		(save the change into the JSON file).
		Structure: update [class name] [id] [dictionary]
		"""
		if not arg:
			print("** class name missing **")
			return

		my_dictionary = "{" + arg.split("{")[1]
		tokens = shlex.split(arg)
		storage.reload()
		objects_dict = storage.all()
		if tokens[0] not in HBNBCommand.my_dict.keys():
			print("** class doesn't exist **")
			return
		if (len(tokens) == 1):
			print("** instance id missing **")
			return
		try:
			key = tokens[0] + "." + tokens[1]
			objects_dict[key]
		except KeyError:
			print("** no instance found **")
			return
		if (my_dictionary == "{"):
			print("** attribute name missing **")
			return

		my_dictionary = my_dictionary.replace("\'", "\"")
		my_dictionary = json.loads(my_dictionary)
		my_instance = objects_dict[key]
		for my_key in my_dictionary:
			if hasattr(my_instance, my_key):
				data_type = type(getattr(my_instance, my_key))
				setattr(my_instance, my_key, my_dictionary[my_key])
			else:
				setattr(my_instance, my_key, my_dictionary[my_key])
		storage.save()

	def do_count(self, arg):
		"""
		Counts number of instances of a class
		"""
		x = 0
		objects_dict = storage.all()
		for key in objects_dict:
			if (arg in key):
				x += 1
		print(x)


if __name__ == '__main__':
	HBNBCommand().cmdloop()
