import librosa
from pydub import AudioSegment


def m2ms(music_file_mp3):
    # 音声ファイルを読み込む
    audio_data, sr = librosa.load(music_file_mp3)

    # オンセットを検出する
    onsets = librosa.onset.onset_detect(audio_data, sr=sr)

    # オンセット位置から音を区切る
    segments = librosa.effects.split(audio_data, onsets)

    # 分割された音声をmp3に変換し、リストに格納する
    audio_list = []
    for i, segment in enumerate(segments):
        start, end = segment
        segment_data = audio_data[start:end]
    
        # データを-1から1の範囲に正規化する
        normalized_data = librosa.util.normalize(segment_data)
    
        # 正規化されたデータをオーディオセグメントに変換する
        audio_segment = AudioSegment(normalized_data.tobytes(), frame_rate=sr, sample_width=normalized_data.dtype.itemsize, channels=1)
    
        # オーディオセグメントをmp3にエンコードする
        mp3_data = audio_segment.export(format='mp3').read()
    
        # mp3データをリストに追加する
        audio_list.append(mp3_data)
    
    return audio_list