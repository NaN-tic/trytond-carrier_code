#This file is part carrier_code module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Carrier']
__metaclass__ = PoolMeta


class Carrier:
    __name__ = 'carrier'
    description = fields.Char('Description')
    code = fields.Char('Code')
    sequence = fields.Integer('Sequence')

    @classmethod
    def __setup__(cls):
        super(Carrier, cls).__setup__()
        cls._order.insert(0, ('sequence', 'ASC'))
        cls._order.insert(1, ('party', 'ASC'))

    @staticmethod
    def default_sequence():
        return 1

    def get_rec_name(self, name):
        if self.code and self.description:
            return '[%s] - %s' % (
                    self.code,
                    self.description,
                    )
        if self.description:
            return '%s' % (
                    self.description,
                    )
        return '%s - %s' % (
                self.party.rec_name,
                self.carrier_product.rec_name,
                )
