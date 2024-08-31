#!/usr/bin/python3

"""
Module that creates the database for the project DoctorGestures.
"""

from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Date, DateTime, Float
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql import text
from sqlalchemy.orm import declarative_base


engine = create_engine('mysql+pymysql://ahmedelkh:Rcajuv1949!!!!@localhost/')
with engine.connect() as connection:
    connection.execute(text("CREATE DATABASE IF NOT EXISTS DoctorGestures"))

login = 'mysql+pymysql://ahmedelkh:Rcajuv1949!!!!@localhost/DoctorGestures'
engine = create_engine(login)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    userId = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(45))
    lastname = Column(String(45))
    username = Column(String(20))
    password = Column(String(45))
    function = Column(String(45))
    createdOn = Column(DateTime)


class Patient(Base):
    __tablename__ = 'patients'
    patientId = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(45))
    lastname = Column(String(45))
    sexe = Column(String(10))
    idCard = Column(String(15))
    address = Column(String(100))
    birthDate = Column(Date)
    patientInsurance = Column(String(50))
    patientFamilyState = Column(String(20))
    patientProfession = Column(String(50))
    registredOn = Column(DateTime)
    registredBy = Column(Integer, ForeignKey('users.userId'))


class Consultation(Base):
    __tablename__ = 'consultations'
    consultationId = Column(Integer, primary_key=True, autoincrement=True)
    patientId = Column(Integer, ForeignKey('patients.patientId'))
    consultedBy = Column(Integer, ForeignKey('users.userId'))
    consultedOn = Column(DateTime)
    consultationType = Column(String(15))
    consultationCause = Column(String(255))
    medicalHistory = Column(String(1000))
    symptomsDevelopment = Column(String(1000))
    functionalSigns = Column(String(1000))


class PhysicalExamination(Base):
    __tablename__ = 'physicalExaminations'
    examinationId = Column(Integer, primary_key=True, autoincrement=True)
    consultationId = Column(Integer,
                            ForeignKey('consultations.consultationId'))
    height = Column(Integer)
    weight = Column(Integer)
    bloodPressure = Column(String(10))
    oxygenSaturation = Column(Float)
    temperature = Column(Float)
    heartRate = Column(Float)
    respiratoryRate = Column(Float)
    conjunctivae = Column(String(30))
    dipStick = Column(String(1000))
    others = Column(String(1000))


class ClinicalExamination(Base):
    __tablename__ = 'clinicalExaminations'
    examinationId = Column(Integer, primary_key=True, autoincrement=True)
    consultationId = Column(Integer,
                            ForeignKey('consultations.consultationId'))
    cardiovascular = Column(String(1000))
    pleuropulmonary = Column(String(1000))
    abdominal = Column(String(1000))
    gynecological = Column(String(1000))
    entExamination = Column(String(1000))
    otherExamination = Column(String(1000))


class AdvancedExamination(Base):
    __tablename__ = 'advancedExaminations'
    examinationId = Column(Integer, primary_key=True, autoincrement=True)
    consultationId = Column(Integer,
                            ForeignKey('consultations.consultationId'))
    ultraSound = Column(String(1000))
    EKG = Column(String(1000))
    otherExamination = Column(String(1000))


class Prescription(Base):
    __tablename__ = 'prescriptions'
    prescriptionId = Column(Integer, primary_key=True, autoincrement=True)
    consultationId = Column(Integer,
                            ForeignKey('consultations.consultationId'))
    medicines = Column(String(1000))
    labAnalysis = Column(String(1000))
    radiologicalExamination = Column(String(1000))
    reference = Column(String(1000))


Base.metadata.create_all(engine)
