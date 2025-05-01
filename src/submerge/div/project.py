import os
import toml
import logging
from .node import DivNode
from .error import DivError


logger = logging.getLogger(__name__)


class DivProject:
    
    def __init__(self):
        self.project_name = None
        self.root_folder_path = None
        self.current_node_folder_path = None
        # Full tree of div-nodes where 'key = node_sub_folder_path'
        self.nodes = {}
        self.current_node_key = None

    @property
    def root(self):
        return self.nodes['root']

    @property
    def current_node(self):
        return self.nodes[self.current_node_key]

    def load(self):
        """
        Load the project structure and nodes.
        
        This function loads the project structure and nodes from the `.div` folder.
        It also sets the current node to the root node of the project.
        """
        # discover the project structure
        self._discover()
        # load the project configuration
        self.config = self._load_config()
        assert self.config, "Project configuration is empty or invalid."
        assert self.project_name == self.config.get("name"), f"Project name does not match the configuration: {self.project_name} != {self.config.get('name')}"
        
        # Load the full tree of div-nodes starting from the root path.
        self._load_node_tree(self.root_folder_path)
        # Current node is not None
        assert self.current_node is not None, "Current node is None. Project loading failed."

    def _discover(self):
        """
        Discover the project structure and location of the root.
        
        Take the current working directory and check if `dive` folder is one of the parents
        on the absolute path. If it is, interpret the absolute location of `dive` as the root of the project.
        If not, panic
        """
        current_path = os.getcwd()
        self.current_node_folder_path = os.path.abspath(current_path)
        # string must contain dive folder
        if "dive" not in self.current_node_folder_path:
            # dive can be still the subfolder of the software project root
            # check if the dive folder is a subfolder of the current path
            dive_subfolder_path = os.path.join(self.current_node_folder_path, "dive")
            if os.path.exists(dive_subfolder_path):
                self.current_node_folder_path = dive_subfolder_path
            else:
                # panic
                raise DivError("INVALID_DIV_THREAD_NODE: The node path does not contain a dive folder.")
        # get the root path of the project
        self.root_folder_path, self.current_node_key = self.current_node_folder_path.split("dive")
        self.root_folder_path += "dive"
        self.current_node_key = "root" + self.current_node_key
        # get the project name
        self.project_name = os.path.basename(os.path.dirname(self.root_folder_path))
        # check if the project name is valid
        logger.debug(f"Discovered project name: {self.project_name}")
        logger.debug(f"Discovered root path: {self.root_folder_path}")
        logger.debug(f"Discovered current node path: {self.current_node_folder_path}")
        logger.debug(f"Discovered current node key: {self.current_node_key}")
        
    def _load_config(self):
        """
        Load the project configuration from the .div folder.
        No valid project configuration found.
        This function loads the project configuration from the `.div/project.toml`
        """
        config_path = os.path.join(self.root_folder_path, ".div", "project.toml")
        if os.path.exists(config_path):
            with open(config_path, "r") as f:
                config = toml.load(f)
            return config
        else:
            raise DivError(f"No valid project configuration found. Please create a .div/project.toml file in: {self.root_folder_path}")
        
    def _load_node_tree(self, node_folder_path, node_key="root"):
        """
        Load the full tree of div-nodes starting from the root path.
        
        Start by creating and loading the root node.
        Then recursively load all child nodes (by accessing payload of the threads property).
        """
        node = self._load_node(self.root_folder_path)
        self.nodes[self.root_folder_path] = node
        children = node.properties["threads"].payload
        # Load the tree of nodes
        for child in children:
            child_key = f"{node_key}/{child}"
            child_folder_path = os.path.join(node_folder_path, child)
            self.nodes[child_key] = self._load_node(child_folder_path)

    def _load_node(self, node_folder_path):
        """
        Load a single node from the given folder path.

        This function initializes a DivNode object for the folder and calls its load method.
        """
        try:
            # Create a DivNode object for the folder
            node = DivNode(node_folder_path)
            # Call the load method to populate the node's properties
            node.load()
            logger.debug(f"Loaded node from {node_folder_path}")
            return node
        except Exception as error:
            logger.error(f"Failed to load node from {node_folder_path}.")
            raise error
            