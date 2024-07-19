from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from datetime import datetime, timezone

from database import Base
import bcrypt


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
  mob_no = Column(String(15), index=True, nullable=True)
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
  mob_no = Column(String(15), index=True, nullable=True)
  created_at = Column(DateTime, index=True, default=datetime.now(timezone.utc))


class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50))
  email = Column(String(50), unique=True)
  password_hash = Column(String(250))
  is_active = Column(Boolean, default=True)

  def set_password(self, password):
    self.password_hash = bcrypt.hashpw(password.encode('utf-8'),
                                       bcrypt.gensalt()).decode('utf-8')

  def check_password(self, password):
    return bcrypt.checkpw(password.encode('utf-8'),
                          self.password_hash.encode('utf-8'))
