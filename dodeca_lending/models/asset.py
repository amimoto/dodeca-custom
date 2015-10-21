from osv import osv, fields

class asset(osv.osv):
    _name = 'dode.ca.asset'
    _description = 'Asset'
    _columns = {
        'name': fields.char('Name', size=255, required=True),
        'owner_person_id': fields.many2one('dode.ca.person','dode.ca.person',help="Owner"),
        'description': fields.text('Description'),
        'asset_type': fields.selection([('item','Item'),('consumable','Consumable')], 'Asset Type', required=True),
        'policy_id': fields.many2one('dode.ca.policy','Policy'),
        'list_price': fields.float('List Price'),
    }

class asset_tag(osv.osv):
    _name = 'dode.ca.asset.tag'
    _columns = {
        'asset_id': fields.many2one('dode.ca.asset','Asset',required=True),
        'tag_id': fields.many2one('dode.ca.tag','Tag',required=True),
    }


class asset_attribute(osv.osv):
    _name = 'dode.ca.asset.attribute'
    _columns = {
        'asset_id': fields.many2one('dode.ca.asset','Asset',required=True),
        'tag_id': fields.many2one('dode.ca.tag','Tag'),
        'category_id': fields.many2one('dode.ca.category','Catgory'),
        'attribute_id': fields.many2one('dode.ca.attribute','Attribute',required=True),
        'value': fields.text('Value'),
    }

class asset_move(osv.osv):
    _name = 'dode.ca.asset.move'
    _columns = {
        'asset_id': fields.many2one('dode.ca.asset','Asset',required=True),
        'from_location_id': fields.many2one('dode.ca.location','From Location'),
        'to_location_id': fields.many2one('dode.ca.location','To Location'),
        'quantity': fields.float('Quantity'),
        'timestamp': fields.datetime('Timestamp'),
        'state': fields.selection(
                        [
                            ('pending','Pending'),
                            ('done','Done'),
                            ('reservation','Reserved'),
                        ],
                        'State',
                        required=True,
                    ),
    }

class asset_move_summary(osv.osv):
    _name = 'dode.ca.move.summary'
    _columns = {
        'asset_id': fields.many2one('dode.ca.asset','Asset',required=True),
        'location_id': fields.many2one('dode.ca.location','Location'),
        'timestamp': fields.datetime('Timestamp'),
        'quantity': fields.float('Quantity'),
    }


