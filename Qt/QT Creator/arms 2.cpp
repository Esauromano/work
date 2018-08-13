#include "arms.h"
#include "ui_arms.h"

ARMS::ARMS(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::ARMS)
{
    ui->setupUi(this);
}

ARMS::~ARMS()
{
    delete ui;
}
