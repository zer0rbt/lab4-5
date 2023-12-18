from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from generated_ui import Ui_MainWindow
from typing import List
from main import GeneticAlgorithm, Gene

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Инициализация генетического алгоритма
        self.genetic_algorithm = None

        # Подключение кнопок к функциям
        self.Set1iterationCount.clicked.connect(lambda: self.set_iteration_count(1))
        self.Set10iterationCount.clicked.connect(lambda: self.set_iteration_count(10))
        self.Set100iterationCount.clicked.connect(lambda: self.set_iteration_count(100))
        self.Set1000iterationCount.clicked.connect(lambda: self.set_iteration_count(1000))
        self.pushButton_3.clicked.connect(self.run_genetic_algorithm)
        self.pushButton_2.clicked.connect(self.previous_iteration)
        self.pushButton.clicked.connect(self.next_iteration)

        # Инициализация таблицы
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['X', 'Y', 'F(X,Y)'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Задание базовых параметров
        self.IterationCount.setText(str(50))
        self.GeneAmountQLE.setText(str(12))
        self.funcQLE.setText("100 * (y - x ** 2) ** 2 + (1 - x)**2")
        self.bound0QLE.setText("-10")
        self.bound1QLE.setText("10")
        self.MutationPercentQLE.setText("20")

        self.genetic_algorithm: GeneticAlgorithm
        self.table_iteration = -1

    def set_iteration_count(self, count: int):
        self.IterationCount.setText(str(count))

    def set_table_iteration_count(self):
        self.lineEdit.setText(str(self.genetic_algorithm.generations + self.table_iteration + 1))

    def run_genetic_algorithm(self):
        # Получение значений из интерфейса
        func = self.funcQLE.text()
        gene_amount = int(self.GeneAmountQLE.text())
        mutation_percent = float(self.MutationPercentQLE.text())
        bounds = (float(self.bound0QLE.text()), float(self.bound1QLE.text()))
        iteration_count = int(self.IterationCount.text())

        # Инициализация генетического алгоритма
        self.genetic_algorithm = GeneticAlgorithm(GeneClass=Gene, genes_amount=gene_amount, mutation_p=mutation_percent, bounds=bounds, func=func, generations=iteration_count, crossover_points=2)

        # Запуск генетического алгоритма
        print(self.genetic_algorithm.solve())

        # Отображение результатов
        self.show_results()

    def display_genes_in_table(self):
        self.set_table_iteration_count()
        contents = self.genetic_algorithm.iterations[self.table_iteration]
        contents = sorted(contents, key=float)
        self.tableWidget.setRowCount(0)
        for i, gene in enumerate(contents):
            value = float(gene)
            position = gene.decoded()

            # Добавляем новую строку в таблицу
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

            # Заполняем ячейки таблицы  # Значение
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(position[0])))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(position[1])))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(str(value)))
    def show_results(self):
        self.table_iteration = -1
        self.display_genes_in_table()

    def previous_iteration(self):
        if self.table_iteration + self.genetic_algorithm.generations >= 0:
            self.table_iteration -= 1
            self.display_genes_in_table()

    def next_iteration(self):
        if self.table_iteration < -1:
            self.table_iteration += 1
            self.display_genes_in_table()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
