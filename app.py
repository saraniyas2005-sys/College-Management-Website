import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from wtforms.validators import DataRequired
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from flask import send_from_directory
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from models import Review
from datetime import datetime
from flask import Flask, render_template, request
from flask import Flask, request, redirect, url_for, jsonify
from models import db, Announcement  # Update with your actual model import
from models import ContactMessage
from models import db 
import re



app = Flask(__name__)


@app.route('/faq', methods=['GET', 'POST'])
def faq():
    answer = ""
    if request.method == 'POST':
        user_input = request.form['question'].lower()

        if "admission" in user_input:
            answer = ("Admissions are open from June to August every year. "
                      "You can apply online through our college website or visit the admission office for guidance. "
                      "Required documents include your previous mark sheets, ID proof, and passport-sized photos.")

        elif "exam" in user_input or "examination" in user_input:
            answer = ("Exams are conducted at the end of each semester, usually in November and April. "
                      "The exam timetable is published on the notice board and online. "
                      "Make sure to check the academic calendar and prepare accordingly.")

        elif "library" in user_input:
            answer = ("The college library is open Monday to Friday from 9 AM to 6 PM, and on Saturdays till 2 PM. "
                      "We offer access to thousands of books, journals, and online research databases. "
                      "You can also borrow up to 5 books at a time for 2 weeks.")

        elif "courses" in user_input or "subjects" in user_input:
            answer = ("We offer undergraduate courses in Science, Commerce, and Arts streams. "
                      "Popular courses include B.Sc, B.Com, B.A, BCA, and BBA. "
                      "Subjects include Physics, Chemistry, Mathematics, Economics, History, Computer Science, and more. "
                      "Detailed syllabus and course structure are available on the courses page.")

        elif "fees" in user_input or "fee structure" in user_input:
            answer = ("The fee structure varies by course and category (general, SC/ST, OBC). "
                      "Tuition fees range from INR 10,000 to 30,000 per semester. "
                      "Additional fees include library, lab, and exam fees. "
                      "Scholarships and fee concessions are available for eligible students.")

        elif "contact" in user_input or "phone" in user_input or "email" in user_input:
            answer = ("You can contact the college office at +91-1234567890 or email us at info@stannescollege.edu. "
                      "Office hours are 9 AM to 5 PM on weekdays.")

        elif "hostel" in user_input or "accommodation" in user_input:
            answer = ("The college provides separate hostels for boys and girls with well-furnished rooms, mess facilities, and 24/7 security. "
                      "Hostel applications are submitted after admission and are subject to availability.")

        elif "sports" in user_input or "games" in user_input:
            answer = ("We have excellent sports facilities including cricket, basketball, badminton courts, and a gymnasium. "
                      "Students can join various sports clubs and participate in inter-college tournaments.")

        elif "placement" in user_input or "career" in user_input:
            answer = ("Our placement cell assists students with internships and job placements. "
                      "We conduct training sessions, resume workshops, and invite top companies for campus recruitment every year.")

        elif "scholarship" in user_input or "financial aid" in user_input:
            answer = ("Scholarships are offered based on merit and need. "
                      "You can apply through the scholarship office with required documents. "
                      "Check the website for application deadlines and eligibility criteria.")

        elif "faculty" in user_input or "teachers" in user_input:
            answer = ("Our faculty members are highly qualified with many holding PhDs and having extensive teaching experience. "
                      "You can find faculty details on the staff directory on our website.")

        elif "transport" in user_input or "bus" in user_input:
            answer = ("The college runs a fleet of buses covering major routes across the city. "
                      "Bus passes can be obtained from the transport office after admission.")

        elif "timings" in user_input or "class schedule" in user_input:
            answer = ("Classes run from Monday to Friday, 9 AM to 4 PM with breaks in between. "
                      "The detailed timetable is available on the student portal.")

        elif "internship" in user_input:
            answer = ("We encourage internships as part of the curriculum. "
                      "The placement cell helps students find suitable internship opportunities in reputed companies.")

        elif "cafeteria" in user_input or "canteen" in user_input:
            answer = ("Our cafeteria offers a variety of healthy and affordable meals and snacks. "
                      "It is open throughout the college hours with hygienic facilities.")

        elif "events" in user_input or "fest" in user_input or "cultural" in user_input:
            answer = ("The college hosts annual cultural and sports festivals, workshops, and seminars. "
                      "Keep an eye on the events calendar on the website or notice board.")

        elif "attendance" in user_input:
            answer = ("Attendance is mandatory and is regularly monitored. "
                      "Students must maintain at least 75% attendance to be eligible for exams.")

        elif "results" in user_input or "marks" in user_input:
            answer = ("Exam results are published online on the student portal approximately 4-6 weeks after exams. "
                      "You will need your student ID and password to access the results.")

        elif "advising" in user_input or "counseling" in user_input:
            answer = ("Academic and career counseling services are available for students. "
                      "You can book an appointment with our counselor through the student services office.")

        elif "registration" in user_input or "enrollment" in user_input:
            answer = ("Registration for each semester happens online via the student portal. "
                      "You will receive notifications about registration dates and procedures.")

        elif "exam syllabus" in user_input or "syllabus" in user_input:
            answer = ("Syllabi for all courses and semesters are available on the college website under the academics section. "
                      "Please download the latest version for your course.")

        elif "holiday" in user_input or "vacation" in user_input:
            answer = ("The college calendar includes winter holidays in December, summer holidays in May-June, and other national holidays. "
                      "Check the official academic calendar for exact dates.")

        elif "placement eligibility" in user_input:
            answer = ("To be eligible for campus placements, students must have cleared all subjects and maintained good academic standing. "
                      "Check placement cell guidelines for more details.")

        elif "grading system" in user_input:
            answer = ("The college follows a semester-based grading system with letter grades A, B, C, D, and F. "
                      "Grade point averages (GPA) are calculated each semester.")

        elif "contact faculty" in user_input or "email faculty" in user_input:
            answer = ("You can contact faculty members via email addresses listed on the staff directory page on the college website.")

        elif "online classes" in user_input or "virtual classes" in user_input:
            answer = ("Due to recent events, online classes are conducted via Zoom and Google Meet. "
                      "Links are shared by the respective departments.")

        elif "research" in user_input:
            answer = ("Our college encourages research activities and provides facilities and funding for student projects. "
                      "Contact the research department for more information.")

        elif "student clubs" in user_input or "societies" in user_input:
            answer = ("There are several student clubs including debate, drama, music, robotics, and entrepreneurship. "
                      "You can join clubs during the orientation week or contact the student affairs office.")

        elif "library timings" in user_input:
            answer = ("The library is open from 9 AM to 6 PM on weekdays and 9 AM to 2 PM on Saturdays.")

        elif "technical support" in user_input or "it help" in user_input:
            answer = ("For technical assistance, contact the IT helpdesk at ithelp@stannescollege.edu or call +91-9876543210.")

        else:
            answer = ("Sorry, I don't have the answer to that. "
                      "Please contact the college office for more information or check our website's FAQ section.")

    return render_template('faq.html', answer=answer)


