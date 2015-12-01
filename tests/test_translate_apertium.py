# This file is part of the translate_apertium module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class TranslateApertiumTestCase(ModuleTestCase):
    'Test Translate Apertium module'
    module = 'translate_apertium'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        TranslateApertiumTestCase))
    return suite
