#/usr/bin/env bash -e

VENV=venv

if [ ! -d "$VENV" ]
then

    PYTHON=`which python3`

    if [ ! -f $PYTHON ]
    then
        echo "could not find python"
    fi
    virtualenv -p $PYTHON $VENV

fi

. $VENV/bin/activate
chmod +x /var/lib/snips/skills/Snips-Football-Skill/action-Fußball.py
pip install -r requirements.txt
if [ ! -d ligen ]
then
    echo 'Folder was successfully created'
    mkdir ligen
else
    echo "Folder already exists"
fi
python3 write.py
chown -R _snips-skills:_snips-skills ligen
