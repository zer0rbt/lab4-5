from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QPlainTextEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from typing import Type
from your_genetic_algorithm_module import GeneticAlgorithm, Gene

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Загрузка UI из XML
        self.setup_ui()

        # Создание экземпляра GeneticAlgorithm
        self.genetic_algorithm = None

        # Подключение функций к кнопкам
        self.pushButton_3.clicked.connect(self.run_genetic_algorithm)
        self.pushButton_2.clicked.connect(self.previous_iteration)
        self.pushButton.clicked.connect(self.next_iteration)
        self.Set1iterationCount.clicked.connect(lambda: self.set_iteration_count(1))
        self.Set10iterationCount.clicked.connect(lambda: self.set_iteration_count(10))
        self.Set100iterationCount.clicked.connect(lambda: self.set_iteration_count(100))
        self.Set1000iterationCount.clicked.connect(lambda: self.set_iteration_count(1000))

    def setup_ui(self):
        # Загрузка UI из XML (вставьте сюда ваш XML-код)
        # ...

    def run_genetic_algorithm(self):
        # Получение значений параметров из UI
        gene_amount = int(self.GeneAmountQLE.text())
        mutation_percent = int(self.MutationPercentQLE.text())
        bounds = (float(self.bound0QLE.text()), float(self.bound1QLE.text()))
        func = self.funcQLE.text()
        iteration_count = int(self.IterationCount.text())

        # Создание экземпляра GeneticAlgorithm
        gene_class = Type[Gene]  # Укажите здесь класс вашего гена
        self.genetic_algorithm = GeneticAlgorithm(gene_class, gene_amount, mutation_percent, bounds, func, iteration_count)

        # Расчет и вывод результатов
        best_gene = self.genetic_algorithm.solve()
        self.BestGene.setPlainText(f"Best Gene: {best_gene}")

        # Отображение таблицы генов
        self.show_genes_table()

    def show_genes_table(self):
        # Получение текущих генов из алгоритма
        current_genes = self.genetic_algorithm.get_current_genes()

        # Очистка таблицы
        self.tableWidget.clear()

        # Заголовки столбцов
        headers = ['X', 'Y']
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)

        # Заполнение таблицы данными
        self.tableWidget.setRowCount(len(current_genes))
        for row, gene in enumerate(current_genes):
            x_item = QTableWidgetItem(str(gene.x))
            y_item = QTableWidgetItem(str(gene.y))
            self.tableWidget.setItem(row, 0, x_item)
            self.tableWidget.setItem(row, 1, y_item)

    def set_iteration_count(self, count):
        # Установка значения количества итераций
        self.IterationCount.setText(str(count))

    def previous_iteration(self):
        # Переход к предыдущей итерации
        if self.genetic_algorithm:
            self.genetic_algorithm.previous_iteration()
            self.show_genes_table()

    def next_iteration(self):
        # Переход к следующей итерации
        if self.genetic_algorithm:
            self.genetic_algorithm.next_iteration()
            self.show_genes_table()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
