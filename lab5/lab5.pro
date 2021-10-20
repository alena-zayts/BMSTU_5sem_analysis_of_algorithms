TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += \
        conveyor.cpp \
        logger.cpp \
        main.cpp \
        slau_solver.cpp

HEADERS += \
    conveyor.h \
    logger.h \
    slau_solver.h
