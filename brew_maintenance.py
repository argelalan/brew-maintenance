#!/usr/bin/env python3

import subprocess

update_result = subprocess.run(['brew', 'update'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

if 'Already up-to-date.' not in update_result.stdout:
	outdated_result = subprocess.run(['brew', 'outdated'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
else:
	outdated_result = None

print(update_result)
