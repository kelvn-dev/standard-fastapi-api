from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from sqlalchemy import Column, DateTime, String

from models.base_model import BaseModel


class Module(BaseModel):
  __tablename__ = 'module'
  name = Column(String(255))
