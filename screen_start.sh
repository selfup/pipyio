echo '
   Server will boot up and run in the background
   This should not take long at all :)
'
FLASK_APP=main.py screen -d -m flask run -p 9001
