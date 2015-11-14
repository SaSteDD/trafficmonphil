#ifndef TRAFFICMONITOR_H
#define TRAFFICMONITOR_H

#include <QWidget>
#include <QTcpSocket>
#include <QNetworkSession>

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

private:
    double convertToMbps(quint32 Bps);

    Ui::TrafficMonitor *ui;

    QTcpSocket *tcpSocket;
    quint16 blockSize;

};

#endif // TRAFFICMONITOR_H
