class Privilege(object):
    "Privilege definition associated with a Role"

    def __init__(self):
        self._readPrivilege = []
        self._writePrivilege = []
        self._deletePrivilege = []

    def read(self, role, method, data):
        """Add rules to allow read access :param role: Role of this rule , method: READ :param data: The data one wants to access"""
        privilege = (role.get_name(), method, data)
        if privilege  not in self._readPrivilege:
            self._readPrivilege.append(privilege)

    def write(self, role, method, data):
        """Add rules to allow read access :param role: Role of this rule , method: WRITE :param data: The data one wants to  write to """
        privilege  = (role.get_name(), method, data)
        if privilege  not in self._writePrivilege:
            self._writePrivilege.append(privilege)

    def delete(self, role, method, data):
        """Add rules to allow read access :param role: Role of this rule , method: DELETE :param data: The data one need o delete"""

        privilege  = (role.get_name(), method,data)
        if privilege not in self._deletePrivilege:
            self._deletePrivilege.append(privilege)

    def readeallowed(self, role, method, data):
        """returns whether the role is allowed READ access resource
        :return: Boolean
        """
        return (role, method, data) in self._readPrivilege

    def writeeallowed(self, role, method, data):
        """returns whether the role is allowed WRITE access resource
        :return: Boolean
        """
        return (role, method, data) in self._writePrivilege

    def deleteallowed(self, role, method, data):
        """returns whether the role is allowed DELETE access resource
        :return: Boolean
        """
        return (role, method, data) in self._deletePrivilege