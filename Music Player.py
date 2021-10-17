from kivy.app import App
from kivy.core.audio import SoundLoader,Sound
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import random as rand
import os


def list_of_music():
    files = os.listdir('music')
    return files

def place(folder_name,file_name):
    place_of_file = folder_name+'/'+file_name
    return place_of_file


base_of_music = list_of_music()
first_bit = True


class Song:
    def __init__(self,PlayMusic, file=''):
        self.PlayMusic = PlayMusic
        self.file = file
    def play_song(self,song):
        if self.PlayMusic:
            song.play()
        else:
            song.stop()


class SayHello(App):

    def build(self):
        # returns a window object with all it's widgets
        self.firstBit = True
        self.text = ''
        self.sound = None
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        self.greeting2 = Label(
            text="Choose music...",
            font_size=24,
            color='#FFFF00'
        )
        self.window.add_widget(self.greeting2)
        self.button2 = Button(
            size_hint_x=20,
            width=50,
            text="Random music",
            size_hint=(1, 0.5),
            bold=True,
            font_size=24,
            background_color='#ffc0cb',
            # remove darker overlay of background colour
            # background_normal = ""
        )
        self.button2.bind(on_press=self.Sound)
        self.window.add_widget(self.button2)
        return self.window

    def Sound(self,instance):
        if self.firstBit:
            #start song
            random_integer = rand.randint(0, len(base_of_music)-1)
            self.text = base_of_music[random_integer] # search random name of song
            self.sound = SoundLoader.load(place(folder_name='music', file_name=self.text))
            self.song1 = Song(PlayMusic=True)
            self.song1.play_song(song = self.sound)
        else:
            #stop song
            self.song1.PlayMusic = False
            self.song1.play_song(song = self.sound)
            #start new random song
            random_integer = rand.randint(0, len(base_of_music)-1)
            self.text = base_of_music[random_integer]
            self.sound = SoundLoader.load(place(folder_name='music', file_name=self.text))
            self.song1.song = self.sound
            self.song1.PlayMusic = True
            self.song1.play_song(song = self.sound)
        self.firstBit = False
        self.greeting2.text = self.text

if __name__ == "__main__":
    SayHello().run()