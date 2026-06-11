from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database import Base


class Scan(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String)

    score = Column(Integer)

    risk_level = Column(String)

    findings = Column(Text)

    explanation = Column(Text)

    remediation = Column(Text)

    report_path = Column(String)