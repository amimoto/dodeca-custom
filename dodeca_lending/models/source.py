from osv import osv, fields

class source(osv.osv):
    _name = 'dode.ca.source'
    _columns = {
        'asset_id': fields.many2one('dode.ca.asset','Asset',required=True),
        'partner_id': fields.many2one('res.partner', 'Partner'),
        'part_number': fields.text('Partner Part Number'),
    }

