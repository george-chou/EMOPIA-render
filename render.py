import os
import zipfile
import argparse
from midi2audio import FluidSynth

parser = argparse.ArgumentParser(description='soundfont')
parser.add_argument(
    '--sf', type=str, default='./sound_font/J800 Piano.sf2', help='Select a sound font.')
args = parser.parse_args()


def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')


def render(midi_dir, font):
    fs = FluidSynth(sound_font=font)
    for _, _, filenames in os.walk(midi_dir):
        for filename in filenames:
            input = midi_dir + '/' + filename
            output = audio_dir + '/' + filename[:-3] + 'wav'
            print(input, output)
            fs.midi_to_audio(input, output)


def create_dirs(midi_zip, midi_dir, audio_dir):
    if(not os.path.exists(midi_dir)):
        unzip_file(midi_zip, './')

    if not os.path.exists(audio_dir):
        os.mkdir(audio_dir)


if __name__ == "__main__":

    midi_zip = './midis.zip'
    midi_dir = './midis'
    sound_font = args.sf
    audio_dir = './audios(' + sound_font.split('/')[-1][:-4] + ')'

    create_dirs(midi_zip, midi_dir, audio_dir)
    render(midi_dir, sound_font)
