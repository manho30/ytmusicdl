#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : Treeify the playlist
@File        : treeify.py
@IDE         : PyCharm
@Date        : 29/4/2023 14:17
"""

def treeify_songs(songs, limit: int, offset: int):
    tree = "I found the following songs for you.\n"
    for song, i in zip(songs, range(len(songs))):
        # if is last song
        if songs.index(song) == len(songs) - 1:
            title = song['title']
            song_tree  = f"{i} └─ {title}\n"
            song_tree += f"    ├─ id: {song['id']}\n"
            song_tree += f"    ├─ duration: {song['duration']}\n"
            song_tree += f"    └─ author: {song['author']}\n"
            tree += song_tree
        else:
            title = song['title']
            song_tree  = f"{i} ├─ {title}\n"
            song_tree += f"│   ├─ id: {song['id']}\n"
            song_tree += f"│   ├─ duration: {song['duration']}\n"
            song_tree += f"│   └─ author: {song['author']}\n"
            tree += song_tree
    return tree