# Configure file upload settings
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Add your secret key here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///college.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# ------------------ MODELS ------------------
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    venue = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    poster = db.Column(db.String(300), nullable=True)  # To store poster image URL

# models.py or inside your app file if it's small
class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    duration = db.Column(db.String(50), nullable=False)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_submitted = db.Column(db.DateTime, default=datetime.utcnow)



# ------------------ FORMS ------------------
class EventForm(FlaskForm):
    name = StringField('Event Name', validators=[DataRequired()])
    description = TextAreaField('Event Description', validators=[DataRequired()])
    date = StringField('Event Date (YYYY-MM-DD)', validators=[DataRequired()])
    venue = StringField('Event Venue', validators=[DataRequired()])
    type = StringField('Event Type', validators=[DataRequired()])
    poster = FileField('Event Poster')

class ReviewForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    role = SelectField('Your Role', choices=[('Student','Student'), ('Alumni','Alumni'), ('Faculty','Faculty'), ('Parent','Parent')], validators=[DataRequired()])
    rating = IntegerField('Rating (1-5)', validators=[DataRequired(), NumberRange(min=1, max=5)])
    message = TextAreaField('Your Review', validators=[DataRequired()])

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    message = db.Column(db.Text, nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)



# ------------------ ROUTES ------------------
@app.route('/admin/reviews/')
def admin_reviews():
    reviews = Review.query.order_by(Review.date_submitted.desc()).all()
    return render_template('admin_reviews.html', reviews=reviews)




# ------------------ ROUTES ------------------

@app.route('/')
def welcome():
    return render_template('first.html')

@app.route('/index/')
def index():
    return render_template('index.html')

# REVIEW PAGES
@app.route('/review/', methods=['GET', 'POST'])
def review():
    form = ReviewForm()
    if form.validate_on_submit():
        new_review = Review(
            name=form.name.data,
            role=form.role.data,
            rating=form.rating.data,
            message=form.message.data
        )
        db.session.add(new_review)
        db.session.commit()
        flash('Thank you for your review!', 'success')
        return redirect(url_for('review_submitted'))
    return render_template('review.html', form=form)


@app.route('/review-submitted/')
def review_submitted():
    return render_template('submit_review.html')

@app.route('/reviews/')
def all_reviews():
    reviews = Review.query.order_by(Review.date_submitted.desc()).all()
    return render_template('all_reviews.html', reviews=reviews)

