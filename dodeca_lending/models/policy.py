from osv import osv, fields

class policy(osv.osv):
    _name = 'dode.ca.policy'
    _columns = {
        'name': fields.char('Name', size=255, required=True),
        'owner_person_id': fields.many2one('dode.ca.person','Owner',help="Owner's Identity"),
        'visible_qty': fields.integer('Visible Quantity',
                                help="Visible when quantity of asset is greater than this number"),
        'borrow_qty': fields.integer('Borrowable Quantity',
                              help="Borrowable when quantity of asset is greater than this number"),
        'purchase_qty': fields.integer('Purchase Quantity',
                              help="Purchasable when quantity of asset is greater than this number"),
    }

class policy_list(osv.osv):
    _name = 'dode.ca.policy.list'
    _columns = {
        'list_id': fields.many2one('dode.ca.person.list','Person List',required=True),
        'policy_id': fields.many2one('dode.ca.policy','Policy',required=True),
    }

