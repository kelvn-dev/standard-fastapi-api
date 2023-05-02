from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, String)
from sqlalchemy.orm import relationship

from database import Base

class BaseModel(Base):
  __abstract__ = True
  
  id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
  created_by = Column(String, nullable=False)
  created_time = Column(DateTime(timezone=True), nullable=False)
  updated_by = Column(String)
  updated_time = Column(DateTime(timezone=True))
  