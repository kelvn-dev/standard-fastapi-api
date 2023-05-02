from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Group(BaseModel):
  __tablename__ = 'group'
  name = Column(String(255))
  app_users = relationship('AppUser', back_populates='group')
  module_permissions = relationship('ModulePermission', backref='group', cascade='all, delete-orphan')