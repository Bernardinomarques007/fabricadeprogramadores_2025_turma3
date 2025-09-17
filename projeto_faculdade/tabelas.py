import datetime
from sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# configuração da conexão
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/postgres"

# A engine gerencia as conexões com o banco
engine = create_engine(DATABASE_URL)

# configuração da sessão
# a sessão é a nossa "area de trabalho" para conversar com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base Declarativa
# Ela faz a ligação entre nossas classes e as tabelas do banco
Base = declarative_base()

# mapeamento da tabela 'usuarios' para a classe m'usuario
class Usuario(Base):

    __tablename__ = "usuarios" # O nome exato da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True)
    nome = column(String(255, nullable=False))
    email = column(String(255), unique=True, nullable=False)
    senha_hash = Column(DateTime(timezone=True), default=datetime.datetime.now)

    notas = relationship("Nota", back_populates="autor")