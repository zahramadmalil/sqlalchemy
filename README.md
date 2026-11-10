<div align="center">

# 🗄️ SQLAlchemy Learning Project

### 📘 مستندات جامع و آموزش عملی SQLAlchemy از صفر تا روابط پیشرفته

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-red?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Educational-yellow?style=for-the-badge)]()

</div>

---

## 📖 درباره پروژه

این مخزن، یک **مجموعه آموزشی کامل، گام‌به‌گام و عملی** از کتابخانه‌ی قدرتمند **SQLAlchemy** در زبان پایتون است. 

هدف این پروژه، آموزش مفاهیم **ORM (Object-Relational Mapping)** از سطح مقدماتی تا پیشرفته است. در این پروژه، به جای نوشتن کوئری‌های خام SQL، با اشیاء پایتونی کار می‌کنیم که این کار کدنویسی را بسیار خواناتر، امن‌تر (در برابر SQL Injection) و سریع‌تر می‌کند.

### 🗂️ فایل‌های پروژه

این پروژه شامل چهار فایل مستقل است که هر کدام یک بخش از قابلیت‌های SQLAlchemy را پوشش می‌دهند:

| # | نام فایل | موضوع | سطح |
|---|---|---|---|
| ۱ | `app1.py` (بخش ماشین) | مبانی ORM، تعریف مدل، CRUD پایه، کوئری‌های شرطی | 🟢 مقدماتی |
| ۲ | `app2.py` (بخش ماشین) | روابط یک‌به‌چند (One-to-Many) بین دو جدول | 🟡 متوسط |
| ۳ | `app1.py` (بخش دانش‌آموز) | پیاده‌سازی کامل CRUD با خروجی زیبا در کنسول | 🟡 متوسط |
| ۴ | `app2.py` (بخش دانش‌آموز) | روابط پیشرفته + حذف آبشاری (Cascade Delete) | 🔴 پیشرفته |

> ⚠️ **توجه مهم:** در پروژه شما دو فایل با نام `app1.py` و دو فایل با نام `app2.py` وجود دارد. در این مستندات، برای جلوگیری از سردرگمی، هر فایل را با موضوع آن (ماشین یا دانش‌آموز) تفکیک کرده‌ایم. پیشنهاد می‌شود فایل‌ها را در پوشه‌های `tamrin1` و `tamrin2` قرار دهید.

---

## ✨ ویژگی‌های کلیدی

- ✅ **تعریف مدل‌ها (Models):** تبدیل کلاس‌های پایتون به جداول دیتابیس با `declarative_base`.
- ✅ **عملیات CRUD کامل:** ایجاد (Create)، خواندن (Read)، به‌روزرسانی (Update) و حذف (Delete).
- ✅ **کوئری‌های پیشرفته:** استفاده از `filter`، `filter_by`، `like`، `>`, `<` و توابع تجمیعی.
- ✅ **مدیریت روابط (Relationships):** پیاده‌سازی روابط یک‌به‌چند با `ForeignKey` و `relationship`.
- ✅ **دسترسی دوطرفه:** استفاده از `back_populates` برای دسترسی از هر دو سمت رابطه.
- ✅ **حذف آبشاری (Cascade Delete):** حذف خودکار رکوردهای وابسته با `delete-orphan`.
- ✅ **سفارشی‌سازی خروجی:** استفاده از متد `__repr__` برای نمایش خوانا در کنسول.
- ✅ **دیتابیس SQLite:** بدون نیاز به نصب سرور دیتابیس، سبک و سریع.

---

## 🧰 پیش‌نیازها

قبل از اجرای پروژه، مطمئن شوید موارد زیر روی سیستم شما نصب شده‌اند:

- **Python** نسخه ۳.۸ یا بالاتر
- **pip** (مدیر بسته‌های پایتون)

برای بررسی نسخه پایتون خود، در ترمینال دستور زیر را اجرا کنید:

python --version

---

## 🚀 نصب و راه‌اندازی

### ۱. کلون کردن مخزن
ابتدا مخزن را روی سیستم خود کلون کنید:

git clone https://github.com/zahramadmalil/sqlalchemy.git
cd sqlalchemy

### ۲. ساخت محیط مجازی (توصیه می‌شود)
برای جلوگیری از تداخل کتابخانه‌ها، یک محیط مجازی بسازید:

