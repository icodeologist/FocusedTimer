import time
from pydub import AudioSegment
from pydub.playback import play



def main():

    POMODORO_TIMER = 0
        
    pomodoro_song = AudioSegment.from_mp3("../FocusClock/music/ios.mp3")
    pomodoro_break_song = AudioSegment.from_mp3("../FocusClock/music/break.mp3")


    def setTime(t):
        i = 0
        t = t * 60
        for i in range(t+1):
            time.sleep(1)
            #kind of fizz buzz because where will use it anyways haha
            if i % 10 == 0:
                print("Get back to focus Dont look at me")
            else:
                print(i)
        print("Time is over")
        play(pomodoro_song)
        getBreakTime = input("Get 5 min quick Break: ")
        if getBreakTime == 'y' or getBreakTime.lower() == "yes" or getBreakTime.upper() == "YES":
            addBreak(5)
        else:
            exit()

    def addBreak(t):
        timer = t*60
        for i in range(timer+1, -1, -1):
            time.sleep(1)
            remaining = i - 1
            print("Your break ends in ", remaining)
        play(pomodoro_break_song)
        
        #continue with one more Your
        while True:
            try:
                restart = str(input("Do you want to start another session(y/n)"))
                if restart.lower() == 'y' or restart.upper() == "Y":
                    break
                else:
                    exit()
            except ValueError:
                print("Please enter Y/y or N/n to the console")
                time.sleep(1)

        setTime(POMODORO_TIMER)

    #Pomodoro timer in Mins
    print("Welcome Set a time for Pomodoro")
    while True:
        try:
            getUserIp = int(input("Enter the time you wanna focus in minutes(1 is min and 60 is max) : "))
            if getUserIp >=  1 and getUserIp <= 60:
                POMODORO_TIMER = getUserIp
                break
            else:
                print("Please enter the time between 1 and 60 minutes")
        except ValueError:
            print("Please enter a valid digit")
            time.sleep(1)

    #get getUserIp and set time 
    setTime(getUserIp)
main()

