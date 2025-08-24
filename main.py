#!/usr/bin/env python3
from PySide6.QtWidgets import QApplication
from gui.gui import Widget
import os
import sys

app = QApplication(sys.argv)

audio_path = "audio/croods_song.mp3"
img_path = "img/grug.jpg"
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

window = Widget(audio_path, img_path)
window.show()

app.exec()