**در لینوکس / مک:**
python -m venv venv
source venv/bin/activate

**در ویندوز:**
python -m venv venv
venv\Scripts\activate

### ۳. نصب وابستگی‌ها
کتابخانه SQLAlchemy را نصب کنید:

pip install sqlalchemy

یا اگر فایل `requirements.txt` را دارید:
pip install -r requirements.txt

---

## 🎯 نحوه استفاده

هر فایل را می‌توانید به صورت مستقل اجرا کنید. پیشنهاد می‌شود هر فایل را در پوشه مربوط به خودش (مثلاً `tamrin1` یا `tamrin2`) قرار دهید و از داخل آن پوشه اجرا کنید:

python app1.py
python app2.py

> 💡 **نکته:** اگر فایل را چندین بار اجرا کنید، ممکن است رکوردهای تکراری در دیتابیس ایجاد شود. برای شروع مجدد، کافی است فایل `.db` مربوطه را حذف کنید تا از نو ساخته شود.

---

## 📘 مستندات فایل ۱: `app1.py` — مبانی و CRUD (ماشین و مشتری)

### 🎓 چه چیزی یاد می‌گیرید؟
این فایل پایه و اساس کار با SQLAlchemy را آموزش می‌دهد. شما یاد می‌گیرید چطور یک دیتابیس بسازید، جدول تعریف کنید و عملیات پایه را انجام دهید.

### 🗂️ ساختار جداول
- **جدول `carsinfo` (مدل `Car`):** شامل ستون‌های `id`, `brand`, `model`, `price`, `quantity`.
- **جدول `customer` (مدل `Customer`):** شامل ستون‌های `id`, `name`, `address`, `mobile`, `price`.

### 💻 نمونه کدهای آموزش‌داده‌شده

**۱. ایجاد جدول:**
class Car(Base):
    __tablename__ = 'carsinfo'
    id = Column(INTEGER, primary_key=True)
    brand = Column(String, nullable=False)
    # ...

**۲. کوئری‌های مختلف:**
# گرفتن همه ماشین‌ها
cars_obj = sessionlocal.query(Car).all()

# فیلتر بر اساس یک شرط خاص (قیمت بیشتر از ۱۵۰۰)
car_temp = sessionlocal.query(Car).filter(Car.price > 1500).all()

# جستجو با LIKE (مدل‌هایی که با AMG شروع می‌شوند)
car_temp = sessionlocal.query(Car).filter(Car.model.like('AMG%')).all()

**۳. به‌روزرسانی و حذف:**
# تغییر برند
car_temp.brand = 'AUDI'
sessionlocal.commit()

# حذف رکورد
sessionlocal.delete(car_temp)
sessionlocal.commit()

---

## 📗 مستندات فایل ۲: `app2.py` — رابطه یک‌به‌چند (ماشین و مشتری)

### 🎓 چه چیزی یاد می‌گیرید؟
در این فایل، شما یاد می‌گیرید چطور دو جدول را به هم متصل کنید. یک مشتری می‌تواند چندین ماشین داشته باشد (رابطه یک‌به‌چند).

### 🗂️ ساختار جداول
- **جدول `customerinfo` (مدل `Customer`):** شامل `id`, `name`, `address`, `mobile_number`.
- **جدول `carsinfo` (مدل `Car`):** شامل `id`, `brand`, `model`, `price`, `quantity` و **کلید خارجی `customer_id`** که به جدول مشتری متصل است.

### 🔗 نحوه تعریف رابطه
class Car(Base):
    customer_id = Column(INTEGER, ForeignKey('customerinfo.id'))
    customers = relationship('Customer', back_populates='owner')

class Customer(Base):
    owner = relationship('Car', back_populates='customers')

### 💡 دسترسی به داده‌ها از طریق رابطه
به لطف `relationship`، می‌توانید بدون نوشتن کوئری‌های پیچیده، به اطلاعات مرتبط دسترسی داشته باشید:
customer1 = sessionLocal.query(Customer).first()

# گرفتن همه ماشین‌های یک مشتری
for car in customer1.owner:
    print(car.brand, car.model)

# گرفتن مشخصات مشتری از روی ماشین
car1 = sessionLocal.query(Car).first()
print(car1.customers.name)

---

