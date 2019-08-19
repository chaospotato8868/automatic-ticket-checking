# automatic-ticket-checking
Send an email if tickets available

use crontab to schedule a time to run python script

crontab -e
type i for insert
<!-- # ┌───────────── minute (0 - 59) -->
<!-- # │ ┌───────────── hour (0 - 23) -->
<!-- # │ │ ┌───────────── day of month (1 - 31) -->
<!-- # │ │ │ ┌───────────── month (1 - 12) -->
<!-- # │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday; -->
<!-- # │ │ │ │ │                                       7 is also Sunday on some systems) -->
<!-- # │ │ │ │ │ -->
<!-- # │ │ │ │ │ -->
<!-- # * * * * *  command_to_execute -->

<!-- # 30 22 * * * /Users/dingchao8868/anaconda3/bin/python3 /Users/dingchao8868/Documents/GitHub/automatic-ticket-checking/ticket.py -->

type esc then :wq to save and quit

crontab -l to check 

