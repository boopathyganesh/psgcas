# build_files.sh
sudo apt install python3.10-venv build-essential python3-dev
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

# make migrations
python3 manage.py migrate
python3 manage.py collectstatic
