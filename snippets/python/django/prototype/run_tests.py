import unittest
from django.test.utils import setup_test_environment, setup_databases
from django.test.runner import DiscoverRunner

setup_test_environment()
names = setup_databases(verbosity=1, interactive=True)
runner = DiscoverRunner()

suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
result = runner.run_suite(suite)
runner.suite_result(suite, result)
