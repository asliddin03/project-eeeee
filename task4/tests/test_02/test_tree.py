import pytest
from tree_utils_02.tree import Tree
from tree_utils_02.node import FileNode
import os
import shutil


cl = Tree()
a1 = '/home/asliddin/Desktop/git/project-eeeee/task4/TechProgTemplates/task-testing-python'

def test1():
    with pytest.raises(AttributeError):
        cl.get(a1 + 'sdjfgsdjgfhf', True, False)

    file_node = FileNode(
        name='test_tree.py',
        is_dir = False,
        children=[]
    )
    assert file_node == cl.get(a1 + '/tests/test_02/test_tree.py', False)
    assert None == cl.get(a1 + '/tests/test_02/test_tree.py' , True, True)
    with pytest.raises(AttributeError):
        cl.get(a1 + '/tests/test_02/test_tree.py' , True, False)

def test2():
    answer = FileNode(
        'test_02',
        is_dir=True,
        children=[]
    )
    
    for child_filename in sorted(os.listdir(a1 + '/tests/test_02')):
        child_path = os.path.join(a1 + '/tests/test_02', child_filename)

        child_node = cl.get(
            child_path,
            dirs_only=True,
            recurse_call=True
        )

        if child_node is not None:
            answer.children.append(child_node)
    assert answer == cl.get(a1 + '/tests/test_02', True, True)

