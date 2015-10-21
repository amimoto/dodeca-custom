from osv import osv, fields

class person_list(osv.osv):
    _name = 'dode.ca.person.list'
    _columns = {
        'name': fields.char('Name', size=255, required=True),
        'owner_person_id': fields.many2one('dode.ca.person','Owner',help="Owner's Identity"),
        'member_person_ids': fields.one2many(
                      'dode.ca.person.list.member',
                      'list_id',
                      'Members'
                  ),
    }

class person_list_member(osv.osv):
    _name = 'dode.ca.person.list.member'
    _columns = {
        'list_id': fields.many2one('dode.ca.person.list','Person List',required=True),
        'person_id': fields.many2one('dode.ca.person','Person',help="Owner's Identity",required=True),
    }



