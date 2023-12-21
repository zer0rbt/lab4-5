from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from main import Unit, Swarm
from generated_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Инициализация генетического алгоритма
        self.swarm = None

        # Подключение кнопок к функциям
        self.Set1iterationCount.clicked.connect(lambda: self.set_iteration_count(1))
        self.Set10iterationCount.clicked.connect(lambda: self.set_iteration_count(10))
        self.Set100iterationCount.clicked.connect(lambda: self.set_iteration_count(100))
        self.Set1000iterationCount.clicked.connect(lambda: self.set_iteration_count(1000))
        self.pushButton_3.clicked.connect(self.run_swarm_algorithm)
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
        self.GlobalMinQLE.setText("1")
        self.LocalMinQLE.setText("5")
        self.swarm: Swarm
        self.table_iteration = -1

    def set_iteration_count(self, count: int):
        self.IterationCount.setText(str(count))

    def set_table_iteration_count(self):
        self.lineEdit.setText(str(self.swarm.generations + self.table_iteration + 1))

    def run_swarm_algorithm(self):
        # Получение значений из интерфейса
        func = self.funcQLE.text()
        unit_amount = int(self.GeneAmountQLE.text())
        local_best_weight = float(self.LocalMinQLE.text())
        global_best_weight = float(self.GlobalMinQLE.text())
        bounds = (float(self.bound0QLE.text()), float(self.bound1QLE.text()))
        iteration_count = int(self.IterationCount.text())

        # Инициализация алгоритма рой частиц
        self.swarm = Swarm(UnitClass=Unit, units_amount=unit_amount, global_best_weight=global_best_weight,
                           local_best_weight=local_best_weight, bounds=bounds, func=func, generations=iteration_count)

        # Запуск алгоритма
        print(self.swarm.solve(num_iterations=iteration_count))

        # Отображение результатов
        self.show_results()

    def display_units_in_table(self):
        self.set_table_iteration_count()
        contents = self.swarm.iterations[self.table_iteration]
        contents = sorted(contents, key=float)
        self.tableWidget.setRowCount(0)
        for i, gene in enumerate(contents):
            value = float(gene)
            position = gene.pos

            # Добавляем новую строку в таблицу
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

            # Заполняем ячейки таблицы  # Значение
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(position[0])))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(position[1])))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(str(value)))

    def display_best_gene(self):
        best_gene = min(self.swarm.iterations[-1], key=float)
        result_text = f"X: {best_gene.pos[0]}, Y: {best_gene.pos[1]}, F(X, Y): {float(best_gene)}"
        self.BestGene.setPlainText(result_text)

    def show_results(self):
        self.table_iteration = -1
        self.display_units_in_table()
        self.display_best_gene()

    def previous_iteration(self):
        if self.table_iteration + self.swarm.generations >= 0:
            self.table_iteration -= 1
            self.display_units_in_table()

    def next_iteration(self):
        if self.table_iteration < -1:
            self.table_iteration += 1
            self.display_units_in_table()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
