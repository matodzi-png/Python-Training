# demo_reader/multireader.py

import os

from demo_reader.compressed import bzipped,gzziped 
extension_map ={
    '.bz2':bzipped.operner,
    '.gz':gzipped.opener
}
class multiReader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension, open)
        self.file = filename
        self.f = open(filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()     

import gzip 
import sys

open =gzip.open

if __name__ == "__main__":
    f =gzip.open(
        sys.argv[1],
        mode='wt')
    f.write(''.join(sys.argv[2:]))
    f.close()    

