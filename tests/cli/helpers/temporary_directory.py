#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for the temporary directory CLI arguments helper."""

from __future__ import unicode_literals

import argparse
import unittest

from plaso.cli import tools
from plaso.cli.helpers import temporary_directory
from plaso.lib import errors

from tests.cli import test_lib as cli_test_lib


class TemporaryDirectoryArgumentsHelperTest(cli_test_lib.CLIToolTestCase):
  """Tests for the temporary directory CLI arguments helper."""

  # pylint: disable=protected-access

  _EXPECTED_OUTPUT = '\n'.join([
      'usage: cli_helper.py [--temporary_directory DIRECTORY]',
      '',
      'Test argument parser.',
      '',
      'optional arguments:',
      '  --temporary_directory DIRECTORY, --temporary-directory DIRECTORY',
      ('                        Path to the directory that should be used '
       'to store'),
      '                        temporary files created during processing.',
      ''])

  def testAddArguments(self):
    """Tests the AddArguments function."""
    argument_parser = argparse.ArgumentParser(
        prog='cli_helper.py', description='Test argument parser.',
        add_help=False,
        formatter_class=cli_test_lib.SortedArgumentsHelpFormatter)

    temporary_directory.TemporaryDirectoryArgumentsHelper.AddArguments(
        argument_parser)

    output = self._RunArgparseFormatHelp(argument_parser)
    self.assertEqual(output, self._EXPECTED_OUTPUT)

  def testParseOptions(self):
    """Tests the ParseOptions function."""
    options = cli_test_lib.TestOptions()
    options.temporary_directory = self._GetTestFilePath(['testdir'])

    test_tool = tools.CLITool()
    temporary_directory.TemporaryDirectoryArgumentsHelper.ParseOptions(
        options, test_tool)

    # pylint: disable=no-member
    self.assertEqual(
        test_tool._temporary_directory, options.temporary_directory)

    with self.assertRaises(errors.BadConfigObject):
      temporary_directory.TemporaryDirectoryArgumentsHelper.ParseOptions(
          options, None)


if __name__ == '__main__':
  unittest.main()
