#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_ex1Button_clicked()
{
    double p[6] = {1 - ui->inpt1->value(), 1 - ui->inpt2->value(), 1 - ui->inpt3->value(), 1 - ui->inpt4->value(), 1 - ui->inpt5->value(), 1 - ui->inpt6->value()};
    ui->outpt->setNum( 1 - (p[0]*(p[1]*(p[2] + p[3] - p[2]*p[3]) + p[4]*p[5] - p[1]*p[4]*p[5]*(p[2] + p[3] - p[2]*p[3])))) ;

};
