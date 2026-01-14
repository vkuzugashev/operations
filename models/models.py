from typing import Optional
from sqlalchemy import create_engine, String, Integer, Boolean, Float, DateTime, Text, select, delete
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sqlalchemy.dialects.sqlite import insert as sqlite_insert
from datetime import datetime, timedelta, timezone
from master import Base

class OperType(Base):
    __tablename__ = 'op_types'
    id: Mapped[str] = mapped_column(String(10), primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

class OperSpecificationType(Base):
    __tablename__ = 'op_spec_type'
    id: Mapped[str] = mapped_column(String(10), primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

class OperSpecification(Base):
    __tablename__ = 'op_specs'
    id: Mapped[str] = mapped_column(String(10), primary_key=True)
    op_spec_type: Mapped[str] = mapped_column(String(10), nullable=False)
    name: Mapped[str] = mapped_column(String(10), nullable=False)
    version: Mapped[str] = mapped_column(String(10), nullable=False)

class ProcessDef(Base):
    __tablename__ = 'op_specs'
    id: Mapped[str] = db.Column(db.String(10), primary_key=True)
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
