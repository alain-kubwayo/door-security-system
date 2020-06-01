1. Install Anaconda Python and Spyder on Windows 10
2. Visit www.anaconda.com/download and select the one with Python 3.6
3. Run the executable file 
4. Using Anaconda Prompt from the start menu:
> python --version
>conda info
>conda install numpy
>start spyder and press enter to start Spyder IDE

Start Menu and select Anaconda navigator: create an environment (opencv)
from Ananconda prompt, run the following command: activate opencv
start running the codes provided:

a) sampleCollect.py (which was mainly used for the project) will collect 150 faces (this number can be increased or reduced) with faceSample folder created, inside the project folder, to store the faces being captured. 
b) sampleCollectMany.py is used for collecting faces of multiple individuals to be recognized by the system
c) mainWithoutNotify.py to train the samples collected and recognize real-time face (this does not send the notification).
d) mainWithNotify.py is used to train faces collected and recognize real-time face with an option to send email notification. 
e) notify.py can be run to send a mail notification using SMTP (Simple Mail Transfer Protocol was used. notify.py can be run as a standalone module just to ensure that the notification can be sent)
f) lock.py is used for the locking mechanism but was never run since it was designed to be run on Raspberry Pi (Raspbian OS).
g) Similarly, buzzer.py was designed but never run for similar reason. There were no physical components to test the code. 

In the face recognition code called "mainWithNotification.py" the receiverEmail should be replaced by the tester's email to ensure that the email sent by the system is sent directly to that accessible email (what is there is my own), otherwise, the email will not be delivered to the recipient. 

sampleCollect.py collects face samples to be used or fed into the recognition code which is either mainWithoutNotify.py or mainWithNotify.py

buzzer.py and lock.py were designed to run on Rasbian operating system of Raspberry Pi, unless they are run on Raspian or any similar system with circuits physically connected, they won't run normally. These two codes were designed and written conceptionally but not fully tested on any system because Raspberry Pi, buzzer, and lock were not physically available. You can refer to buzzer.png and lock.png for the circuit diagrams.

Two videos were included for demonstrating how mainWithNotify.py and mainWithoutNotify.py were run and the results of the process. 