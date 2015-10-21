from osv import osv, fields

class person(osv.osv):
    _name = 'dode.ca.person'
    _description = 'Person'
    _columns = {
        'name': fields.char('Name', size=255, required=True),
        'user_id': fields.many2one('res.users','Associated User',help="Associated User Account"),
    }

