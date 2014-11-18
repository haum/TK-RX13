#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# motors.py
#
# Copyright © 2014 Mathieu Gaborit (matael) <mathieu@matael.org>
#
#
# Distributed under WTFPL terms
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.
#

"""

"""

from RPIO import PWM
from settings import *

def set_motor_speed(dma_buf, pin, speed):
    pulse_width = 650 + speed/100*(1000-650)
    PWM.add_channel_pulse(dma_buf, pin, 0, pulse_width)

def left_speed(speed):
    if speed <0:
        PWM.clear_channel_gpio(DMA_LEFT, LEFT_FORWARD)
        set_motor_speed(DMA_LEFT, LEFT_BACKWARD, -speed)
    else:
        PWM.clear_channel_gpio(DMA_LEFT, LEFT_BACKWARD)
        set_motor_speed(DMA_LEFT, LEFT_FORWARD, speed)

def right_speed(speed):
    if speed <0:
        PWM.clear_channel_gpio(DMA_RIGHT, RIGHT_FORWARD)
        set_motor_speed(DMA_RIGHT, RIGHT_BACKWARD, -speed)
    else:
        PWM.clear_channel_gpio(DMA_RIGHT, RIGHT_BACKWARD)
        set_motor_speed(DMA_RIGHT, RIGHT_FORWARD, speed)
