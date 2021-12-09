from datetime import datetime
from package.application import salary
from package.application.db import people


if __name__ == '__main__':
    print(salary.calculate_salary(), datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'))
    print(people.get_employees(), datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'))
