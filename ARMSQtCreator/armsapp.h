#ifndef ARMSAPP_H
#define ARMSAPP_H

#include <QMainWindow>

namespace Ui {
class ARMSApp;
}

class ARMSApp : public QMainWindow
{
    Q_OBJECT

public:
    explicit ARMSApp(QWidget *parent = 0);
    ~ARMSApp();

private:
    Ui::ARMSApp *ui;
};

#endif // ARMSAPP_H
