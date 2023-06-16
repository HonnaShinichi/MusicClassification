from music_module.music_split import m2ms
from music_module.music2array import mp3conversion
from music_module.music_mass import(
    random_vol_change,
    random_stretch_change,
    random_noise_add,
)
from pathlib import Path
import numpy as np
import glob
from sklearn.model_selection import train_test_split

music_path = Path('./music')

music_list = []
[music_list.append(music) for music in music_path.glob('**/*.mp3')]


X = [None]*len(music_list)
Y = [None]*len(music_list)
count = 0
for music in music_list:
    x = []
    name, music_vec = mp3conversion(music)
    vol_list = random_vol_change(music_vec)
    stretch_list = random_stretch_change(music_vec)
    noise_list = random_noise_add(music_vec)
    music_vec_list = vol_list + stretch_list + noise_list
    music_vec_list.append(music_vec)
    X[count] = music_vec_list
    Y[count] = name
    count +=1

