#!/usr/bin/env python3

import os
import sys
import wave

import aiy.audio
import aiy.cloudspeech
from src.my_assistant import MyAssistant

sys.path.append(os.path.realpath(os.path.join(__file__, '..', '..')) + '/src/')


class AudioAssistant(MyAssistant):
    
    def __init__(self):
        MyAssistant.__init__(self)
    
    #local commands - record file
    def record_file():
        wave_file = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    
        try:
            print('Recording ...')
            aiy.audio.record_to_wave(wave_file, RECORD_DURATION_SECONDS)
        except:
            print('Problems with recording')
        wave_file.close()
    

        
        


#voice commands
RECORD_DURATION_SECONDS = 5
WAVE_OUTPUT_FILENAME = ''



    #local commands - repeat
#    def repeat_after_me():
#        assistant = aiy.assistant.grpc.get_assistant()
#        with aiy.audio.get_recorder():
#            while True:
#                print('Listening ...')
#                text, audio = assistant.recognize()
#                if text is not None:
#                    print('You said, "', text, '"')
#                    aiy.audio.say(text)
#                else:
#                    print('I did not hear you')
    
#    def delete_file(wave_file):
#        try:
#            print('deleting file ...')
#        except FileNotFoundError:
#            pass 