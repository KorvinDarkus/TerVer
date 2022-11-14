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
        ui->outpt_2->setNum((p_ex2[0]*p_ex2[1]*(1-p_ex2[2])*(1-p_ex2[3])) + (p_ex2[0]*p_ex2[2]*(1-p_ex2[1])*(1-p_ex2[3]))+
                            (p_ex2[0]*p_ex2[3]*(1-p_ex2[1])*(1-p_ex2[2])) + (p_ex2[1]*p_ex2[2]*(1-p_ex2[0])*(1-p_ex2[3]))+
                            (p_ex2[1]*p_ex2[3]*(1-p_ex2[0])*(1-p_ex2[2])) + (p_ex2[2]*p_ex2[3]*(1-p_ex2[0])*(1-p_ex2[1])));
        break;
    case 3:
        ui->outpt_2->setNum(1-(1-p_ex2[0])*(1-p_ex2[1])*(1-p_ex2[2])*(1-p_ex2[3]));
        break;
    default:
        ui->outpt_2->setText("ERROR");

    }
}


void MainWindow::on_spinBox_valueChanged(int h)
{
    QDoubleSpinBox *inputs[]={ui->inpt1_e3,ui->inpt2_e3,ui->inpt3_e3,ui->inpt4_e3,ui->inpt5_e3,ui->inpt6_e3,ui->inpt7_e3,ui->inpt8_e3,ui->inpt9_e3,ui->inpt10_e3,ui->inpt11_e3,ui->inpt12_e3};
    QDoubleSpinBox *inputs2[]={ui->inpt21_e3,ui->inpt22_e3,ui->inpt23_e3,ui->inpt24_e3,ui->inpt25_e3,ui->inpt26_e3,ui->inpt27_e3,ui->inpt28_e3,ui->inpt29_e3,ui->inpt210_e3,ui->inpt211_e3,ui->inpt212_e3};

    for(int i = 0; i < h; i++)
    {
        inputs[i]->setEnabled(true);
        inputs2[i]->setEnabled(true);
    }
    for(int i = 11; i > h; i--)
    {
        inputs[i]->clear();
        inputs[i]->setEnabled(false);
        inputs2[i]->clear();
        inputs[i]->setEnabled(false);
    }
}
