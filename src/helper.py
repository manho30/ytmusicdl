#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : Helper function
@File        : helper.py
@IDE         : PyCharm
@Date        : 29/4/2023 12:46
"""


def human_duration_to_machine_duration(duration: str) -> str:
    """
    Sumary:
        Convert human-readable duration to machine-readable duration
    Args:
        duration (str): Human-readable duration (e.g. 3:30)
    Returns:
        str: Machine-readable duration (e.g. 210)
    """
    duration = duration.split(":")
    duration = int(duration[0])*60+int(duration[1])
    return duration


def machine_duration_to_human_duration(duration: str) -> str:
    """
    Sumary:
        Convert machine-readable duration to human-readable duration
    Args:
        duration (str): Machine-readable duration (e.g. 210)
    Returns:
        str: Human-readable duration (e.g. 3:30)
    """
    duration = int(duration)
    duration = f"{duration//60}:{duration%60}"
    return duration
