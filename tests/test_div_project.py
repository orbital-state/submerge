import os
import unittest
from unittest.mock import patch, MagicMock
from submerge.div.project import DivProject
from submerge.div.error import DivError

dive_folder_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "dive")

class TestDivProject(unittest.TestCase):

    @patch("os.getcwd")
    @patch("os.path.exists")
    def test_discover_root_path(self, mock_exists, mock_getcwd):
        """
        Test that the project correctly discovers the root path when the current path is the root.
        """
        # Mock the current working directory to be the root path
        mock_getcwd.return_value = dive_folder_path
        mock_exists.return_value = True

        project = DivProject()
        project._discover()

        self.assertEqual(project.root_folder_path, dive_folder_path)
        self.assertEqual(project.current_node_folder_path, dive_folder_path)
        self.assertEqual(project.current_node_key, "root")
        self.assertEqual(project.project_name, "submerge")

    @patch("os.getcwd")
    @patch("os.path.exists")
    def test_discover_child_path(self, mock_exists, mock_getcwd):
        """
        Test that the project correctly discovers the root path when the current path is a child node.
        """
        # Mock the current working directory to be a child node path
        mock_getcwd.return_value = os.path.join(dive_folder_path, "summary")
        mock_exists.side_effect = lambda path: path.endswith("dive") or path.endswith("summary")

        project = DivProject()
        project._discover()

        self.assertEqual(project.root_folder_path, dive_folder_path)
        self.assertEqual(project.current_node_folder_path, os.path.join(dive_folder_path, "summary"))
        self.assertEqual(project.current_node_key, "root/summary")
        self.assertEqual(project.project_name, "submerge")

    @patch("os.getcwd")
    @patch("os.path.exists")
    def test_discover_invalid_path(self, mock_exists, mock_getcwd):
        """
        Test that the project raises an error when the current path does not contain a dive folder.
        """
        # Mock the current working directory to be an invalid path
        mock_getcwd.return_value = os.path.join(os.path.dirname(__file__), "invalid-path")
        mock_exists.return_value = False

        project = DivProject()
        with self.assertRaises(DivError) as context:
            project._discover()

        self.assertIn("INVALID_DIV_THREAD_NODE", str(context.exception))

if __name__ == "__main__":
    unittest.main()