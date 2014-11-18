#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# setup.py
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

def setup():
    PWM.setup()
    PWM.init_channel(DMA_LEFT,10000)
    PWM.init_channel(DMA_RIGHT,10000)
    PWM.add_channel_pulse(DMA_LEFT, LEFT_FORWARD, 0, 0)
    PWM.add_channel_pulse(DMA_LEFT, LEFT_BACKWARD, 0, 0)
    PWM.add_channel_pulse(DMA_RIGHT, RIGHT_FORWARD, 0, 0)
    PWM.add_channel_pulse(DMA_RIGHT, RIGHT_BACKWARD, 0, 0)




