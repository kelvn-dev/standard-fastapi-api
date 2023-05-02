from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, String)
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class AppUser(BaseModel):
  __tablename__ = 'app_user'
  username = Column(String(255), nullable=False)
  email = Column(String(255), nullable=False)
  password = Column(String(255))
  is_verified = Column(Boolean, nullable=False)
  verify_token = Column(String, unique=True)
  group_id = Column(GUID, ForeignKey('group.id', ondelete='SET NULL'))
  group = relationship('Group', back_populates='app_users')
