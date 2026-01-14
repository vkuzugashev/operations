from typing import Optional
from sqlalchemy import create_engine, String, Integer, Boolean, Float, DateTime, Text, select, delete
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sqlalchemy.dialects.sqlite import insert as sqlite_insert
from datetime import datetime, timedelta, timezone

class Base(DeclarativeBase):
    pass

class SysFormat(Base):
    __tablename__ = 'sys_formats'
    id: Mapped[str] = mapped_column(String(10), primary_key=True)
    format: Mapped[str] = mapped_column(String(100), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

class Unit(Base):
    __tablename__ = 'units'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(250))
    updated_at: Mapped[datetime] = mapped_column(DateTime)

class WorkUnitType(Base):
    __tablename__ = 'work_unit_types'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(250))
    updated_at: Mapped[datetime] = mapped_column(DateTime)

class WorkUnit(Base):
    __tablename__ = 'work_units'
    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    parent_id: Mapped[str] = mapped_column(String(100), default=1)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    work_unit_type_id: Mapped[int] = mapped_column(Integer, nullable=False) # 4 Unit, 3 Cell, 2 Area, 1 Site, 0 Enterprise
    description: Mapped[Optional[str]] = mapped_column(String(250))
    updated_at: Mapped[datetime] = mapped_column(DateTime)

class State(Base):
    __table__ = 'states'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(10), nullable=False)
    use_in_proc: Mapped[bool] = mapped_column(Boolean)
    use_in_oper: Mapped[bool] = mapped_column(Boolean)
    use_in_unit: Mapped[bool] = mapped_column(Boolean)
    use_in_item: Mapped[bool] = mapped_column(Boolean)
    use_in_pers: Mapped[bool] = mapped_column(Boolean)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

# Operation definition
class OperType(Base):
    __tablename__ = 'op_types'
    id: Mapped[str] = mapped_column(String(10), primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

class OperSpecType(Base):
    __tablename__ = 'op_spec_type'
    id: Mapped[str] = mapped_column(String(10), primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

class OperSpec(Base):
    __tablename__ = 'op_specs'
    id: Mapped[str] = mapped_column(String(10), primary_key=True)
    op_spec_type: Mapped[str] = mapped_column(String(10), nullable=False)
    name: Mapped[str] = mapped_column(String(10), nullable=False)
    version: Mapped[str] = mapped_column(String(10), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

class ProcDef(Base):
    __tablename__ = 'proc_defs'
    id: Mapped[str] = mapped_column(String(10), primary_key=True)
    work_unit_id: Mapped[str] = mapped_column(String(10), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    version: Mapped[str] = mapped_column(String(10), nullable=False)
    note: Mapped[str] = mapped_column(String(500))
    product_id: Mapped[str] = mapped_column(String(10))    
    spec_id: Mapped[str] = mapped_column(String(10))
    updated_at: Mapped[datetime] = mapped_column(DateTime)

class ProcAttr(Base):
    __tablename__ = 'proc_attrs'
    proc_id: Mapped[str] = mapped_column(String(10), primary_key=True)
    attr_id: Mapped[str] = mapped_column(String(10), primary_key=True)
    value: Mapped[str] = mapped_column(String(100), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

class OperDef(Base):
    __tablename__ = 'oper_defs'
    id: Mapped[str] = mapped_column(String(10), primary_key=True)
    proc_id: Mapped[str] = mapped_column(String(10), primary_key=True)
    op_type: Mapped[str] = mapped_column(String(10), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    op_order: Mapped[int] = mapped_column(Integer, nullable=False)
    version: Mapped[str] = mapped_column(String(10), nullable=False)
    note: Mapped[str] = mapped_column(String(500))
    product_id: Mapped[str] = mapped_column(String(10))    
    spec_id: Mapped[str] = mapped_column(String(10))
    updated_at: Mapped[datetime] = mapped_column(DateTime)

class OperAttr(Base):
    __tablename__ = 'oper_attrs'
    oper_id: Mapped[str] = mapped_column(String(10), primary_key=True)
    attr_id: Mapped[str] = mapped_column(String(10), primary_key=True)
    value: Mapped[str] = mapped_column(String(100), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

class OperWorkUnitDef(Base):
    oper_id: Mapped[str] = mapped_column(String(10), primary_key=True)
    work_unit_id: Mapped[str] = mapped_column(String(10), primary_key=True)
    note: Mapped[str] = mapped_column(db.String(500))
    quantity: Mapped[float] = mapped_column(Float)

class AttrType(Base):
    __tablename__ = 'attr_types'
    id: Mapped[str] = mapped_column(String(10), primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False) # bool, int, float, str, select, date, datetime, time
    format: Mapped[str] = mapped_column(String(10)) # формат
    updated_at: Mapped[datetime] = mapped_column(DateTime)

class AttrDef(Base):
    __tablename__ = 'attr_defs' 
    id: Mapped[str] = mapped_column(String(10), primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    attr_type_id: Mapped[str] = mapped_column(String(10), nullable=False)
    note: Mapped[str] = mapped_column(String(500))
    use_in_proc: Mapped[bool] = mapped_column(Boolean)
    use_in_oper: Mapped[bool] = mapped_column(Boolean)
    use_in_unit: Mapped[bool] = mapped_column(Boolean)
    use_in_item: Mapped[bool] = mapped_column(Boolean)
    use_in_pers: Mapped[bool] = mapped_column(Boolean)
    value: Mapped[str] = mapped_column(String(500)) # значения по умолчанию
    updated_at: Mapped[datetime] = mapped_column(DateTime)
