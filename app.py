import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog
from keras.models import load_model
from keras_preprocessing import image
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import numpy as np

class Diagnotica(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui_app.ui", self)
        self.btnDiagnosis.clicked.connect(lambda: self.loadModel(self.txtPath.text()))
        self.btnBrowser.clicked.connect(self.browseFIle)

    def loadModel(self, file):
        # Cargar el modelo
        modelo_cargado = load_model('model/model_densenet201.h5')
        #print("El modelo se ha cargado: ", modelo_cargado)
        img_a_predecir = image.load_img(file, target_size=(224, 224))
        test_image = image.img_to_array(img_a_predecir)
        test_image = np.expand_dims(test_image, axis=0)
        test_image = test_image.astype('float32')
        test_image /= 255
        result = modelo_cargado.predict(test_image)[0][0]
        prediccion = 1 if (result >= 0.5) else 0
        CLASSES = ['Normal', 'Covid19+']
        ClassPred = CLASSES[prediccion]
        ClassProb = result
        self.txtName.setText(ClassPred)

    global path

    def browseFIle(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', 'C:', '*.jpg')
        self.txtPath.setText(filename[0])
        path = filename[0]
        self.showX(path)

    # Mostrar la imagen en el cuadro
    # Show the image in the box
    def showX(self, path):
        pixmap = QPixmap(path)
        pixmap_resized = pixmap.scaled(441, 411)
        self.xray.setPixmap(pixmap_resized)


if __name__ == '__main__':
    #Iniciar app
    app = QApplication(sys.argv)
    GUI = Diagnotica()
    GUI.show()
    sys.exit(app.exec())