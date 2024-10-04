def healltyCheck(age, blood):
    if age >= 60 and blood > 140: return 'Status kesehatan: Tinggi'
    elif age >= 60 and blood <= 140: return 'Status kesehatan: Normal'
    elif age < 60 and blood > 130: return 'Status kesehatan: Tinggi'
    elif age < 60 and blood <= 130: return 'Status kesehatan: Normal'