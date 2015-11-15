#include "strechtedlabel.h"
#include <QFont>
StrechtedLabel::StrechtedLabel(QWidget* parent) :
    QLabel(parent)
{
    setSizePolicy(QSizePolicy::Ignored, QSizePolicy::Ignored);
}

void StrechtedLabel::resizeEvent(QResizeEvent *)
{
    if( this->text().isEmpty() )
            return;

    QRect cRect = this->contentsRect();
    QFont font = this->font();


    int fontSize = 10;

    while( true )
    {
                QFont f(font);
                     f.setPixelSize( fontSize );
                QRect r = QFontMetrics(f).boundingRect( this->text() );
                if (r.height() <= 0.95*cRect.height() && r.width() <= 0.95*cRect.width() )
                      fontSize++;
                else
                      break;
    }

   font.setPixelSize(fontSize);
   this->setFont(font);
}

