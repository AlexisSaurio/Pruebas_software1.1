# -*- coding: utf-8 -*-

"""
Mock up testing examples.
"""
import unittest
import subprocess
from unittest.mock import patch, mock_open

# Cambiamos la importación para que sea directa
from mockup_exercises import (
    fetch_data_from_api, 
    perform_action_based_on_time,
    read_data_from_file,
    execute_command
)

class TestFetchDataFromApi(unittest.TestCase):
    """
    Fetch data from API unittest class.
    """
    # Quitamos "white_box." del path del patch
    @patch("mockup_exercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Success case.
        """
        mock_get.return_value.json.return_value = {"key": "value"}
        result = fetch_data_from_api("https://api.example.com/data")
        self.assertEqual(result, {"key": "value"})
        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)


class TestReadDataFromFile(unittest.TestCase):
    """
    Read data from file unittest class.
    """
    # builtins no necesita cambiar porque es interno de Python
    @patch("builtins.open", new_callable=mock_open, read_data="contenido de prueba")
    def test_read_data_from_file_success(self, mock_file):
        """
        Success case: File is read correctly.
        """
        result = read_data_from_file("dummy.txt")
        self.assertEqual(result, "contenido de prueba")
        mock_file.assert_called_once_with("dummy.txt", encoding="utf-8")

    @patch("builtins.open")
    def test_read_data_from_file_not_found(self, mock_file):
        """
        Exception case: FileNotFoundError is raised.
        """
        mock_file.side_effect = FileNotFoundError("File not found")
        with self.assertRaises(FileNotFoundError):
            read_data_from_file("missing.txt")


class TestExecuteCommand(unittest.TestCase):
    """
    Execute command unittest class.
    """
    # Quitamos "white_box." del path del patch
    @patch("mockup_exercises.subprocess.run")
    def test_execute_command_success(self, mock_run):
        """
        Success case: Command executes and returns stdout.
        """
        mock_run.return_value.stdout = "salida del comando"
        command = ["ls", "-l"]
        result = execute_command(command)
        self.assertEqual(result, "salida del comando")
        mock_run.assert_called_once_with(command, capture_output=True, check=False, text=True)

    # Quitamos "white_box." del path del patch
    @patch("mockup_exercises.subprocess.run")
    def test_execute_command_called_process_error(self, mock_run):
        """
        Exception case: CalledProcessError is raised.
        """
        command = ["failing_command"]
        mock_run.side_effect = subprocess.CalledProcessError(returncode=1, cmd=command)
        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(command)


class TestPerformActionBasedOnTime(unittest.TestCase):
    """
    Perform Action Based On Time unittest class.
    """
    # Quitamos "white_box." del path del patch
    @patch("mockup_exercises.time.time")
    def test_perform_action_based_on_time_action_a(self, mock_time):
        """
        Action A.
        """
        mock_time.return_value = 5
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")

    # Quitamos "white_box." del path del patch
    @patch("mockup_exercises.time.time")
    def test_perform_action_based_on_time_action_b(self, mock_time):
        """
        Action B.
        """
        mock_time.return_value = 15
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")

if __name__ == '__main__':
    unittest.main()