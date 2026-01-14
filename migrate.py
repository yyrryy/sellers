import os
os.system('python3 manage.py makemigrations pis_product pis_retailer pis_ledger pis_sales pis_com')
os.system('python3 manage.py migrate')
