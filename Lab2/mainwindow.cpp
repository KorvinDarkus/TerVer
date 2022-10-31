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
    double p_ex1[6] = {1 - ui->inpt1->value(), 1 - ui->inpt2->value(), 1 - ui->inpt3->value(), 1 - ui->inpt4->value(), 1 - ui->inpt5->value(), 1 - ui->inpt6->value()};
    ui->outpt->setNum( 1 - (p_ex1[0]*(p_ex1[1]*(p_ex1[2] + p_ex1[3] - p_ex1[2]*p_ex1[3]) + p_ex1[4]*p_ex1[5] - p_ex1[1]*p_ex1[4]*p_ex1[5]*(p_ex1[2] + p_ex1[3] - p_ex1[2]*p_ex1[3])))) ;

};


void MainWindow::on_ex2Button_2_clicked()
{
    double p_ex2[4] = {1 - ui->inpt1_2->value(), 1 - ui->inpt2_2->value(), 1 - ui->inpt3_2->value(), 1 - ui->inpt4_2->value()};

    switch (ui->tabWidget_2->currentIndex())
    {
    case 0:
        ui->outpt_2->setNum(p_ex2[0]*(1-p_ex2[1])*(1-p_ex2[2])*(1-p_ex2[3])+p_ex2[1]*(1-p_ex2[0])*(1-p_ex2[2])*(1-p_ex2[3])+p_ex2[2]*(1-p_ex2[0])*(1-p_ex2[1])*(1-p_ex2[3])+p_ex2[3]*(1-p_ex2[0])*(1-p_ex2[1])*(1-p_ex2[2]));
        break;
    case 1:
        ui->outpt_2->setNum(p_ex2[2]*(1-p_ex2[0])*(1-p_ex2[1])*(1-p_ex2[3]));
        break;
    case 2:
        ui->outpt->setNum((p_ex2[0]*p_ex2[1]*(1-p_ex2[2])*(1-p_ex2[3]))+(p_ex2[0]*p_ex2[2]*(1-p_ex2[1])*(1-p_ex2[3]))+
                            (p_ex2[0]*p_ex2[3]*(1-p_ex2[1])*(1-p_ex2[2]))+(p_ex2[1]*p_ex2[2]*(1-p_ex2[0])*(1-p_ex2[3]))+
                            (p_ex2[1]*p_ex2[3]*(1-p_ex2[0])*(1-p_ex2[2]))+(p_ex2[2]*p_ex2[3]*(1-p_ex2[0])*(1-p_ex2[1])));
        break;
    case 3:
        //ui->outpt_2->setNum();
        break;
    default:
        ui->outpt_2->setText("ERROR");

    }
}

