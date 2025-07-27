// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_interfaces:msg/HardwareStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "my_robot_interfaces/msg/hardware_status.hpp"


#ifndef MY_ROBOT_INTERFACES__MSG__DETAIL__HARDWARE_STATUS__BUILDER_HPP_
#define MY_ROBOT_INTERFACES__MSG__DETAIL__HARDWARE_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_robot_interfaces/msg/detail/hardware_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_robot_interfaces
{

namespace msg
{

namespace builder
{

class Init_HardwareStatus_dubug_message
{
public:
  explicit Init_HardwareStatus_dubug_message(::my_robot_interfaces::msg::HardwareStatus & msg)
  : msg_(msg)
  {}
  ::my_robot_interfaces::msg::HardwareStatus dubug_message(::my_robot_interfaces::msg::HardwareStatus::_dubug_message_type arg)
  {
    msg_.dubug_message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::msg::HardwareStatus msg_;
};

class Init_HardwareStatus_are_motors_ready
{
public:
  explicit Init_HardwareStatus_are_motors_ready(::my_robot_interfaces::msg::HardwareStatus & msg)
  : msg_(msg)
  {}
  Init_HardwareStatus_dubug_message are_motors_ready(::my_robot_interfaces::msg::HardwareStatus::_are_motors_ready_type arg)
  {
    msg_.are_motors_ready = std::move(arg);
    return Init_HardwareStatus_dubug_message(msg_);
  }

private:
  ::my_robot_interfaces::msg::HardwareStatus msg_;
};

class Init_HardwareStatus_temprature
{
public:
  Init_HardwareStatus_temprature()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HardwareStatus_are_motors_ready temprature(::my_robot_interfaces::msg::HardwareStatus::_temprature_type arg)
  {
    msg_.temprature = std::move(arg);
    return Init_HardwareStatus_are_motors_ready(msg_);
  }

private:
  ::my_robot_interfaces::msg::HardwareStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::msg::HardwareStatus>()
{
  return my_robot_interfaces::msg::builder::Init_HardwareStatus_temprature();
}

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__MSG__DETAIL__HARDWARE_STATUS__BUILDER_HPP_
