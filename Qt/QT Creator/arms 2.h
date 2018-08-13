#ifndef ARMS_H
#define ARMS_H

#include <QMainWindow>

namespace Ui {
class ARMS;
}

class ARMS : public QMainWindow
{
    Q_OBJECT

public:
    explicit ARMS(QWidget *parent = 0);
    ~ARMS();

private:
    Ui::ARMS *ui;
};

#endif // ARMS_H
