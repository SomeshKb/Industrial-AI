from marshmallow import Schema, fields, validate, ValidationError


class AnomalyModelSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    status = fields.Str(validate=validate.Length(max=50))


create_schema = AnomalyModelSchema()
list_schema = AnomalyModelSchema(many=True)
