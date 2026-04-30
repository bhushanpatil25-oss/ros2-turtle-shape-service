# ROS2 Turtle Shape Service

A ROS2 project where turtlesim draws shapes using a custom ROS2 service.

## Features

- Custom service interface using `DrawShape.srv`
- Draw square
- Draw circle
- Draw triangle
- Draw pentagon
- Draw hexagon

## Packages

### `shape_interface`
Contains the custom service definition:

```srv
string shape
---
bool success
string message
