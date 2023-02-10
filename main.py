import json

from Layout import layout as lay
from Program import itt
import datetime as date
import os

if not os.path.isfile('data.json'):
    d = dict()
    open('data.json', 'a+').write(json.dumps(d))

itt.load()

lay.initial(date.datetime.today().year, date.datetime.today().month)
