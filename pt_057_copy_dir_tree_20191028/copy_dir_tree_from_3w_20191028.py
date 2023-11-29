# from: https://stackoverflow.com/questions/15663695/shutil-copytree-without-files

import os

def create_empty_dirtree(srcdir, dstdir, onerror=None):
    srcdir = os.path.abspath(srcdir)
    srcdir_prefix = len(srcdir) + len(os.path.sep)
    os.makedirs(dstdir)
    for root, dirs, files in os.walk(srcdir, onerror=onerror):
        for dirname in dirs:
            dirpath = os.path.join(dstdir, root[srcdir_prefix:], dirname)
            try:
                os.mkdir(dirpath)
            except OSError as e:
                if onerror is not None:
                    onerror(e)