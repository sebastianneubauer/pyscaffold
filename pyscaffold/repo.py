# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import

from os.path import join as join_path

from sh import git

from . import utils

__author__ = "Florian Wilhelm"
__copyright__ = "Blue Yonder"
__license__ = "new BSD"


def git_tree_add(struct, prefix=None):
    if prefix is None:
        prefix = ""
    for name, content in struct.iteritems():
        if isinstance(content, str):
            git("add", join_path(prefix, name))
        elif isinstance(content, dict):
            git_tree_add(struct[name], prefix=join_path(prefix, name))
        else:
            raise RuntimeError("Don't know what to do with content type "
                               "{type}.".format(type=type(content)))


def init_commit_repo(project, struct):
    with utils.chdir(project):
        git("init")
        git_tree_add(struct[project])
        git("commit", "-m", "Initial commit")
