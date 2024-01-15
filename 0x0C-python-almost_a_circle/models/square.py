#!/usr/bin/python3
""" Module That contains class Square,
inheritance of class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
      """Initializes Class Square"""
      
      def __init__(self, size, x=0, y=0, id=None):
            """Initializes instances"""
            super().__init__(size, size, x, y , id)
                
                
      def __str__(self):
        """Returns a string representation of a Square instance."""

        result = "[Square] ({}) {} / {} - {} / {}".format(
            self.id, self.x, self.y, self.width, self.height
        )
        return result
      
      @property
      def size(self):
          """Getter Size"""
          return self.width
      
      @size.setter
      def size(self, value):
          """Setter Size"""
          self.width = value
          self.height = value

      def __str__(self):
        result = "[Square] ({}) {} / {} - {}".format(
            self.id, self.x, self.y, self.size
        )
        return result
      
      def update(self, *args, **kwargs):
          """Update Method"""
          if args != None and len(args) != 0:
              list_args = ['id', 'x', 'y', 'size']
              for i in range(len(args)):
                  if list_args[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
              else:
                  setattr(self, list_args[i], args[i])
          else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)
      def to_dictionary(self):
        """ Returns a dictionary with attributes """
        list_args = ['id', 'x', 'y', 'size']
        dict_res = {}
        for key in list_args:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)
        return dict_res
