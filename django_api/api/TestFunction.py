from functions.PrepData import scale_data

data = {
    "Gender": ['Male'],
    "Married": ['Yes'],
    "Dependents": [0],
    "Education": ['Graduate'],
    "Self_Employed": ['No'],
    "ApplicantIncome": [3500],
    "CoapplicantIncome": [1667],
    "LoanAmount": [11400],
    "Loan_Amount_Term": [360],
    "Credit_History": [0],
    "Property_Area": ['Semiurban'],
}

unit = scale_data(data)

print(unit)
