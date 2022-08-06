 #!/usr/bin/env python3

import subprocess

subprocess.run(['brew', 'update'])

outdated_result = subprocess.run(['brew', 'outdated'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
if outdated_result.stdout:
    subprocess.run(['brew', 'upgrade'])
