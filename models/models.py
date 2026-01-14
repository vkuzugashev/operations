from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#definition models
class Unit(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    parent_id = db.Column(db.String(10), nullable=True)
    name = db.Column(db.String(100), nullable=False)
    unit_type = db.Column(db.Integer, nullable=True)   #0 Work Unit, 1- Work Center, 2-Area, 3-Site, 4-Enterprise

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    use_in_process = db.Column(db.Boolean, nullable=False)
    use_in_operation = db.Column(db.Boolean, nullable=False)
    use_in_unit = db.Column(db.Boolean, nullable=False)
    use_in_material = db.Column(db.Boolean, nullable=False)
    use_in_personal = db.Column(db.Boolean, nullable=False)

class OperationType(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class SpecificationType(db.Model):
    id = db.Column(db.String(10), primary_key=True)

class Specification(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    specification_type = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(10), nullable=False)
    version = db.Column(db.String(10), nullable=False)

class ProcessDef(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    unit_id = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(10), nullable=True)
    note = db.Column(db.String(500), nullable=True)
    product_id = db.Column(db.String(10), nullable=True)    
    specification_id = db.Column(db.String(10), nullable=True)

class OperationDef(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    process_id = db.Column(db.String(10), primary_key=True)
    operation_type = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    operation_order = db.Column(db.Integer, nullable=False)
    version = db.Column(db.String(10), nullable=True)
    note = db.Column(db.String(500), nullable=True)
    product_id = db.Column(db.String(10), nullable=True)    
    specification_id = db.Column(db.String(10), nullable=True)

class OperationUnitDef(db.Model):
    operation_id = db.Column(db.String(10), primary_key=True)
    unit_id = db.Column(db.String(10), primary_key=True)
    note = db.Column(db.String(500), nullable=True)
    quantity = db.Column(db.Float, nullable=True)

#runtime models
class Process(db.Model):
    process_id = db.Column(db.String(10), primary_key=True)
    unit_id = db.Column(db.String(10), primary_key=True)
    direction = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, primary_key=True)
    stop_time = db.Column(db.DateTime, nullable=True)
    product_id = db.Column(db.String(10), nullable=True)    
    specification_id = db.Column(db.String(10), nullable=True)    
    status = db.Column(db.Integer, nullable=True)
    note = db.Column(db.String(500), nullable=True)

class Operation(db.Model):
    process_id = db.Column(db.String(10), primary_key=True)
    operation_id = db.Column(db.String(10), primary_key=True)
    direction = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, primary_key=True)
    stop_time = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.Integer, nullable=True)
    note = db.Column(db.String(500), nullable=True)
    product_id = db.Column(db.String(10), nullable=True)    
    specification_id = db.Column(db.String(10), nullable=True)

class OperationUnitMaterial(db.Model):
    operation_id = db.Column(db.String(10), primary_key=True)
    unit_id = db.Column(db.String(10), primary_key=True)
    material_id = db.Column(db.String(10), primary_key=True)    
    direction = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, primary_key=True)
    stop_time = db.Column(db.DateTime, nullable=True)
    quality_id = db.Column(db.String(10), nullable=True)    
    quantity = db.Column(db.Float, nullable=True)
    status = db.Column(db.Integer, nullable=True)

class OperationUnitPersonal(db.Model):
    operation_id = db.Column(db.String(10), primary_key=True)
    unit_id = db.Column(db.String(10), primary_key=True)
    personal_id = db.Column(db.String(10), primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    stop_time = db.Column(db.DateTime, nullable=True)
    direction = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Float, nullable=True)
    status = db.Column(db.Integer, nullable=True)

class OperatonUnit(db.Model):
    operation_id = db.Column(db.String(10), primary_key=True)
    unit_id = db.Column(db.String(100), primary_key=True)
    start_time = db.Column(db.DateTime, primary_key=True)
    stop_time = db.Column(db.DateTime, nullable=True)
    direction = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Float, nullable=True)
    status = db.Column(db.Integer, nullable=True)
