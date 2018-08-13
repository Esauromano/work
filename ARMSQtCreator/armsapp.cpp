#include "armsapp.h"
#include "ui_armsapp.h"

ARMSApp::ARMSApp(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::ARMSApp)
{
    ui->setupUi(this);
}

ARMSApp::~ARMSApp()
{
    delete ui;
}
