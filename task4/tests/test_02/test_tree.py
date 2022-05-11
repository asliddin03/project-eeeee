import pytest
from tree_utils_02.tree import Tree
from tree_utils_02.node import FileNode
import os
import shutil


cl = Tree()

def test1():
    with pytest.raises(AttributeError):
        cl.get('qwwerty', True, False)

    file_node = FileNode(
        name='test_tree.py',
        is_dir = False,
        children=[]
    )
    assert file_node == cl.get('tests/test_02/test_tree.py', False)
    assert None == cl.get('tests/test_02/test_tree.py' , True, True)
    with pytest.raises(AttributeError):
        cl.get('tests/test_02/test_tree.py' , True, False)

    a = cl.get('src', True)
    assert FileNode('src', True, []) != a

    trash =FileNode('trash', False, [])
    assert None == cl.filter_empty_nodes(trash)

    os.chdir('trash1')
    os.mkdir('trash2')
    trash2 = FileNode('trash2', True, [])
    trash1 =FileNode('trash1', True, [trash2])
    assert None == cl.filter_empty_nodes(trash1)
