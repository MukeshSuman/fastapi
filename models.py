from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from datetime import datetime, timezone

from database import Base


class ContactUs(Base):
  __tablename__ = "contact_us"

  id = Column(Integer, primary_key=True, index=True)
  first_name = Column(String(50), index=True)
  last_name = Column(String(50), index=True)
  company_name = Column(String(50), index=True)
  servicetype = Column(String(15), index=True)
  email = Column(String(120), index=True)
  position = Column(String(50), index=True)
  message = Column(Text, index=True)
  created_at = Column(DateTime, index=True, default=datetime.now(timezone.utc))
