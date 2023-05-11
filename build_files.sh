# build_files.sh
pip install -r requirements.txt

# make migrations
python3.9 manage.py migrate 
python3.9 manage.py collectstatic

#linux update and install

apt-get update
apt-get upgrade
apt install mysql-server libmysqlclient-dev build-essential python3-dev

export PATH="/usr/local/bin:$PATH"
