#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QFile>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    readFile();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::readFile()
{
    QFile file("file.txt"); // создаем объект класса QFile
    QByteArray data; // Создаем объект класса QByteArray, куда мы будем считывать данные
    if (!file.open(QIODevice::ReadOnly)) // Проверяем, возможно ли открыть наш файл для чтения
        return; // если это сделать невозможно, то завершаем функцию
    data = file.readAll(); //считываем все данные с файла в объект data
    ui->label->setText(QString(data)); // Выводим данные в консоль, предварительно создав строку из полученных данных
}
