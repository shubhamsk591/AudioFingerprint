from pydub import AudioSegment
import os

def resample(file_path,file):
    song = AudioSegment.from_mp3(file_path)

    resampled_song = song.set_frame_rate(44100)

    resampled_song.export(os.path.splitext("data/t/"+file)[0] + '_resampled.mp3', format='mp3')

song_files = os.listdir('data/')
for file in song_files:
    file_name="data/"+file
    resample(file_name,file)
