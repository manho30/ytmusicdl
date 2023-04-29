#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : Download music
@File        : download.py
@IDE         : PyCharm
@Date        : 29/4/2023 12:57
"""

import time

import threading
import yt_dlp

from src.edit import _edit

def _download(id: str, data: dict) -> None:
    """
    Sumary:
        Download music and edit metadata
    Args:
        id (str): ID of music
        data (dict): Data of music
    Returns:
        None
    """
    ydl_opts = {
        'outtmpl': f'music/{id}.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3'
        }],
        'socket_timeout': 10,
        'ignoreerrors': True,
        'nocheckcertificate': True,
        'quiet': True,
    }

    def download_and_edit():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            start_time = time.time()
            print('Download start at', time.strftime('%H:%M:%S', time.localtime()))
            ydl.download([f'https://www.youtube.com/watch?v={id}'])
            print('Download end at', time.strftime('%H:%M:%S', time.localtime()))
            print('Time usage:', time.strftime('%H:%M:%S', time.gmtime(time.time() - start_time)))
            _edit(id, data)
    t = threading.Thread(target=download_and_edit)
    t.start()


def download(id: str, data: dict) -> None:
    """
    Sumary:
        Download music and edit metadata
    Args:
        id (str): ID of music
        data (dict): Data of music
    Returns:
        None
    """
    _download(id, data)
    return None