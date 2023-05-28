import speech_recognition as sr
import pyautogui as pag

next_slide = "please switch to the next page"
previous_slide = "please switch to the previous page"

other_window = "please switch to the other window"

start_slideshow_from_beginning = "please start the slideshow from the beginning" # for Google Slides only
start_slideshow_here = "please start the slideshow from this slide" # for Google Slides only

start_slideshow_from_first_slide = "please start the presentation from the beginning" # for MS PowerPoint only
start_slideshow_from_current_slide = "please start the presentation from here" # for MS PowerPoint only

end_slideshow = "please stop the presentation"

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language='en-IN')
        print(command)

        if command == next_slide:
            pag.press('right') 
        elif command == previous_slide:
            pag.press('left')

        elif command == other_window:
            pag.hotkey('alt', 'tab')

        elif command == start_slideshow_from_beginning:
            pag.hotkey('ctrl', 'shift', 'f5')
        elif command == start_slideshow_here:
            pag.hotkey('ctrl', 'f5')

        elif command == start_slideshow_from_first_slide:
            pag.hotkey('f5')
        elif command == start_slideshow_from_current_slide:
            pag.hotkey('shift', 'f5')

        elif command == end_slideshow:
             pag.hotkey('esc')

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
