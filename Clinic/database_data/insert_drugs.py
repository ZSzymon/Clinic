
from django.utils import timezone
import os, sys



PROJECT_NAME = 'Clinic'
PROJECT_PATH = '/Clinic'
sys.path.append(PROJECT_PATH)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '%s.settings' % PROJECT_NAME)
FILE_PATH = 'C:\\tmp\\Clinic-Project\\Clinic\\database_data\\drugs.txt'

import django
django.setup()
from main_app.models import *
from pharmacy.models import Drug
def start():
    Drug.objects.all().delete()
    with open(FILE_PATH, 'r') as file:
        stop = 9999990
        for i, line in enumerate(file, 0):
            if i > stop:
                break

            if (line.startswith('<li>')):
                begin = str(line).find('">',15)
                end = str(line).find('</a>')
                new_line = line[begin+2:end]

                d = Drug.objects.filter(name = new_line).first()
                if not d:
                    drug = Drug.objects.create(name = new_line).save()
                    print('insert ' + str(new_line))
                
                    
                    

            pass

if __name__ == '__main__':
    start()