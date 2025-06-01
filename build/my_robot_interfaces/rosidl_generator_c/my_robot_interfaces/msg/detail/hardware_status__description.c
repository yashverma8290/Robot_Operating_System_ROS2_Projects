// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from my_robot_interfaces:msg/HardwareStatus.idl
// generated code does not contain a copyright notice

#include "my_robot_interfaces/msg/detail/hardware_status__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_my_robot_interfaces
const rosidl_type_hash_t *
my_robot_interfaces__msg__HardwareStatus__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x12, 0x57, 0xbb, 0x04, 0xd2, 0x62, 0x06, 0xb2,
      0x41, 0x04, 0x04, 0x0d, 0xc9, 0x73, 0x62, 0x77,
      0x11, 0x76, 0x7c, 0x0a, 0xab, 0x00, 0xa2, 0x99,
      0x69, 0x03, 0x96, 0x3d, 0xc8, 0x8d, 0xe5, 0x99,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char my_robot_interfaces__msg__HardwareStatus__TYPE_NAME[] = "my_robot_interfaces/msg/HardwareStatus";

// Define type names, field names, and default values
static char my_robot_interfaces__msg__HardwareStatus__FIELD_NAME__temprature[] = "temprature";
static char my_robot_interfaces__msg__HardwareStatus__FIELD_NAME__are_motors_ready[] = "are_motors_ready";
static char my_robot_interfaces__msg__HardwareStatus__FIELD_NAME__dubug_message[] = "dubug_message";

static rosidl_runtime_c__type_description__Field my_robot_interfaces__msg__HardwareStatus__FIELDS[] = {
  {
    {my_robot_interfaces__msg__HardwareStatus__FIELD_NAME__temprature, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_interfaces__msg__HardwareStatus__FIELD_NAME__are_motors_ready, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_interfaces__msg__HardwareStatus__FIELD_NAME__dubug_message, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
my_robot_interfaces__msg__HardwareStatus__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {my_robot_interfaces__msg__HardwareStatus__TYPE_NAME, 38, 38},
      {my_robot_interfaces__msg__HardwareStatus__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float64 temprature\n"
  "bool are_motors_ready\n"
  "string dubug_message\n"
  "\n"
  "\n"
  "\n"
  "# This message file defines the hardware status information.\n"
  "\n"
  "# 1. We create this message file (HardwareStatus.msg) to define the hardware data structure.\n"
  "# 2. We add this message file to CMakeLists.txt so ROS2 knows to compile it.\n"
  "# 3. Dependencies are listed in package.xml to provide necessary build and runtime tools.\n"
  "# 4. When we run colcon build, ROS2 auto-generates C++ and Python code from this message.\n"
  "# 5. This generated code is used in ROS2 nodes for publishing and subscribing hardware status messages.";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
my_robot_interfaces__msg__HardwareStatus__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {my_robot_interfaces__msg__HardwareStatus__TYPE_NAME, 38, 38},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 581, 581},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
my_robot_interfaces__msg__HardwareStatus__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *my_robot_interfaces__msg__HardwareStatus__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
