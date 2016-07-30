# sefi - SEnd FIles
## instructions

You must have python and git installed. Open your terminal program of choice and move to the directory you would like to install to.
Then run:
    git clone https://github.com/siathema/sefi.git

Next run sefi with the directory of your choosing to generate a jason file for sefi:
    ./sefi [Path to directory]

If you want to have cron run it every 4 hours at half past the hour then first change your VISUAL enviroment variable to nano:
    export VISUAL=nano
    
This makes it easier to edit using crontab:
    crontab -e
    
Add this entry to your contab file:
    MAILTO=user@example.com                                                         
    30 0,4,8,16,20 * * * path-to-sefi/sefi.py path-to-directory   
