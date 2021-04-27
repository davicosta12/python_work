from user02 import User
from privileges_admin import Admin, Privileges

user01 = Admin('davi', 'silva', 21, 'masculino', 'solteiro', 6)

user01.admin_privileges.show_privileges()
