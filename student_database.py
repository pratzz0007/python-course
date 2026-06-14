class student:
    def __init__(self, name, grade,administration_no):
        self.name =name
        self.grade = grade
        self.administration_no = administration_no

        defis_passing(self):
            return self.grade >= 60
     def details (self):
        return f"{self.name} (administration_no: {self.administration_no})"
    student1 = student("pratik", 85, 12345)
    st