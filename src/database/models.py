import uuid
from sqlalchemy import Column, String, Boolean, DateTime, Integer, Text, ForeignKey, JSON
from sqlalchemy.sql import func
from src.database.database import Base

class AssetModel(Base):
    __tablename__ = "assets"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    hostname = Column(String, unique=True, index=True, nullable=False)
    ip_address = Column(String, nullable=True)
    environment = Column(String, default="Production")
    business_criticality = Column(String, default="High")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class FindingModel(Base):
    __tablename__ = "findings"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    source = Column(String, nullable=False)
    external_id = Column(String, nullable=False)
    asset_identifier = Column(String, index=True, nullable=False)
    cve_id = Column(String, index=True, nullable=False)
    technical_severity = Column(String, nullable=False)
    severity_score = Column(Integer, default=0)
    exploit_status = Column(Boolean, default=False)
    status = Column(String, default="OPEN")
    raw_payload = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class CampaignModel(Base):
    __tablename__ = "campaigns"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    scope_description = Column(Text, nullable=True)
    target_date = Column(String, nullable=True)
    status = Column(String, default="ACTIVE")
    created_at = Column(DateTime(timezone=True), server_default=func.now())