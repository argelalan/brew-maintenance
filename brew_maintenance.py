#!/usr/bin/env python3

import subprocess
from datetime import datetime as dt
import time


brew_command = '/usr/local/bin/brew'

subprocess.run([brew_command, 'update'])
outdated_result = subprocess.run([brew_command, 'outdated'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
if outdated_result.stdout:
    subprocess.run([brew_command, 'upgrade'])

current_date = dt.now()
current_localtime = time.localtime()
current_time = time.strftime('%H:%M:%S', current_localtime)
log_message = f'Updated at {current_time}'
print(log_message)
