#ifndef TRAFFICMONITOR_H
#define TRAFFICMONITOR_H

#include <QWidget>
#include <QTcpSocket>
#include <QNetworkSession>
#include <QShortcut>

namespace Ui {
class TrafficMonitor;
}

class TrafficMonitor : public QWidget
{
    Q_OBJECT

public:
    explicit TrafficMonitor(QWidget *parent = 0);
    ~TrafficMonitor();

private slots:
    void readTrafficData();
    void connected();
    void toggleFullscreen();

private:
    double convertToMbps(quint32 Bps);
    bool isFullScreen;

    Ui::TrafficMonitor *ui;
    QShortcut * fullScreenShortcut;

    QTcpSocket *tcpSocket;
    quint16 blockSize;


};

#endif // TRAFFICMONITOR_H
