# bmsbuy

It is selenium based script to check for availability of tickets and venues on bookmyshow.
It was orignally created for Avengers Endgame but it is written in generic way to later change it for any other service.
Systemd/Timer is used to trigger script every 20 minutes.

## Steps : 

#### 1 - Create and activate virtual envirnoment
```
python3.6 -m venv venv
source venv/bin/activate
```

#### 2 - Install requirements

`pip install -r requirements.txt`

#### 3 - Copy chromedriver to /usr/bin/ or add project root to path variable

#### 4 - Copy configs/config.json to root of project and add your bms credentials

#### 5 - Copy bms.service bms.timer to /etc/systemd/system/

#### 6 - Start the timer by

`sudo systemctl start bms.timer`
