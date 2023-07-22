import os

import time 

# files and directories to be backedup
# mention them in a list

source=['/Users/harsha/Documents/git/moon']

target_dir='/Users/harsha/Documents/backup'

print(os.sep)
print(time.strftime('%Y%m%d%H%M%S'))

today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')

comment = input('Enter a comment --> ')
# Check if a comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

print(target)

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory',today)

zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

# Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
