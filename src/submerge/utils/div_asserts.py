import os


def is_div_node(node_path):
    """
    Check if the given path is a valid DIV node.
    A valid DIV node must contain a `.div` subfolder.
    """
    return os.path.isdir(node_path) \
            and (os.path.isdir(os.path.join(node_path, ".div")) 
                or os.path.isfile(os.path.join(node_path, "prompt.div")))