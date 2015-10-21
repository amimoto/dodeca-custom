from osv import osv, fields

class category(osv.osv):
    _name = 'dode.ca.category'
    _columns = {
        'name': fields.char('Name', size=255, required=True),
        'parent_id': fields.many2one('dode.ca.category','Parent'),
        'full_name': fields.char('Full Name', size=255),
    }


class category_attribute(osv.osv):
    _name = 'dode.ca.category.attribute'
    _columns = {
        'category_id': fields.many2one('dode.ca.category','Catgory',required=True),
        'attribute_id': fields.many2one('dode.ca.attribute','Attribute',required=True),
        'required': fields.boolean('Required'),
    }
