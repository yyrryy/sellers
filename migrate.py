import os
os.system('py manage.py makemigrations pis_product pis_retailer pis_ledger pis_sales pis_com')
os.system('py manage.py migrate')
