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
    node = cl.filter_empty_nodes(FileNode('trash', False, []))
    assert None == node

#def test2():
#    answer = FileNode(
#        'test_02',
#        is_dir=True,
#        children=[]
#    )
    

    
   # assert answer != cl.get('/tests/test_02', True, True)

