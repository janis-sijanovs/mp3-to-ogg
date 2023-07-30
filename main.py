import os
from pydub import AudioSegment
from glob import glob

# directory containing the mp3 files
source_dir = './mp3s'

# directory to save the ogg files
target_dir = './oggs'

# get a list of mp3 files in source_dir
mp3_files = glob(os.path.join(source_dir, '*.mp3'))

for i, mp3_file in enumerate(mp3_files):
    # read mp3 file
    audio = AudioSegment.from_mp3(mp3_file)
    
    # convert stereo to mono
    audio = audio.set_channels(1)
    
    # export as ogg
    audio.export(os.path.join(target_dir, f'healing_{i}.ogg'), format='ogg')
