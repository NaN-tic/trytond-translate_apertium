# This file is part of translate_apertium module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import subprocess
from trytond.pool import Pool, PoolMeta

__all__ = ['TranslateWizardStart', 'TranslateWizardTranslation']
__metaclass__ = PoolMeta


def apertium_output(cmd, stdin=''):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout, stderr = process.communicate(stdin.encode('utf-8'))
    process.wait()
    return unicode(stdout, 'utf-8'), stderr


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
        Config = Pool().get('translate.configuration')
        trans_config = Config(1)

        lang = '%s-%s' % (source_lang[:2], target_lang[:2])
        cmd = ['apertium', lang]
        if trans_config.apertium_unknown_words:
            cmd.append('-u')
        out, error = apertium_output(cmd, text)
        if error:
            cls.raise_user_error('error_translating', error_args=(text,))
        return out.strip('\r\n')
