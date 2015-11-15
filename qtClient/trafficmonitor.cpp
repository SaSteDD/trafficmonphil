#include "trafficmonitor.h"
#include "ui_trafficmonitor.h"
#include <QDebug>

TrafficMonitor::TrafficMonitor(QWidget *parent) :
    QWidget(parent),
    isFullScreen(false),
    ui(new Ui::TrafficMonitor),
    blockSize(8)
{

    fullScreenShortcut= new QShortcut(QKeySequence("F11"),this);
    connect(fullScreenShortcut, SIGNAL(activated()), this, SLOT(toggleFullscreen()));

    ui->setupUi(this);

    tcpSocket = new QTcpSocket(this);
    tcpSocket->setReadBufferSize(this->blockSize);


    connect(tcpSocket, SIGNAL(readyRead()), this, SLOT(readTrafficData()));

    connect(tcpSocket,SIGNAL(connected()), this, SLOT(connected()));

    tcpSocket->connectToHost(
                QHostAddress("192.168.1.1"),
                9999
                );

}

TrafficMonitor::~TrafficMonitor()
{
    delete ui;
}

void TrafficMonitor::readTrafficData()
{
    //in.setVersion(QDataStream::Qt_4_0);

    if (tcpSocket->bytesAvailable() < blockSize)
            return;

    QDataStream in(tcpSocket);
    in.setByteOrder(QDataStream::BigEndian);//network byte order

    quint32 tx, rx;
    in >> rx >> tx;

    double rxMbps = convertToMbps(rx);
    double txMbps = convertToMbps(tx);

    ui->rxLabel->setText("Down: " + QString::number(rxMbps,'f',3).rightJustified(6,'0') + " Mbit/s");
    ui->txLabel->setText("Up  : " + QString::number(txMbps,'f',3).rightJustified(6,'0') + " Mbit/s");

}

void TrafficMonitor::connected()
{
    qDebug() << "Connected";
}

void TrafficMonitor::toggleFullscreen()
{
    isFullScreen = !isFullScreen;

    if(isFullScreen){
        this->showFullScreen();
    } else {
        this->showNormal();
    }
}

double TrafficMonitor::convertToMbps(quint32 Bps)
{
    return ((double) Bps * 8.0 / 1000000.0);
}