# ------------------ RUN ------------------




# ------------------ ADMIN LOGIN ------------------

hashed_password = generate_password_hash("stannes@123", method='pbkdf2:sha256')

@app.route("/admin", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and check_password_hash(hashed_password, password):
            return redirect(url_for("admin_dashboard"))  # Only redirect if login is successful
        else:
            error = "Invalid credentials. Please try again."
    return render_template("login.html", error=error)

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        # TODO: Handle email lookup and send reset link
        flash('Password reset link sent to your email.', 'info')
        return redirect(url_for('login'))
    return render_template('forgot_password.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    event_count = Event.query.count()
    announcement_count = Announcement.query.count()
    contact_message_count = ContactMessage.query.count()
    review_count = Review.query.count()  # ✅ Add review count

    return render_template('dashboard.html',
                           event_count=event_count,
                           announcement_count=announcement_count,
                           contact_message_count=contact_message_count,
                           review_count=review_count)  # ✅ Pass it to template




# ------------------ EVENT HANDLING ------------------
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/admin/add_event', methods=['GET', 'POST'])
def add_event():
    form = EventForm()
    if form.validate_on_submit():
        # Get form data
        name = form.name.data
        description = form.description.data
        date_str = form.date.data  # The date is in the 'DD-MM-YYYY' format
        venue = form.venue.data
        event_type = form.type.data
        poster = form.poster.data

        # Convert the string date to a datetime object
        event_date = datetime.strptime(date_str, '%d-%m-%Y').date()  # Change format to '%d-%m-%Y'

        # Save the poster image if available
        if poster and allowed_file(poster.filename):
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])  # Create directory if not exists

            filename = secure_filename(poster.filename)
            poster.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # Save image in static/uploads folder

            # Save event details to database, including the relative path to the image
            event = Event(name=name, description=description, date=event_date, venue=venue,
                          type=event_type, poster=f'uploads/{filename}')
            db.session.add(event)
            db.session.commit()

            flash('Event added successfully!', 'success')
            return redirect(url_for('view_all_events'))

    return render_template('add_event.html', form=form)

@app.route('/view_all_events')
def view_all_events():
    events = Event.query.all()  # Get all events from the database
    return render_template('view_all_events.html', events=events)

