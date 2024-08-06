#include "mainwindow.h"
#include <QtWidgets>
#include "counter.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    //Counter
    hours = new Counter(this,3600);
    minutes = new Counter(this,60);
    seconds = new Counter(this,1);

    //Labels
    QLabel *hoursLabel = new QLabel(tr("Hours"));
    QLabel *minutesLabel = new QLabel(tr("Minutes"));
    QLabel *secondsLabel = new QLabel(tr("Seconds"));
    QHBoxLayout *labels = new QHBoxLayout;
    labels->addWidget(hoursLabel);
    labels->addWidget(minutesLabel);
    labels->addWidget(secondsLabel);
    //labels->SetMaximumSize;

    //Screen
    hourScreen = new QLCDNumber(this);
    //hourScreen->display(1);
    minuteScreen = new QLCDNumber(this);
    //minuteScreen->display(1);
    secondScreen = new QLCDNumber(this);
    connect(hours,SIGNAL(countChanges(int)), this, SLOT(hourScreenUpdate(int)));
    connect(minutes,SIGNAL(countChanges(int)), this, SLOT(minuteScreenUpdate(int)));
    connect(seconds,SIGNAL(countChanges(int)), this, SLOT(secondScreenUpdate(int)) );
    //QLabel *hours = new QLabel(tr("Hi"));
    QHBoxLayout *screen = new QHBoxLayout;
    screen->addWidget(hourScreen);
    screen->addWidget(minuteScreen);
    screen->addWidget(secondScreen);

    //Buttons
    startButton = new QPushButton("Start", this);
    connect(startButton, SIGNAL (released()), this, SLOT (start()));
    stopButton = new QPushButton("Stop", this);
    connect(stopButton, SIGNAL (released()), this, SLOT (terminate()));
    QHBoxLayout *buttons = new QHBoxLayout;
    buttons->addWidget(startButton);
    buttons->addWidget(stopButton);

    QGridLayout *mainLayout = new QGridLayout;
    mainLayout->addLayout(labels,0,0,1,1);
    mainLayout->addLayout(screen,1,0,1,1);
    mainLayout->addLayout(buttons,2,0,1,1);
    //mainLayout->addWidget(button);
    QWidget *widget = new QWidget();
    widget->setLayout(mainLayout);
    setCentralWidget(widget);

}

void MainWindow::start(){
    hours->start();
    minutes->start();
    seconds->start();
}
void MainWindow::terminate(){
    hours->terminate();
    minutes->terminate();
    seconds->terminate();
}
void MainWindow::hourScreenUpdate(int i)
{hourScreen->display(i);}
void MainWindow::minuteScreenUpdate(int i)
{minuteScreen->display(i);}
void MainWindow::secondScreenUpdate(int i)
{secondScreen->display(i);}
