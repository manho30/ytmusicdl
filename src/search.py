#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : Search music list
@File        : search.py
@IDE         : PyCharm
@Date        : 29/4/2023 12:13
"""


import ytmusicapi

from src.helper import human_duration_to_machine_duration, machine_duration_to_human_duration

ytmusic = ytmusicapi.YTMusic()

def _search(query: str, limit: int, offset: int) -> list:
    """
    Sumary:
        Search music list
    Args:
        query (str): Search query
        limit (int): Limit of search result
        offset (int): Offset of search result
    Returns:
        list: List of search result
    """
    music = ytmusic.search(query, filter="songs", limit=limit*(offset+1))
    return music[offset*limit:offset*limit+limit]

def search(query: str, limit: int, offset: int) -> str:
    """
    Sumary:
        Search music list
    Args:
        query (str): Search query
        limit (int): Limit of search result
        offset (int): Offset of search result
    Returns:
        str: JSON of search result
    """
    music = _search(query, limit, offset)
    result = []
    for i in music:
        result.append({
            "id": i["videoId"],
            "title": i["title"],
            'duration': human_duration_to_machine_duration(i["duration"]),
            "author": i["artists"][0]["name"],
            "thumbnail": f'https://img.youtube.com/vi/{i["videoId"]}/maxresdefault.jpg'
        })
    return result
if __name__ == "__main__":
    music = search("seventeen", 10, 0)
    print(music)