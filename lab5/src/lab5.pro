TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += \
        conveyor.cpp \
        logger.cpp \
        main.cpp \
        standardizer.cpp

HEADERS += \
    conveyor.h \
    logger.h \
    standardizer.h
