from sqlalchemy import create_engine, Column, INTEGER, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker

# اتصال به دیتابیس 

engine = create_engine('sqlite:///StudentData.db', echo=False)
engine.connect()

Base = declarative_base()


# تعریف جدول 

class Student(Base):
    __tablename__ = 'students'

    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)
    score = Column(Float)

    
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', score={self.score})>"




Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

               


print("========== CREATE ==========")

student1 = Student(name='Ali',   score=18.5)
student2 = Student(name='Sara',  score=19.75)
student3 = Student(name='Reza',  score=15.0)

session.add_all([student1, student2, student3])
session.commit()

print("3 دانش‌آموز اضافه شد.")


                     


print("\n========== READ (All) ==========")

all_students = session.query(Student).all()
for s in all_students:
    print(s.id, '|', s.name, '|', s.score)


                      


print("\n========== UPDATE ==========")


student_to_update = session.query(Student).filter_by(id=1).first()

if student_to_update is not None:
    student_to_update.name = 'Ali Ahmadi'  
    student_to_update.score = 20.0          
    session.commit()
    print(f"دانش‌آموز با id=1 به‌روزرسانی شد: {student_to_update}")


  

print("\n========== DELETE ==========")


student_to_delete = session.query(Student).filter_by(id=3).first()

if student_to_delete is not None:
    session.delete(student_to_delete)
    session.commit()
    print("دانش‌آموز با id=3 حذف شد.")


              


print("\n========== FINAL STATE ==========")

final_list = session.query(Student).all()
for s in final_list:
    print(s.id, '|', s.name, '|', s.score)

session.close()