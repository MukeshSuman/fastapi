from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime, timezone

from database import Base


class ContactUs(Base):
  __tablename__ = "contact_us"

  id = Column(Integer, primary_key=True, index=True)
  first_name = Column(String(50), index=True)
  last_name = Column(String(50), index=True)
  company_name = Column(String(50), index=True)
  service = Column(String(15), index=True)
  email = Column(String(120), index=True)
  position = Column(String(50), index=True)
  message = Column(Text, index=True)
  date = Column(DateTime, default=datetime.now(timezone.utc))
  type = Column(String(15), index=True)
  created_at = Column(DateTime, index=True, default=datetime.now(timezone.utc))

  def __repr__(self):
    return f"<ContactUs {self.id}>"


class ContactTableBase(Base):
  __tablename__ = "contact"

  id = Column(Integer, primary_key=True, index=True)
  first_name = Column(String(50), index=True)
  last_name = Column(String(50), index=True)
  company_name = Column(String(50), index=True)
  service = Column(String(15), index=True)
  email = Column(String(120), index=True)
  position = Column(String(50), index=True)
  message = Column(Text, index=True)
  date = Column(DateTime, default=datetime.now(timezone.utc))
  type = Column(String(15), index=True)
  created_at = Column(DateTime, index=True, default=datetime.now(timezone.utc))
