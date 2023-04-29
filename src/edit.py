#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : Edit music Metadata
@File        : edit.py
@IDE         : PyCharm
@Date        : 29/4/2023 12:59
"""


import os

import eyed3

from src.thumnail import _thumbnail

def _edit(id: str, data: dict) -> None:
    """
    Sumary:
        Edit music Metadata
    Args:
        id (str): ID of music
        data (dict): Data of music
    Returns:
        None
    """

    _thumbnail(data)

    try:
        audiofile = eyed3.load(f"music/{id}.mp3")
        audiofile.tag.artist = data["author"]
        audiofile.tag.title = data["title"]
        audiofile.tag.images.set(3, open(f"thumbnail/{id}.jpg", "rb").read(), "image/jpeg")
        audiofile.tag.save()
    except:
        # using another library to edit metadata
        os.system(f"ffmpeg -i music/{id}.mp3 -metadata title=\"{data['title']}\" -metadata artist=\"{data['author']}\" music/{id}.mp3")

    _rename(id, data)
    return None


def _rename(id: str, data: dict) -> None:
    """
    Sumary:
        Rename music
    Args:
        id (str): ID of music
        data (dict): Data of music
    Returns:
        None
    """
    if os.path.isfile(f"music/{id}.mp3"):
        counter = 1
        new_name = f"music/{data['title']}.mp3"
        while os.path.isfile(new_name):
            new_name = f"music/{data['title']} ({counter}).mp3"
            counter += 1

        os.rename(f"music/{id}.mp3", new_name)
    else:
        print(f"File 'music/{id}.mp3' not found")

    return None