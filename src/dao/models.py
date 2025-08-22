import os
from sqlalchemy import Column, String, Boolean, DateTime, create_engine, BigInteger
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, UTC

from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class User(Base): #new * ????
    __tablename__ = 'olgaservbot_users'


    telegram_id = Column(BigInteger, primary_key=True) # ID пользователя в Telegram
    username = Column(String(50), nullable=True) # @username (может быть None, если скрыт)
    first_name = Column(String(50), nullable=False) #Имя
    last_name = Column(String(50), nullable=True) #Фамилия (можеть быть None)
    phone = Column(String(20), nullable=True) #Телефон (если пользователь его предоставит)
    is_admin = Column(Boolean, default=False) #Админ ли?
    is_activ = Column(Boolean, default=True) #Активен ли аккаунт
    registered_at = Column(DateTime, default=datetime.now(tz=UTC)) # Дата регистрации


    def __repr__(self): #new * ????
        return f"<User(id={self.telegram_id}, username='{self.username}')>"
    
engine = create_engine(
    os.getenv("OLGASERVBOT_DATABASE_URL",'sqlite:///olgaservbot.db'), 
    echo=True) #Что бы можно было подключаться к другой базе данных. Если "OLGASERVBOT_DATABASE_URL" отсутствует создается sqlite:///olgaservbot.db
#Base.metadata.create_all(engine) #Код создания таблиц. Изменили на тот который ниже

AsyncSessionLocal = None
if SERVBOT_ASYNC_DATABASE_URL := os.getenv("OLGASERVBOT_ASYNC_DATABASE_URL"):
    #async_engine = create_async_engine(
    async_engine = create_async_engine(
        os.getenv("OLGASERVBOT_ASYNC_DATABASE_URL", "sqlite+aiosqlite:///olgaservbot.db"),
        echo=True
    )

    #AsyncSessionLocal = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False) #NoQa
    AsyncSessionLocal = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False) #NoQa
