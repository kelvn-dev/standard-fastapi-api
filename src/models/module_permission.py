from fastapi_utils.guid_type import GUID
from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, String)
from sqlalchemy.orm import relationship

from database import Base
from models import Module


class ModulePermission(Base):
  __tablename__ = 'module_permission'
  group_id = Column(GUID, ForeignKey('group.id'), primary_key=True)
  module_id = Column(GUID, ForeignKey('module.id'), primary_key=True)
  module = relationship(Module, lazy='joined')
  read = Column(Boolean, nullable=False)
  create = Column(Boolean, nullable=False)
  update = Column(Boolean, nullable=False)
  delete = Column(Boolean, nullable=False)
