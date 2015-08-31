# trim_git_index.py
#
# Trim trailling whitespace from your git index.
# Use with care since it mutates your index directly.
#
# If you use VIM you can just do `execute(':%s:\v\s+$::g')`
#
# Usage: Call this script from your root git directory. Requires GitPython

from git import Repo
import os

def get_all_changed_files():
    curr_dir = os.getcwd()
    repo = Repo(curr_dir)
    assert not repo.bare

    index = repo.index
    return [curr_dir + os.sep + diff.a_blob.path for diff in index.diff(None)]

def trim_files(files):
    for f_name in files:
        new_lines = []
        did_trim = False

        with open(f_name, 'r') as f:
            lines = f.readlines()
            for l in lines:
                new_line = l.rstrip() + '\n'
                new_lines += new_line
                did_trim = len(new_line) != len(l)

        if did_trim:
            with open(f_name, 'w') as f:
                f.writelines(new_lines)
            print 'Trim: ' + f_name


if __name__ == '__main__':
    all_files = get_all_changed_files()
    trim_files(all_files)
    print "==== Success ===="
