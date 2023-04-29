#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : Download, edit thumbnail
@File        : thumbnail.py
@IDE         : PyCharm
@Date        : 29/4/2023 13:07
"""

import os
import threading
import PIL
from PIL import Image

import requests


def _download_thumbnail(data: dict) -> None:
    """
    Sumary:
        Download thumbnail
    Args:
        data (dict): Data of music
    Returns:
        None
    """
    # download thumbnail through requests and save to thumbnail folder
    r = requests.get(data["thumbnail"])
    with open(f"thumbnail/{data['id']}.jpg", "wb") as f:
        f.write(r.content)

    _edit_thumbnail(data)
    return None


def _edit_thumbnail(data: dict) -> None:
    """
    Sumary:
        Edit thumbnail to square. Height = Picture original height, Width = Height
    Args:
        data (dict): Data of music
    Returns:
        None
    """
    im = Image.open(f"thumbnail/{data['id']}.jpg")
    width, height = im.size
    if width > height:
        im = im.crop(((width-height)//2, 0, (width+height)//2, height))
    elif width < height:
        im = im.crop((0, (height-width)//2, width, (height+width)//2))
    im.thumbnail((height, height), PIL.Image.ANTIALIAS)
    im.save(f"thumbnail/{data['id']}.jpg")

    return None


def _thumbnail(data: dict) -> None:
    """
    Sumary:
        Download and edit thumbnail
    Args:
        data (dict): Data of music
    Returns:
        None
    """
    _download_thumbnail(data)
    return None