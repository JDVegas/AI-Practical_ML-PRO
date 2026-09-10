


# -- SETUP -- 
# -- x-------------------------------x --
# Standard libraries
from typing import Annotated
from datetime import datetime, timezone

# FatsAPI libraries
from fastapi import FastAPI, Depends, HTTPException, status, Query
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel, ConfigDict, Field 

# SQL libraries
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase, relationship



# -- x-------------------------------x --
