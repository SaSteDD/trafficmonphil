#-------------------------------------------------
#
# Project created by QtCreator 2015-11-14T14:49:19
#
#-------------------------------------------------

QT       += core gui network
QMAKE_CXXFLAGS += -std=c++0x

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = qtClient
TEMPLATE = app


SOURCES += main.cpp\
        trafficmonitor.cpp \
    strechtedlabel.cpp

HEADERS  += trafficmonitor.h \
    strechtedlabel.h

FORMS    += trafficmonitor.ui
