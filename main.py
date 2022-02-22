from  PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow
import sys
from combinatoric import Combinatoric

class mywindow(QtWidgets.QMainWindow):
    '''Конструктор гловного окна'''
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Установить изображение с формулой в главном окне
        pixmap = QPixmap("img/img.jpg")
        self.ui.label_2.setPixmap(pixmap)

        # Подвязка кнопки "Решить" к методам класса главного окна
        self.ui.solve_button.clicked.connect(self.solve)

    '''Произвести рассчёт по формуле у данной задачи'''
    def solve(self):
        #Считать введённые пользователем данные
        n = self.ui.n_spinBox.value()
        m = self.ui.m_spinBox.value()

        # Проверить введенные данные
        if m > n:
            QtWidgets.QMessageBox.information(self, "Ошибка", "Значение m не должно быть больше значения n")
            return

        # Произвести вычисления по формуле
        result = 1 / Combinatoric.combinations_without_repeats(n, m)

        # Вывести результат в поле для ответа
        str_result = "{:01.12}".format(result)
        self.ui.result_lineEdit.setText(str_result)

if __name__ == '__main__': 
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    
    sys.exit(app.exec())