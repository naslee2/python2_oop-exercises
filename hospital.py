class Patients(object):
    def __init__(self, ids, Name, Allergies):
        self.ids = ids
        self.Name = Name
        self.Allergies = Allergies
        self.BedNum = 0

class Hospital(object):
    def __init__(self,Hname, Capacity ):
        self.Patients = []
        self.Hname = Hname
        self.Capacity = Capacity

    def admit(self, NewPatient):
        if len(self.Patients) < self.Capacity:
            self.Patients.append(NewPatient)
            NewPatient.BedNum = self.Capacity - self.Capacity+ len(self.Patients)
            print "Patient Admitted", NewPatient.Name
        else: 
            print "Hospital is full, Patient not Admitted"
        return self
    def discharge(self,OutPatient):
        for i in range(0, len(self.Patients)):
            if self.Patients[i].Name == OutPatient:
                self.Patients[i].BedNum = 0
                self.Patients.pop(i)
                break
        return self
    def info(self):
        for x in range(0, len(self.Patients)):
            print self.Patients[x].Name
        return self

HospitalName = Hospital("Bob Hope Hospital", 500)
patient1 = Patients("121", "John Doe", "Hay Fever")
patient2 = Patients("471", "Steve Ray", "Flu")
HospitalName.admit(patient1).admit(patient2).discharge("John Doe").info()
            