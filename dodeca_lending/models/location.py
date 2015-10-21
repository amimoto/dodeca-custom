from osv import osv, fields

class location(osv.osv):
    _name = 'dode.ca.location'
    _columns = {
        'name': fields.char('Name', size=255, required=True),
        'owner_person_id': fields.many2one('dode.ca.person','Owner',help="Owner's Identity"),
        'parent_id': fields.many2one('dode.ca.location','Parent Location'),
    }
