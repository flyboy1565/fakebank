# fakebank
Scambaiting Fakebank

A tool to help fake out scammer while working calling them. 

Setup:
If python and pip are installed
```
cd pathtodownload/bank
# virtualenv -p $(which python3) venv
# source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations && python manage.py migrate
python manage.py createsuperuser
# generate a new unique key
python manage.py generate_secret_key --replace
```
