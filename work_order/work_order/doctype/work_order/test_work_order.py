# Copyright (c) 2013, Aptitude and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Work Order')

class TestWorkOrder(unittest.TestCase):
	pass
