class Role(object):
    """param :name of role"""


    roles = {}

    def __init__(self, name=None):
        """Role initialization with permissions it has"""
        self.name = name
        Role.roles[name] = self

    def get_name(self):
        """to return the name of the role"""
        return self.name

