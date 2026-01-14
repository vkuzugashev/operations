from flask import Flask
from models import db, Status, Unit, SpecificationType, Specification, OperationType, ProcessDef, OperationDef, OperationUnitDef 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///opertion.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.Model
        db.drop_all()
        db.create_all()

        # создаем status
        status1 = Status(id=0, name='New',
                         use_in_process=True,
                         use_in_operation=True,
                         use_in_unit=False,
                         use_in_material=False,
                         use_in_personal=False)
        status2 = Status(id=1, name='Run',
                         use_in_process=True,
                         use_in_operation=True,
                         use_in_unit=True,
                         use_in_material=True,
                         use_in_personal=True)
        status3 = Status(id=2, name='Finished',
                         use_in_process=True,
                         use_in_operation=True,
                         use_in_unit=True,
                         use_in_material=True,
                         use_in_personal=True)
        status4 = Status(id=3, name='Canceled',
                         use_in_process=True,
                         use_in_operation=True,
                         use_in_unit=False,
                         use_in_material=False,
                         use_in_personal=False)
        status5 = Status(id=4, name='Pause',
                         use_in_process=True,
                         use_in_operation=True,
                         use_in_unit=True,
                         use_in_material=True,
                         use_in_personal=True)
        db.session.add_all([status1, status2, status3, status4, status5])
        db.session.commit()

        # создаем Units
        unit1 = Unit(id='unit_000', name='Предприятие')
        unit2 = Unit(id='unit_001', name='Цех 1', parent_id='unit_000')
        unit3 = Unit(id='unit_002', name='Рабочий центр 1', parent_id='unit_001')
        db.session.add_all([unit1, unit2, unit3])
        db.session.commit()
        
        # создаем process
        process1 = ProcessDef(id='proc_001', unit_id='unit_002', name='Процесс 1', version='1.0')
        db.session.add_all([process1])
        db.session.commit()

        # создаем OperationType
        oper_type1 = OperationType(id='prod', name='Производство')
        oper_type2 = OperationType(id='inv', name='Склад')
        oper_type3 = OperationType(id='serv', name='Обслуживание')
        db.session.add_all([oper_type1, oper_type2, oper_type3])
        db.session.commit()

        # создаем operation
        oper1 = OperationDef(id='oper_01', process_id='proc_001', operation_type='prod', name='Операция 1', operation_order=1, version='1.0')
        oper2 = OperationDef(id='oper_02', process_id='proc_001', operation_type='prod', name='Операция 2', operation_order=2, version='1.0')
        oper3 = OperationDef(id='oper_03', process_id='proc_001', operation_type='prod', name='Операция 3', operation_order=3, version='1.0')
        db.session.add_all([oper1, oper2, oper3])
        db.session.commit()

        # создаем SpecificationType
        spec_type1 = SpecificationType(id='material')
        spec_type2 = SpecificationType(id='unit')
        spec_type3 = SpecificationType(id='personal')
        db.session.add_all([spec_type1, spec_type2, spec_type3])
        db.session.commit()

        # создаем Specification
        spec1 = Specification(id='oper_01', specification_type='unit', name='', version='1.0' )
        db.session.add_all([spec1])
        db.session.commit()

        # создаем operation units
        oper_unit1 = OperationUnitDef(unit_id='unit_002', operation_id='oper_01')
        oper_unit2 = OperationUnitDef(unit_id='unit_002', operation_id='oper_02')
        oper_unit3 = OperationUnitDef(unit_id='unit_002', operation_id='oper_03')
        db.session.add_all([oper_unit1, oper_unit2, oper_unit3])
        db.session.commit()
