# This file is part of translate_apertium module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from subprocess import Popen, PIPE

from trytond.pool import PoolMeta


__all__ = ['TranslateWizardStart', 'TranslateWizardTranslation']
__metaclass__ = PoolMeta


class TranslateWizardStart:
    __name__ = 'translate.wizard.start'

    @classmethod
    def __setup__(cls):
        super(TranslateWizardStart, cls).__setup__()
        value = (None, '')
        if value in cls.translator.selection:
            cls.translator.selection.remove(value)
        value = ('apertium', 'Apertium')
        if value not in cls.translator.selection:
            cls.translator.selection.append(value)


class TranslateWizardTranslation:
    __name__ = 'translate.wizard.translation'

    @classmethod
    def __setup__(cls):
        super(TranslateWizardTranslation, cls).__setup__()
        cls._error_messages.update({
                'error_translating':
                    'Error translating the string %s.',
                })

    @classmethod
    def get_translation_from_apertium(cls, text, source_lang, target_lang):
        proccess = Popen('echo "%s" | apertium %s-%s' %
            (text, source_lang[:2], target_lang[:2]),
            shell=True, stdout=PIPE, stderr=PIPE)
        out, error = proccess.communicate()
        if error:
            cls.raise_user_error('error_translating', error_args=(text,))
        return out.strip('\r\n')
