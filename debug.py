from lib.employee import *
from lib.manager import *

# Test your code here

# e.g.
#   m1 = Manager( 'Mr. Levi', 'HR', 33 )
#   e1 = Employee( 'Norris', 40000, m1 )

Man1 = Manager("Apples", "Retail", 45)
Man2 = Manager("Babadook", "Retail", 56)
Man3 = Manager("Mista Bones", "Spookin", 457)

Em1 = Employee("Sad Greg", 45000, Man2)
Em2 = Employee("The One who Knocks", 55000, Man2)
Em3 = Employee("The Eyes", 23000, Man1)
Em4 = Employee("Sleeper", 54000, Man3)





# do not remove
import ipdb; ipdb.set_trace()
