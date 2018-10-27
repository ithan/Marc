# Readme
## The rasperry will be programmed in Python, using the following librarys:

  - RPi.GPIO 0.6.4: https://pypi.org/project/RPi.GPIO/#files
  - datetime to check the current time.
  - socket & sys to send events to a server.
  - pygame, which should already be installed, to play sounds.


  ```
  [How to install?]
  ```
    - Copy the .tar.gz file that contains the project to the current folder in the Rasperry using an FTP connection.
      (You can copy it to a temporary directory such as /va /www/temp and then move it to the desired directory with mv /var/tmp/RPi.GPIO-0.6.4.tar.gz RPi.GPIO-0.6.4.tar.gz )
    - Unzip the file with tar ""-zxvf RPi.GPIO-0.6.4.tar.gz"
    - Move to the directory that was created with "cd RPi.GPIO-0.6.4"
    - Run the installer with "sudo python setup.py install"
    - Move the inout.py to /var/www/temp
    - Move to the folder where you want the scripts, for example /home/pi/scripts (You can create the directory with the command "sudo mkdir /home/pi/scripts" and move with
      "cd /home/pi/scripts")
    - Copy the file with "mv /var/tmp/inout.py inout.py"
    - Execute the file with "sudo python inout.py"
