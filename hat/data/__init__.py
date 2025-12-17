import importlib
from os import path as osp

import basicsr.data.data_util
import basicsr.utils
import basicsr.utils.misc

try:
    import basicsr.data.single_image_dataset
except ImportError:
    basicsr.data.single_image_dataset = None

# Monkeypatch scandir to ignore doc.md, which is not an image
_original_scandir = basicsr.utils.scandir

def filtered_scandir(dir_path, suffix=None, recursive=False, full_path=False):
    for path in _original_scandir(dir_path, suffix, recursive, full_path):
        if osp.basename(path) != 'doc.md':
            yield path

basicsr.utils.scandir = filtered_scandir
basicsr.utils.misc.scandir = filtered_scandir
basicsr.data.data_util.scandir = filtered_scandir
if basicsr.data.single_image_dataset and hasattr(basicsr.data.single_image_dataset, 'scandir'):
    basicsr.data.single_image_dataset.scandir = filtered_scandir

# Use the filtered scandir for the rest of the file
scandir = filtered_scandir

# automatically scan and import dataset modules for registry
# scan all the files that end with '_dataset.py' under the data folder
data_folder = osp.dirname(osp.abspath(__file__))
dataset_filenames = [osp.splitext(osp.basename(v))[0] for v in scandir(data_folder) if v.endswith('_dataset.py')]
# import all the dataset modules
_dataset_modules = [importlib.import_module(f'hat.data.{file_name}') for file_name in dataset_filenames]
