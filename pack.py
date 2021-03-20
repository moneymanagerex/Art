#!/usr/bin/env python
# vi:tabstop=4:expandtab:shiftwidth=4:softtabstop=4:autoindent:smarttab

import os
import shutil

def pack_theme(root_dir, themes, package):
    os.chdir(root_dir)
    print ('~~|zip|~~ ', package + '.zip')
    path = os.path.join(root_dir, themes, package)
    print(path)
    shutil.make_archive(package, 'zip', path)
    #base = os.path.splitext(my_file)[0]
    old_file = os.path.join(root_dir, package) + ".zip"
    new_file = os.path.join(root_dir, package) + ".mmextheme"
    print(old_file, new_file)
    os.rename(old_file, new_file)

if __name__ == '__main__':
    themes = 'themes'
    root = os.path.dirname(os.path.realpath(__file__))
    dir_list = next(os.walk(themes))[1]
    print(dir_list)

    for dir in dir_list:
        print(dir)
        try:
            pack_theme(root, themes, dir)
        except:
            print ('[X] Exception')
            exit(1)
    print ('[V] OK')
    exit(0)
