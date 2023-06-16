import numpy as np
import random
import librosa


def random_vol_change(music:np.ndarray)->list:
    '音量を変えて10サンプルのリストを返す'
    vol_change_list = []
    for _ in range(10):
        vol_change_music = music * random.uniform(0.8, 1.2)
        vol_change_list.append(vol_change_music)
    return vol_change_list

def stretch(music:np.ndarray, rate:int=1)->np.ndarray:
    '音楽の速度を変える'
    input_length = len(music)
    music = librosa.effects.time_stretch(music, rate=rate)
    if len(music)>input_length:
        music = music[:input_length]
    else:
        music = np.pad(music, (0, max(0, input_length - len(music))), "constant")
    return music

def random_stretch_change(music:np.ndarray)->list:
    '速度を変えて10サンプルのリストを返す'
    stretch_change_list = []
    for _ in range(10):
        data_stretch = stretch(music, rate=random.uniform(0.5, 1.5)) #ランダムデータ伸縮
        stretch_change_list.append(data_stretch)
    return stretch_change_list

def random_noise_add(music:np.ndarray)->list:
    'ノイズを加えて10サンプルのリストを返す'
    noise_add_list = []
    wn = np.random.randn(*music.shape)
    for _ in range(10):
        music_wn = music + random.uniform(0.01, -0.01)*wn #ランダムにノイズを作成
        noise_add_list.append(music_wn)
    return noise_add_list

###
#インパルス応答(=響き)をランダム生成してサンプルを作るやつもあった方がいいかもしれないが
#だいぶ面倒なので一時保留
#自然音でなく音楽なのでまぁいける気もする
###