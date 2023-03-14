# myname = 'Febriansyah'
# text = f'My name is {myname}.'
# print(myname)

from datetime import datetime

today = datetime.now()

date_time = today.strftime('%Y-%m-%d-%H-%M-%S')

print(date_time)