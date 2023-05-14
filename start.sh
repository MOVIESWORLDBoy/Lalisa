if [ -z $UPSTREAM_REPO ]

then

  echo "Cloning main Repository"

  git clone https://github.com/imran12ap76/Lalisa.git /app

else

  echo "Cloning Custom Repo from $UPSTREAM_REPO "

  git clone $UPSTREAM_REPO /app

fi

cd /app

pip3 install -U -r requirements.txt

echo "Starting DQ-The-File-Donor...."

python3 bot.py
