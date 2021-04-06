#!/bin/su root

echo > "Run me with sudo"
echo > "Trying to define Main.py with chmod"
chmod +x Main.py
chown root runner.sh
chmod 700 runner.sh
chown root ./
chmod 755 ./
ALL NOPASSWD: runner.sh
echo > "Can be run now with runner.sh, running now"
./runner.sh


