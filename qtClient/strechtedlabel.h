#ifndef STRECHTEDLABEL_H
#define STRECHTEDLABEL_H

#include <QLabel>

class StrechtedLabel : public QLabel
{
public:
    StrechtedLabel(QWidget* parent = 0);

    // QWidget interface
protected:
    void resizeEvent(QResizeEvent *) override;
};

#endif // STRECHTEDLABEL_H
