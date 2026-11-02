from sqlalchemy import create_engine, Column, INTEGER, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


engine = create_engine('sqlite:///StudentCourse.db', echo=False)
engine.connect()

Base = declarative_base()



class Student(Base):
    __tablename__ = 'students'

    
    id   = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String)

    
    courses = relationship(
        'Course',
        back_populates='student',
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"



class Course(Base):
    __tablename__ = 'courses'

    id         = Column(INTEGER, primary_key=True)
    title      = Column(String)
    unit       = Column(INTEGER)

    
    student_id = Column(INTEGER, ForeignKey('students.id'))

    
    student    = relationship('Student', back_populates='courses')

    def __repr__(self):
        return f"<Course(id={self.id}, title='{self.title}', unit={self.unit})>"


#  ساخت جدول‌ها 
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()



                   

print("========== CREATE ==========")


s1 = Student(name='Ali Ahmadi')
s2 = Student(name='Sara Rezaei')
s3 = Student(name="zahra madmalil")
s4 = Student(name="somayeh kabani")


c1 = Course(title='Python',      unit=1, student=s1)
c2 = Course(title='Database',    unit=2, student=s1)
c3 = Course(title='Web Design',  unit=3, student=s2)

session.add_all([s1, s2, s3 ,s4 ,c1, c2, c3])
session.commit()
print("4 دانش‌آموز و 3 درس اضافه شد.")



 

print("\n========== READ ==========")


print("\n--- همه دانش‌آموزان و درس‌هایشان ---")
for stu in session.query(Student).all():
    print(f"{stu.name} (id={stu.id}) :")
    for crs in stu.courses:            
        print(f"   - {crs.title} ({crs.unit} واحد)")
    print('-' * 30)


print("\n--- همه درس‌ها و دانش‌آموزشان ---")
for crs in session.query(Course).all():
    print(f"{crs.title} → {crs.student.name}")   



             

print("\n========== UPDATE ==========")


python_course = session.query(Course).filter_by(title='Python').first()
if python_course is not None:
    python_course.unit = 4
    session.commit()
    print(f"واحد درس Python به {python_course.unit} تغییر کرد.")


ali = session.query(Student).filter_by(name='Ali Ahmadi').first()
if ali is not None:
    ali.name = 'Ali Ahmadi (Updated)'
    session.commit()
    print(f"نام دانش‌آموز id={ali.id} به '{ali.name}' تغییر کرد.")



           

print("\n========== DELETE ==========")


sara = session.query(Student).filter_by(name='Sara Rezaei').first()
if sara is not None:
    session.delete(sara)
    session.commit()
    print("Sara حذف شد (و درس‌هایش هم به خاطر cascade حذف شدند).")


            
# نمایش وضعیت نهایی
print("\n========== FINAL STATE ==========")
for stu in session.query(Student).all():
    print(f"{stu.name}:")
    for crs in stu.courses:
        print(f"   - {crs.title} ({crs.unit} واحد)")

print("\n--- بررسی اینکه درس‌های Sara حذف شده‌اند ---")
for crs in session.query(Course).all():
    print(f"Course id={crs.id} | {crs.title} | student_id={crs.student_id}")

session.close()
