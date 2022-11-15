#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_ex1Button_clicked();

    void on_ex2Button_2_clicked();

    void on_spinBox_valueChanged(int arg1);

    void on_ex31Button_clicked();

    void on_ex3Button_clicked();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
