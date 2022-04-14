from tree_utils_02.node import FileNode
from tree_utils_02.size_tree import SizeTree
from tree_utils_02.size_node import FileSizeNode
import os


a1 = '/home/asliddin/Desktop/git/project-eeeee/task4/TechProgTemplates/task-testing-python'
a2  = '/home/asliddin/Desktop/git/project-eeeee/task4/TechProgTemplates/task-testing-python/src/simple_library_01/functions.py'

tree = SizeTree()
cl = FileSizeNode (
    os.path.basename(a1),
    True,
    [],
    4096
)

def test1():
    assert cl == tree.construct_filenode(a1, True)
    cl.name = os.path.basename(a2)
    cl.size = os.path.getsize(a2)
    cl.is_dir = False
    assert cl == tree.construct_filenode(a2, False)

cl1 = FileSizeNode(
    a1 + '/tests/test_02',
    True,
    [],
    4096
)
def test2():
    a3 = a1 + '/tests/test_02'
    cl2 = cl1
    res = 0
    for item in os.listdir(a3):
        res += os.path.getsize(a3 + '/' + item)
        cl1.children.append(FileSizeNode(item,
                                        False,
                                        [],
                                        os.path.getsize(a3 + '/' + item)))
    cl2.size = res
    assert cl2 == tree.update_filenode(cl1)

