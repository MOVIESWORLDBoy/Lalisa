if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/imran12ap76/Lalisa.git /Lalisa
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Lalisa
fi
cd /Lalisa
pip3 install -U -r requirements.txt
echo "Starting BOT...."
python3 bot.py
