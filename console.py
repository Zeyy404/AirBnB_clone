#!/usr/bin/python3
"""A console module"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """A console that contains the entry point of the command interpreter"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel,
           saves it (to the JSON file) and prints the id.
        """
        if not args:
            print("** class name missing **")
        else:
            try:
                instance = storage.class_()[args]()
                instance.save()
                print(f"{instance.id}")
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string representation of an instance
             based on the class name and id.
        """
        arg = args.split()
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg[0]
            if class_name not in storage.class_():
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            else:
                instance_id = arg[1]
                key = f"{class_name}.{instance_id}"
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name
             and id (save the change into the JSON file).
        """
        arg = args.split()
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg[0]
            if class_name not in storage.class_():
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            else:
                instance_id = arg[1]
                key = f"{class_name}.{instance_id}"
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
            based or not on the class name.
        """
        arg = args.split()
        if arg:
            class_name = arg[0]
            if class_name not in storage.class_():
                print("** class doesn't exist **")
                return

            instances = storage.all().values()
            obj_list = [str(obj) for obj in instances
                        if isinstance(obj, storage.class_()[class_name])]
            print(obj_list)
        else:
            instances = [str(obj) for key, obj in storage.all().items()]
            print(instances)

    def do_update(self, args):
        """ Updates an instance based on the class name and id
             by adding or updating attribute
            (save the change into the JSON file).
        """
        arg = args.split()
        if not args:
            print("** class name missing **")
            return

        class_name = arg[0]
        if class_name not in storage.class_():
            print("** class doesn't exist **")
            return

        if len(arg) < 2:
            print("** instance id missing **")
            return

        instance_id = arg[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all().get(key)

        if len(arg) < 3:
            print("** attribute name missing **")
            return

        attr_name = arg[2]

        if len(arg) < 4:
            print("** value missing **")
            return

        attr_value = arg[3]
        try:
            if isinstance(getattr(instance, attr_name), int):
                attr_value = int(attr_value)
            if isinstance(getattr(instance, attr_name), float):
                attr_value = float(attr_value)
        except ValueError:
            pass
        setattr(storage.all()[key], attr_name, attr_value)
        storage.all()[key].save()

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program on EOF (Ctrl+D)"""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
