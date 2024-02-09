#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import storage

class HBNBCommand(cmd.Cmd):
	prompt = '(hbnb) '

	def do_quit(self, arg):
		"""Quit command to exit the program"""
		return True

	def do_EOF(self, arg):
		"""EOF command to exit the program"""
		return True

	def emptyline(self):
		pass

	def do_create(self, arg):
		"""Creates a new instance of BaseModel, saves it to the JSON file, and prints the id."""
		if not arg:
			print("** class name missing **")
			return

		classes = {"BaseModel": BaseModel, "User": User "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}
		args = arg.split()

		if args[0] not in classes:
			print("** class doesn't exist **")
			return

		new_instance = classes[args[0]]()
		new_instance.save()
		print(new_instance.id)

	def do_show(self, arg):
		"""Prints the string representation of an instance."""
		if not arg:
			print("** class name missing **")
			return

		args = arg.split()
        if args[0] not in {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}:
			print("** class doesn't exist **")
			return

		if len(args) < 2:
			print("** instance id missing **")
			return

		key = "{}.{}".format(args[0], args[1])
		objects = storage.all()
		if key in objects:
			print(objects[key])
		else:
			print("** no instance found **")

	def do_destroy(self, arg):
		"""Deletes an instance based on the class name and id."""
		if not arg:
			print("** class name missing **")
			return

		args = arg.split()
		if args[0] not in {"BaseModel", "User"}:
			print("** class doesn't exist **")
			return

		if len(args) < 2:
			print("** instance id missing **")
			return

		key = "{}.{}".format(args[0], args[1])
		objects = storage.all()
		if key in objects:
			del objects[key]
			storage.save()
		else:
			print("** no instance found **")

	def do_all(self, arg):
		"""Prints all string representation of all instances."""
		classes = {"BaseModel": BaseModel, "User": User, "State", "City", "Amenity", "Place", "Review"}

		if arg and arg not in classes:
			print("** class doesn't exist **")
			return

		objects = storage.all()
		if arg:
			objs = [str(v) for k, v in objects.items() if k.startswith(arg + ".")]
		else:
			objs = [str(v) for v in objects.values()]

		print(objs)

	def do_update(self, arg):
		"""Updates an instance based on the class name and id by adding or updating attribute."""
		if not arg:
			print("** class name missing **")
			return

		args = arg.split()
		if args[0] not in {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}:
			print("** class doesn't exist **")
			return

		if len(args) < 2:
			print("** instance id missing **")
			return

		key = "{}.{}".format(args[0], args[1])
		objects = storage.all()
		if key not in objects:
			print("** no instance found **")
			return

		if len(args) < 3:
			print("** attribute name missing **")
			return

		if len(args) < 4:
			print("** value missing **")
			return

		obj = objects[key]
		setattr(obj, args[2], args[3])
		storage.save()

if _name_ == '_main_':
	HBNBCommand().cmdloop()
