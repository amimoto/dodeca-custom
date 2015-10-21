from osv import osv, fields

class attribute(osv.osv):
    _name = 'dode.ca.attribute'
    _columns = {
        'name': fields.char('Name', size=255, required=True),
        'attribute_type': fields.selection(
                          [
                              ('string','String'),
                              ('integer','Integer'),
                              ('float','Float'),
                              ('weight','Weight'),
                              ('dollar','Dollar Amount'),
                          ], 
                          'Attribute Type', 
                          required=True
                      ),
    }

