from django.db import models

# Create your models here.

COMPUTER_SCIENCE = 'Computer Science'
BUSINESS = 'Business'

CS_1 = 'Software Engineer'
CS_2 = 'Data Scientist'
B_1 = 'Accountant'
B_2 = 'Financial Analyst'

SUBJECT_CHOICES = [
    (COMPUTER_SCIENCE, COMPUTER_SCIENCE),
    (BUSINESS, BUSINESS),
]

JOB_CHOICES = [
    (CS_1, CS_1),
    (CS_2, CS_2),
    (B_1, B_1),
    (B_2, B_2),
]

def get_cs_strings():
    cs_strings = [
        CS_1,
        CS_2,
    ]

    return cs_strings


def get_b_strings():
    b_strings = [
        B_1,
        B_2,
    ]

    return b_strings

class Person(models.Model):
    # id_name
    name = models.CharField(max_length=50)
    # id_subject
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    # id_job
    job = models.CharField(max_length=50, choices=JOB_CHOICES)