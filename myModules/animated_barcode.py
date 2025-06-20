from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QColorDialog,
    QFileDialog,
)
from PySide6.QtGui import QIcon,QMovie,QColor,QPixmap
from PySide6.QtCore import QByteArray
import sys
from qt_material import apply_stylesheet
import segno
from urllib.request import urlopen

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.myColor = QColor("black")

        # Layout
        self.Box = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()

        # Widgets
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')

        self.linkLabel = QLabel(self)
        self.linkLabel.setText('Link:')

        self.link = QLineEdit()
        self.gif = QLineEdit()
        self.name = QLineEdit()

        self.url = QPushButton('Generate')
        self.url.clicked.connect(self.QRmaker)

        

        self.Qr = QLabel(self)
        self.Qr.setVisible(False)

        # Adding Widget to layout
        row1.addWidget(self.nameLabel)
        row1.addWidget(self.name)

        row2.addWidget(self.linkLabel)
        row2.addWidget(self.link)

        self.Box.addLayout(row1)
        self.Box.addLayout(row2)

        self.Box.addWidget(self.gif)
        self.Box.addWidget(self.url)
        self.Box.addWidget(self.Qr)
        
        # Setting the layout of final window
        self.setLayout(self.Box)
        
    def QRmaker(self):
        name = self.name.text()
        # qr = qrcode.QRCode(
        # version=1,
        # error_correction=qrcode.constants.ERROR_CORRECT_L,
        # box_size=10,
        # border=4,
        # )
        # qr.add_data(self.link.text())
        # qr.make(fit=True)
        # # print(self.myColor)
        # img = qr.make_image(fill_color=self.myColor, back_color="white")
        # img.save(f"{name}.png")
        slts_qrcode = segno.make_qr(self.link.text())
        nirvana_url = urlopen(self.gif.text())
        slts_qrcode.to_artistic(
            background=nirvana_url,
            target=f"{name}.gif",
            scale=10,
            )

        self.movie = QMovie(f'{name}.gif', QByteArray(), self) 
        self.movie.setCacheMode(QMovie.CacheAll) 
        self.movie.setSpeed(100) 
        self.Qr.setMovie(self.movie)
        self.movie.start()

        # pixmap = QPixmap(f'{name}.gif')
        # self.Qr.setPixmap(pixmap)
        # self.resize(pixmap.width(), pixmap.height())
        self.Qr.setVisible(True)

        
    
    def on_click(self):
        print("on")
        self.openColorDialog()

    def openColorDialog(self):
        print("open")
        color = QColorDialog.getColor()
        

        if color.isValid():
            self.myColor = color.name()
            print(self.myColor)
        else:
            self.myColor = "black"
            
    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select a directory", "/home")
        if directory:
            print(directory)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app,theme="dark_cyan.xml")
    window = MainWindow()
    window.show()

    app.exec()