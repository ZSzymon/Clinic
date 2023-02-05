
#
#from django.test import TestCase
#from main_app.models import *
#from django.utils.timezone import now
#
#
#class test_models(TestCase):
#
#    def test_test(self):
#        result = test.objects.filter(numer=3).delete()
#        t = test.objects.create(name='ss', numer=3)
#        assert t.numer == 3
#
#    def test_doctor(self):
#        d = Doctors.objects.create(first_name='szymon',
#                                   second_name='zywko',
#                                   email='szymonzywko@gmail.com',
#                                   pesel=99041202454,
#                                   data_of_birth=now(),
#                                   register_date=now(),
#                                   person_info=None,
#                                   position_id=0)
#        d.save()
#        d_db = Doctors.objects.filter(pesel=99041202454).first()
#
#        assert 'szymonzywko@gmail.com' == d_db.email
#
#    def test_patients(self):
#        p = Patients.objects.create(first_name='szymon',
#                                    second_name='zywko',
#                                    email='szymonzywko@gmail.com',
#                                    pesel=99041202454,
#                                    data_of_birth=now(),
#                                    register_date=now(),
#                                    person_info=None,
#                                    position_id=0)
#        p.save()
#        p_db = Patients.objects.filter(pesel=99041202454).first()
#
#        assert 'szymonzywko@gmail.com' == p_db.email
#    def test_insert_drug(self):
#        drug = Drugs.objects.create(icd_10cm_code = 'A06.2',
#                                    icd_10_name = 'Amebiasis',
#                                    quantity = 10,
#                                    price = float(34.1))
#        drug.save()
#        inserted_drug = Drugs.objects.filter(icd_10cm_code = 'A06.2').first()
#        assert 'Amebiasis' == inserted_drug.icd_10_name
#    def
#
#