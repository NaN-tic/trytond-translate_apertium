# This file is part of translate_apertium module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .configuration import *
from .translate import *

def register():
    Pool.register(
        Configuration,
        TranslateWizardStart,
        TranslateWizardTranslation,
        module='translate_apertium', type_='model')
