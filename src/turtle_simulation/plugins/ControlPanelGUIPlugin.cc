#include <gz/gui/Application.hh>
#include <gz/gui/MainWindow.hh>
#include <gz/gui/Plugin.hh>
#include <gz/transport/Node.hh>
#include <gz/msgs/twist.pb.h>
#include <gz/plugin/Register.hh>
#include <QPushButton>
#include <QVBoxLayout>
#include <QWidget>
#include <QDockWidget>
class ControlPanelGUIPlugin : public gz::gui::Plugin
{
  Q_OBJECT

public:
  ControlPanelGUIPlugin(): gz::gui::Plugin()
  {
    

    // Create a layout
    QVBoxLayout *layout = new QVBoxLayout;

    // Add buttons
    QPushButton *forwardButton = new QPushButton("Forward");
    QPushButton *backwardButton = new QPushButton("Backward");
    QPushButton *leftButton = new QPushButton("Left");
    QPushButton *rightButton = new QPushButton("Right");
    QPushButton *stopButton = new QPushButton("Stop");

    layout->addWidget(forwardButton);
    layout->addWidget(backwardButton);
    layout->addWidget(leftButton);
    layout->addWidget(rightButton);
    layout->addWidget(stopButton);
    
    // Create a QWidget container for the layout
    QWidget *container = new QWidget();
    // Set the layout on the container
    container->setLayout(layout);
    this->setContent(container);

    
    // Gazebo transport node
    this->node = std::make_shared<gz::transport::Node>();

    // Connect button signals to methods
    connect(forwardButton, &QPushButton::clicked, this, &ControlPanelGUIPlugin::MoveForward);
    connect(backwardButton, &QPushButton::clicked, this, &ControlPanelGUIPlugin::MoveBackward);
    connect(leftButton, &QPushButton::clicked, this, &ControlPanelGUIPlugin::TurnLeft);
    connect(rightButton, &QPushButton::clicked, this, &ControlPanelGUIPlugin::TurnRight);
    connect(stopButton, &QPushButton::clicked, this, &ControlPanelGUIPlugin::Stop);
  }

private slots:
  void MoveForward()
  {
    PublishVelocity(1.0, 0.0);
  }

  void MoveBackward()
  {
    PublishVelocity(-1.0, 0.0);
  }

  void TurnLeft()
  {
    PublishVelocity(0.0, 1.0);
  }

  void TurnRight()
  {
    PublishVelocity(0.0, -1.0);
  }

  void Stop()
  {
    PublishVelocity(0.0, 0.0);
  }

private:
  void PublishVelocity(double linear, double angular)
  {
    gz::msgs::Twist msg;
    msg.mutable_linear()->set_x(linear);
    msg.mutable_angular()->set_z(angular);
    this->node->Request("/cmd_vel", msg);
  }

  std::shared_ptr<gz::transport::Node> node;
};

// Register the plugin
GZ_ADD_PLUGIN(ControlPanelGUIPlugin,
              gz::gui::Plugin)
