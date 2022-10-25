#!/usr/bin/env python3

import subprocess
from datetime import datetime as dt
import time
import os


brew_command = '/usr/local/bin/brew'

subprocess.run([brew_command, 'update'])
outdated_result = subprocess.run([brew_command, 'outdated'], stdout=subprocess.PIPE, text=True)
if outdated_result.stdout:
    subprocess.run([brew_command, 'upgrade'])
    subprocess.run([brew_command, 'cleanup'])

current_date = dt.now()
current_date = current_date.strftime('%m/%d/%Y')
current_localtime = time.localtime()
current_time = time.strftime('%H:%M:%S', current_localtime)
log_message = f'Updated {current_date} - {current_time}\n'

log_file_path = os.environ['BREW_MAINTENANCE_LOG_FILE_PATH']
with open(log_file_path, 'a') as log_file:
    log_file.write(log_message)