## 📙 مستندات فایل ۳: `app1.py` — CRUD کامل با خروجی زیبا (دانش‌آموز)

### 🎓 چه چیزی یاد می‌گیرید؟
این فایل یک مثال تمیز و مرحله‌به‌مرحله از یک سیستم مدیریت دانش‌آموز است که خروجی‌های آن با فرمت زیبا در ترمینال چاپ می‌شود.

### 🗂️ ساختار جدول
- **جدول `students` (مدل `Student`):** شامل `id`, `name`, `score`.

### 🎨 خروجی نمونه
========== CREATE ==========
3 دانش‌آموز اضافه شد.

========== READ (All) ==========
1 | Ali | 18.5
2 | Sara | 19.75
3 | Reza | 15.0

========== UPDATE ==========
دانش‌آموز با id=1 به‌روزرسانی شد: <Student(id=1, name='Ali Ahmadi', score=20.0)>

========== DELETE ==========
دانش‌آموز با id=3 حذف شد.

========== FINAL STATE ==========
1 | Ali Ahmadi | 20.0
2 | Sara | 19.75

### 💡 نکته کلیدی: `__repr__`
def __repr__(self):
    return f"<Student(id={self.id}, name='{self.name}', score={self.score})>"

با تعریف این متد، وقتی یک شیء را در کنسول چاپ می‌کنید، به جای یک آدرس حافظه نامفهوم، اطلاعات مفید آن نمایش داده می‌شود.

---

## 📕 مستندات فایل ۴: `app2.py` — روابط پیشرفته + Cascade (دانش‌آموز و درس)

### 🎓 چه چیزی یاد می‌گیرید؟
این فایل پیشرفته‌ترین بخش پروژه است. در اینجا رابطه بین دانش‌آموز و درس‌ها را می‌بینیم و با مفهوم مهم **حذف آبشاری** آشنا می‌شوید.

### 🗂️ ساختار جداول
- **جدول `students` (مدل `Student`):** شامل `id`, `name`.
- **جدول `courses` (مدل `Course`):** شامل `id`, `title`, `unit` و کلید خارجی `student_id`.

### 🔗 تعریف رابطه با Cascade
class Student(Base):
    courses = relationship(
        'Course',
        back_populates='student',
        cascade='all, delete-orphan'
    )

### 🎯 مفهوم Cascade Delete چیست؟
وقتی یک دانش‌آموز را حذف می‌کنید، به لطف `cascade='all, delete-orphan'`، تمام درس‌های مرتبط با او نیز **به طور خودکار حذف می‌شوند**. این کار از باقی ماندن داده‌های یتیم (Orphan) در دیتابیس جلوگیری می‌کند.

sara = session.query(Student).filter_by(name='Sara Rezaei').first()
session.delete(sara)
session.commit()
# تمام درس‌های Sara نیز حذف می‌شوند

---

## 🗂️ ساختار پیشنهادی پروژه

sqlalchemy-learning-project/
│
├── tamrin1/                   # تمرین اول: ماشین و مشتری
│   ├── app1.py                # مبانی SQLAlchemy و CRUD
│   └── app2.py                # رابطه یک‌به‌چند
│
├── tamrin2/                   # تمرین دوم: دانش‌آموز و درس
│   ├── app1.py                # CRUD کامل با خروجی زیبا
│   └── app2.py                # روابط پیشرفته + Cascade
│
├── requirements.txt           # وابستگی‌های پروژه
├── README.md                  # همین فایل
├── LICENSE                    # مجوز پروژه
└── .gitignore                 # فایل‌های نادیده‌گرفته‌شده

> 💡 **نکته:** فایل‌های دیتابیس (مثل `CarData.db` و `StudentData.db`) به صورت خودکار در اولین اجرا ساخته می‌شوند. پیشنهاد می‌شود آن‌ها را در فایل `.gitignore` قرار دهید تا در گیت‌هاب آپلود نشوند.

---

## 🧠 مفاهیم کلیدی آموزش‌داده‌شده

<details>
<summary><b>🔹 ۱. ORM چیست و چه مزیتی دارد؟</b></summary>
ORM مخفف Object-Relational Mapping است. به جای نوشتن دستورات خام SQL مثل `SELECT * FROM students`، شما با کلاس‌ها و اشیاء پایتون کار می‌کنید. این کار باعث افزایش امنیت و خوانایی کد می‌شود.
</details>

