from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl

class Widget(QWidget):
    def __init__(self, audio_path, earrape_path, img_path, gurg_path, parent=None):
        super().__init__()

        #Sets audio player
        self.audio_output = QAudioOutput()
        self.player = QMediaPlayer()
        self.player.setAudioOutput(self.audio_output)
        self.audio_path = audio_path
        self.player.setLoops(QMediaPlayer.Infinite)
        self.earrape_path = earrape_path

        #Sets window title
        self.setWindowTitle("Grug")

        #Sets default window size
        self.resize(600,600)

        #Remove window borders and make background transparent
        self.setWindowFlag(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #Creat QLabel to display the GIF
        self.label = QLabel(self)
        self.label.setAttribute(Qt.WA_TranslucentBackground)

        #Loads/Starts GIF
        self.img_path = img_path
        self.gurg_path = gurg_path
        self.movie = QMovie(img_path)
        self.label.setMovie(self.movie)
        self.movie.start()

    #Makes the window resizable
    def resizeEvent(self, event):
        new_size = self.size()
        self.movie.setScaledSize(new_size)
        self.label.resize(new_size)

    #Mouse press event to start dragging
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()


    def mouseMoveEvent(self, event):
        if self.is_dragging:
            self.move(event.globalPos() - self.drag_position)
            event.accept()


    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = False
            event.accept()
    
    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.player.setSource(QUrl.fromLocalFile(self.audio_path))
            self.movie = QMovie(self.img_path)
            self.movie.setScaledSize(self.size())
            self.label.setMovie(self.movie)
            self.movie.start()
            self.player.play()

        elif event.button() == Qt.RightButton:
            self.player.stop()

        elif event.button() == Qt.MiddleButton:
            self.player.setSource(QUrl.fromLocalFile(self.earrape_path))
            self.movie = QMovie(self.gurg_path)
            self.movie.setScaledSize(self.size())
            self.label.setMovie(self.movie)
            self.movie.start()
            self.player.play()
