## importing all the libraries

import speech_recognition as sr
import wave
from tqdm import tqdm
import os
# import pickle
import sys
import contextlib
r = sr.Recognizer()
os.chdir(r'D:\SUDHEENDRA INFO 5082 Project\Project\STT_apr')
# fname = 'IHFL Q2-21.wav'

def run_stt(filename):
    transcript=[]
    audio_file = sr.AudioFile(filename)
    with contextlib.closing(wave.open(filename,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    repetations=int(duration//30)
    if repetations >0:
        with audio_file as source:
            for i in tqdm(range(repetations+1)):
                audio = r.record(source,duration=30)
                recognised_audio = r.recognize_google(audio)
                transcript.append(recognised_audio)
    else:
        with audio_file as source:
            audio = r.record(source,duration=duration)
            recognised_audio=r.recognize_google(audio)
            transcript.append(recognised_audio)
    transcript_final=' '.join(transcript)
    output_file_name=filename.replace('.wav','.txt')
    try:
        os.makedirs(os.sep.join([os.getcwd(),'text files']))
    except:
        pass
    text_file_dir=os.sep.join([os.getcwd(),'text files'])
    with open(os.sep.join([text_file_dir,output_file_name]), 'w') as f:
        f.write(transcript_final)

if __name__ == '__main__':
    fname_argument = "Cliped.wav"
    run_stt(fname_argument)
