def examCheck(valueOfExam):
    if valueOfExam <= 100 and valueOfExam >= 90: return 'Feedback: Sangat baik'
    elif valueOfExam <= 89 and valueOfExam >= 80: return 'Feedback: Baik'
    elif valueOfExam <= 79 and valueOfExam >= 70: return 'Feedback: Cukup'
    elif valueOfExam <= 69 and valueOfExam >= 60: return 'Feedback: Kurang'