<details>
<summary><b>🔹 ۲. ایجاد Session و انجام عملیات</b></summary>
Session مثل یک پنجره ارتباطی با دیتابیس است. تغییرات را در Session جمع می‌کنیم و سپس با `commit()` آن‌ها را ذخیره می‌کنیم.

Session = sessionmaker(bind=engine)
session = Session()
session.add(car1)
session.commit()

</details>

<details>
<summary><b>🔹 ۳. انواع کوئری‌ها</b></summary>

# همه رکوردها
cars = session.query(Car).all()

# فیلتر ساده با filter_by
bmw = session.query(Car).filter_by(brand='BMW').all()

# فیلتر شرطی با filter
expensive = session.query(Car).filter(Car.price > 1500).all()

# جستجو با LIKE
amg = session.query(Car).filter(Car.model.like('AMG%')).all()

# اولین نتیجه
first_car = session.query(Car).first()

</details>

<details>
<summary><b>🔹 ۴. سفارشی‌سازی خروجی با <code>__repr__</code></b></summary>

def __repr__(self):
    return f"<Student(id={self.id}, name='{self.name}', score={self.score})>"

</details>

---

## 🐛 عیب‌یابی رایج (Troubleshooting)

| مشکل | راه‌حل |
|------|--------|
| `ModuleNotFoundError: No module named 'sqlalchemy'` | کتابخانه نصب نشده است. دستور `pip install sqlalchemy` را اجرا کنید. |
| رکوردهای تکراری در دیتابیس | هر بار که فایل را اجرا می‌کنید، رکوردهای جدید اضافه می‌شوند. فایل `.db` را حذف کنید تا دیتابیس از نو ساخته شود. |
| `OperationalError: no such table` | مطمئن شوید که خط `Base.metadata.create_all(engine)` در کد شما اجرا می‌شود. |
| `UNIQUE constraint failed` | در حال تلاش برای درج رکوردی با شناسه (id) تکراری هستید. دیتابیس را پاک کنید. |

---

## ❓ سوالات متداول (FAQ)

**۱. آیا نیاز به نصب دیتابیس خاصی مثل MySQL دارم؟**
خیر، در این پروژه از **SQLite** استفاده شده است که یک دیتابیس فایلی و سبک است و به صورت پیش‌فرض همراه پایتون نصب می‌شود.

**۲. چرا نام فایل‌ها تکراری است؟**
این پروژه از دو تمرین جداگانه تشکیل شده است. پیشنهاد می‌کنیم فایل‌های هر تمرین را در پوشه‌های مجزا (مثل `tamrin1` و `tamrin2`) قرار دهید تا هنگام اجرا دچار تداخل نشوید.

**۳. چگونه کدهای کامنت‌شده را تست کنم؟**
کافی است علامت `#` را از ابتدای خطوط مورد نظر بردارید و فایل را دوباره اجرا کنید تا نتیجه آن کوئری را ببینید.

---

## 🤝 مشارکت

از مشارکت شما در این پروژه استقبال می‌شود! برای همکاری:

1. پروژه را **Fork** کنید.
2. یک شاخه جدید بسازید: `git checkout -b feature/amazing-feature`
3. تغییرات خود را **Commit** کنید: `git commit -m "Add some amazing feature"`
4. شاخه را **Push** کنید: `git push origin feature/amazing-feature`
5. یک **Pull Request** باز کنید 🎉

---

## 📚 منابع پیشنهادی

- 📘 [مستندات رسمی SQLAlchemy](https://docs.sqlalchemy.org/)
- 📗 [آموزش SQLite](https://www.sqlite.org/docs.html)
- 📕 [Python ORM Tutorial](https://docs.python.org/3/)
- 📙 [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)

---

## 📄 مجوز

این پروژه تحت مجوز **MIT** منتشر شده است. برای اطلاعات بیشتر فایل [LICENSE](LICENSE) را مطالعه کنید.

---

## 👨‍💻 نویسنده

**زهرا مدملیل**
- GitHub: [@zahramadmalil](https://github.com/zahramadmalil)

---

<div align="center">

### ⭐ اگر این پروژه برایتان مفید بود، به آن ستاره بدهید! ⭐

ساخته شده با ❤️ و Python

</div>
