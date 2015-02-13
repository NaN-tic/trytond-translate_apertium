#!/usr/bin/env python
# This file is part of translate_apertium module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.tests.test_tryton import test_depends
import trytond.tests.test_tryton
import unittest


class TranslateApertiumTestCase(unittest.TestCase):
    'Test Translate Apertium module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('translate_apertium')

    def test0005views(self):
        'Test views'
        test_view('translate')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        TranslateApertiumTestCase))
    return suite
