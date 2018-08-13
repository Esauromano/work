#include "armsapp.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    ARMSApp w;
    w.show();

    return a.exec();
}