@app.route('/delete_event/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return '', 204
@app.route('/edit_event/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)
    form = EventForm(obj=event)

    if form.validate_on_submit():
        # Get form data
        name = form.name.data
        description = form.description.data
        date_str = form.date.data  # e.g. '14-05-2025'
        venue = form.venue.data
        event_type = form.type.data
        poster = form.poster.data

        # ✅ Update event fields
        event.name = name
        event.description = description
        event.date = datetime.strptime(date_str, '%d-%m-%Y').date()
        event.venue = venue
        event.type = event_type

        # ✅ Handle poster only if a new one is uploaded
        if poster and allowed_file(poster.filename):
            filename = secure_filename(poster.filename)
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            poster.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            event.poster = f'uploads/{filename}'

        db.session.commit()
        flash('Event updated successfully!', 'success')
        return redirect(url_for('view_all_events'))

    return render_template('edit_event.html', form=form, event=event)

@app.route('/event-user')
def view_events_user():
    events = Event.query.order_by(Event.date).all()
    return render_template('view_events_user.html', events=events)

# ------------------ STATIC PAGES ------------------


@app.route("/admin/manage_courses", methods=["GET", "POST"])
def manage_courses():
    courses = Course.query.all()
    return render_template("manage_courses.html", courses=courses)

@app.route('/admin/add_announcement', methods=['GET', 'POST'])
def add_announcement():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']          
        
        new_announcement = Announcement(title=title, content=content)
        db.session.add(new_announcement)
        db.session.commit()
        
        return redirect(url_for('view_announcements'))  # ✅ Correct endpoint here
    return render_template('add_announcement.html')

# --------------------------
# 👁️ View Announcements Route
# --------------------------
# app.py

@app.route('/recommend_form')
def recommend_form():
    return render_template('recommend_form.html')  # Render the form page

@app.route('/recommend', methods=['POST'])
def recommend():
    subject = request.form.get('subject')
    career = request.form.get('career')
    learning_style = request.form.get('learningStyle')

    recommendation = ""

    if subject == "pcmc":
        if career in ["developer", "data"]:
            recommendation = "You should consider <strong>BCA</strong> or <strong>B.Sc in Computer Science</strong>."
        elif career == "scientist":
            recommendation = "Explore <strong>B.Sc in Physics or Electronics</strong>."
    elif subject == "pcmb":
        if career == "scientist":
            recommendation = "You're perfect for <strong>B.Sc in Biotech / Microbiology</strong>."
        else:
            recommendation = "With PCMB, you're flexible. Try <strong>B.Sc</strong>, <strong>BCA</strong>, or <strong>Paramedical Courses</strong>."
    elif subject in ["cebcs", "ceba"]:
        if career == "business":
            recommendation = "Go for <strong>BBA</strong> to grow your managerial skills."
        elif career == "finance":
            recommendation = "<strong>B.Com</strong> with Finance or Accounting is ideal."
        elif career == "developer":
            recommendation = "You can also go for <strong>BCA</strong> if you took CS."
    elif subject == "arts":
        if career == "creative":
            recommendation = "You’d thrive in <strong>BA Journalism, English, or Psychology</strong>."
        elif career == "government":
            recommendation = "Choose <strong>BA in Political Science, Economics, or History</strong>."
    else:
        recommendation = "Please fill all fields to get a recommendation."

    if recommendation and learning_style:
        recommendation += f"<br><br><strong>Bonus Tip:</strong> Since you're a <em>{learning_style.replace('-', ' ')}</em> learner, look for colleges with practical projects and labs!"

    return render_template("recommend-course.html", result=recommendation)


@app.route('/announcements')
def view_announcements():
    announcements = Announcement.query.order_by(Announcement.date_posted.desc()).all()
    return render_template('view_announcements.html', announcements=announcements)

@app.route('/downloads/<filename>')
def download_file(filename):
    print(f"Attempting to download file: {filename}")
    return send_from_directory(os.path.join(app.root_path, 'static', 'downloads'), filename)


@app.route('/delete_announcement/<int:announcement_id>', methods=['POST'])
def delete_announcement(announcement_id):
    announcement = Announcement.query.get_or_404(announcement_id)
    try:
        db.session.delete(announcement)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/viewinganno')
def viewinganno():
    announcements = Announcement.query.order_by(Announcement.date_posted.desc()).all()
    return render_template('viewinganno.html', announcements=announcements)


@app.route('/achiev/')
def achiev():
    return render_template('achiev.html')

@app.route('/ba/')
def ba():
    return render_template('ba.html')



@app.route('/balec/')
def balec():
    return render_template('balec.html')

@app.route('/bba/')
def bba():
    return render_template('bba.html')

# Running the Flask app


@app.route('/bbalec/')
def bbalec(): return render_template('bbalec.html')

@app.route('/bca/')
def bca(): return render_template('bca.html')

@app.route('/bcalec/')
def bcalec(): return render_template('bcalec.html')

@app.route('/bcom/')
def bcom(): return render_template('bcom.html')

@app.route('/bcomlec/')
def bcomlec(): return render_template('bcomlec.html')

@app.route('/bsc/')
def bsc(): return render_template('bsc.html')

@app.route('/bsclec/')
def bsclec(): return render_template('bsclec.html')


@app.route('/contact', methods=['GET', 'POST'])
def submit_contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        new_message = ContactMessage(name=name, email=email, message=message)
        db.session.add(new_message)
        db.session.commit()

        flash('Your message has been sent successfully!')
        return redirect(url_for('submit_contact'))
    return render_template('contact_form.html')


@app.route('/admin_contact_messages')
def admin_contact_messages():
    messages = ContactMessage.query.order_by(ContactMessage.submitted_at.desc()).all()
    return render_template('admin_contact_messages.html', messages=messages)


@app.route('/admissio/')
def admissio(): return render_template('admissio.html')

@app.route('/campus-location/')
def campus_location(): return render_template('campus-location.html')

@app.route('/chat/')
def chat(): return render_template('chat.html')



@app.route('/course/')
def course(): return render_template('course.html')

@app.route('/cultural/')
def cultural(): return render_template('cultural.html')

@app.route('/departments/')
def departments(): return render_template('departments.html')

@app.route('/faculty/')
def faculty(): return render_template('faculty.html')


@app.route('/first/')
def first(): return render_template('first.html')

@app.route('/contact_form/')
def contact(): return render_template('contact_form.html')

@app.route('/history/')
def history(): return render_template('history.html')

@app.route('/mana/')
def mana(): return render_template('mana.html')

@app.route('/mission/')
def mission(): return render_template('mission.html')

@app.route('/place/')
def place(): return render_template('place.html')

@app.route('/pricipal/')
def pricipal(): return render_template('pricipal.html')



@app.route('/seminars/')
def seminars(): return render_template('seminars.html')

@app.route('/sports/')
def sports(): return render_template('sports.html')

@app.route('/staff/')
def staff(): return render_template('staff.html')


@app.route('/vission/')
def vission(): return render_template('vission.html')

@app.route('/workshops/')
def workshops(): return render_template('workshops.html')

# ------------------ MAIN ------------------
# ------------------ MAIN ------------------
if __name__ == '__main__':
    app.run(debug=True)
   