#This file is part carrier_code module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Carrier']
__metaclass__ = PoolMeta


class Carrier:
    'Carrier'
    __name__ = 'carrier'
    code = fields.Char('Code')

    def get_rec_name(self, name):
        if self.code:
            return '%s - %s' % (
                    self.party.rec_name,
                    self.code,
                    )
        else:
            return '%s - %s' % (
                    self.party.rec_name,
                    self.carrier_product.rec_name,
                    )
