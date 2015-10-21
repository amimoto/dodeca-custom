from osv import osv, fields


class tag(osv.osv):
    _name = 'dode.ca.tag'
    _columns = {
        'name': fields.char('Name', size=255, required=True),
        'category_id': fields.many2one('dode.ca.category','Catgory',required=True),
    }


