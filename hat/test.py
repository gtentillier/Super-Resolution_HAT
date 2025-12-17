# flake8: noqa
import os.path as osp
import sys
from datetime import datetime

from basicsr.test import test_pipeline

script_dir = osp.dirname( __file__ )
mymodule_dir = osp.join( script_dir, '..')
sys.path.append( mymodule_dir )


# following imports are necessary
import hat.archs
import hat.data
import hat.models

if __name__ == '__main__':
    root_path = osp.abspath(osp.join(__file__, osp.pardir, osp.pardir))
    test_pipeline(root_path)
    print(f'Finish at: {datetime.now():%Y-%m-%d %H:%M:%S}')
