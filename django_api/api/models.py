from django.db import models

# Create your models here.


class Candidature(models.Model):

  GENDER_CHOICES = (
      ('Male', 'Male'),
      ('Female', 'Female'),
  )
  MARRIED_CHOICES = (
      ('Yes', 'Yes'),
      ('No', 'No'),
  )
  GRADUATED_CHOICES = (
      ('Graduate', 'Graduate'),
      ('Not_Graduated', 'Not_Graduated'),
  )
  SELFEMPLOYED_CHOICES = (
      ('Yes', 'Yes'),
      ('No', 'No'),
  )
  PROPERTY_CHOICES = (
      ('Rural', 'Rural'),
      ('Semiurban', 'Semiurban'),
      ('Urban', 'Urban'),
  )

  Dependents = models.FloatField(default=0)
  ApplicantIncome = models.FloatField(default=0)
  CoapplicantIncome = models.FloatField(default=0)
  LoanAmount = models.FloatField(default=0)
  Loan_Amount_Term = models.FloatField(default=0)
  Credit_History = models.FloatField(default=0)
  Gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
  Married = models.CharField(max_length=15, choices=MARRIED_CHOICES)
  Education = models.CharField(max_length=15, choices=GRADUATED_CHOICES)
  Self_Employed = models.CharField(max_length=15, choices=SELFEMPLOYED_CHOICES)
  Property_Area = models.CharField(max_length=15, choices=PROPERTY_CHOICES)

  def __str__(self):
    return self.Gender
