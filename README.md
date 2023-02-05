# Clinic-Project
Projekt na zaliczenie przedmiotu.

### Instalacja:
        1. Create any virtual enviroment.
        2. `pip install -r requirements.txt`
        3. Delete every file except `__init__.py` in directories account.migrations,\
           main_app.migrations, pharmacy.migrations, 
        4. Delete db.sqlte3 
        5. python manage.py makemigrations
        6. python manage.py migrate
        7. python manage.py runserver


### Funkcjonalności:
Changed default Account model in order to use Email instead of login for authorization.
            
![Rejestracja](docs/rejestracja.png)
![Logowanie](docs/logowanie.png)

#### Home Page:
    Possibility to add Articles to home page through admin page.


#### Profile Page:
    Profile info
    Information about incoming appointement.
![Profil](docs/profile.png)

#### Personal Note:
    - Adding
    - Update
    - Delete
![Notebook](docs/notebook.png)
    

### Pharmacy 
    Admin have access to create prescriptions for clients.
    Admin have access to add druges to store.
    People in pharmacy has list of prescriptions to buy. 
    In store people can add drugs to cart.
![img.png](docs/pharmacyhome.png)
![DrugStore](docs/DrugStore.png)
![DrugStore](docs/pharmacyHomeAdmin.png)
![DrugStore](docs/DrugsList.png)


    

### Cart
    Possibility to modify cart.
![](docs/cart.png)

    Possibility to see cart page.
![](docs/cartPage.png)




### Drug Managing.
    Add prescription
![](docs/addPrescription.png)

    Prescription List
![](docs/prescriptionsList.png)
    
        

    
            
    
