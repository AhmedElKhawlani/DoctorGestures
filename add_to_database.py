#!/usr/bin/python3

"""
Module that defines functions that adds data to tables.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from create_database import User, Patient
from create_database import Consultation
from create_database import PhysicalExamination, ClinicalExamination
from create_database import AdvancedExamination, Prescription


def connect_to_db():
    login = 'mysql+pymysql://ahmedelkh:Rcajuv1949!!!!@localhost/DoctorGestures'
    engine = create_engine(login)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def add_user(data):
    session = connect_to_db()
    new_user = User(firstname=data['firstname'],
                    lastname=data['lastname'].upper(),
                    username=data['username'],
                    password=data['password'],
                    function=data['function'],
                    createdOn=datetime.now())
    session.add(new_user)
    session.commit()
    session.close()


def add_patient(data):
    session = connect_to_db()
    new_patient = Patient(
        firstname=data['firstname'],
        lastname=data['lastname'].upper(),
        sexe=data['sexe'],
        idCard=data['idCard'],
        address=data['address'],
        birthDate=data['birthDate'],
        patientInsurance=data['patientInsurance'],
        patientFamilyState=data['patientFamilyState'],
        patientProfession=data['patientProfession'],
        registredOn=datetime.now(),
        registredBy=data['registredBy'])
    session.add(new_patient)
    session.commit()
    session.close()


def add_consultation(data):
    session = connect_to_db()
    new_consultation = Consultation(
        patientId=data['patientId'],
        consultedBy=data['consultedBy'],
        consultedOn=datetime.now(),
        consultationType=data['consultationType'],
        consultationCause=data['consultationCause'],
        medicalHistory=data['medicalHistory'],
        symptomsDevelopment=data['symptomsDevelopment'],
        functionalSigns=data['functionalSigns'])
    session.add(new_consultation)
    session.commit()
    session.close()


def add_physical_examination(data):
    session = connect_to_db()
    new_examination = PhysicalExamination(
        consultationId=data['consultationId'],
        height=data['height'],
        weight=data['weight'],
        bloodPressure=data['bloodPressure'],
        oxygenSaturation=data['oxygenSaturation'],
        temperature=data['temperature'],
        heartRate=data['heartRate'],
        respiratoryRate=data['respiratoryRate'],
        conjunctivae=data['conjunctivae'],
        dipStick=data['dipStick'],
        others=data['others'])
    session.add(new_examination)
    session.commit()
    session.close()


def add_clinical_examination(data):
    session = connect_to_db()
    new_examination = ClinicalExamination(
        consultationId=data['consultationId'],
        cardiovascular=data['cardiovascular'],
        pleuropulmonary=data['pleuropulmonary'],
        abdominal=data['abdominal'],
        gynecological=data['gynecological'],
        entExamination=data['entExamination'],
        otherExamination=data['otherExamination'])
    session.add(new_examination)
    session.commit()
    session.close()


def add_advanced_examination(data):
    session = connect_to_db()
    new_examination = AdvancedExamination(
        consultationId=data['consultationId'],
        ultraSound=data['ultraSound'],
        EKG=data['EKG'],
        otherExamination=data['otherExamination'])
    session.add(new_examination)
    session.commit()
    session.close()


def add_prescription(data):
    session = connect_to_db()
    new_prescription = Prescription(
        consultationId=data['consultationId'],
        medicines=data['medicines'],
        labAnalysis=data['labAnalysis'],
        radiologicalExamination=data['radiologicalExamination'],
        reference=data['reference'])
    session.add(new_prescription)
    session.commit()
    session.close()
