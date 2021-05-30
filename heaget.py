#!/usr/bin/python

import sys
import requests

vid=sys.argv[1]
m3u8=requests.get('https://media.heanet.ie/m3u8/'+vid).text
addr=m3u8.split('\n')[-2]
os.system('ffmpeg -i '+addr+' -c copy '+vid+'.mp4')
