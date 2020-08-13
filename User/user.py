#User Class

class User(object):
    "Role assignment to USER"

    def __init__(self, roles = []):
        """Initialising the roles tagged to a user
        :param roles: LIST that contains the roles tagged  to a user
        """

        self.roles = set(roles)

    def add_role(self, role):
        """Add the given role to the user

        :param role: the role which has to be assigned to user
        """
        self.roles.add(role)

    def get_roles(self):

        return self.roles


    def removeassignedrole(self, role_name):
        """Remove a role assigned to a User

        :param role_name: name of the role which needs to be removed
        """
        for role in self.get_roles():
            if role.get_name() == role_name:
                self.roles.remove(role)
