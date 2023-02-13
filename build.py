import shutil
import os

if os.path.exists('build'):
    shutil.rmtree('build')

os.makedirs('build/musicpy')
shutil.copyfile('LICENSE', 'build/LICENSE')
shutil.copyfile('README.md', 'build/README.md')
shutil.copyfile('musicpy/musicpy/__init__.py', 'build/musicpy/__init__.py')
shutil.copyfile('musicpy/musicpy/database.py', 'build/musicpy/database.py')
shutil.copyfile('musicpy/musicpy/structures.py', 'build/musicpy/structures.py')
shutil.copyfile('src/main.py', 'build/main.py')

with open('musicpy/musicpy/musicpy.py', 'r', encoding='utf-8') as file:
    data = file.read().replace('import mido_fix as mido', '')
    data = data[0:data.find('os.environ')] + data[data.find('def method_wrapper'):]
    with open('build/musicpy/musicpy.py', 'w', encoding='utf-8') as file:
        file.write(data)

with open('musicpy/musicpy/algorithms.py', 'r', encoding='utf-8') as file:
    data = file.read().replace('[chord_notes[k[0]:k[1]] for k in chord_inds]', 'chord_notes, chord_inds')
    with open('build/musicpy/algorithms.py', 'w', encoding='utf-8') as file:
        file.write(data)
