"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from app.forms import PropertyForm
from app import app, db, login_manager
from flask_login import login_user, logout_user, current_user, login_required
from app.models import Property
from werkzeug.utils import secure_filename


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route("/properties/create", methods=['POST', 'GET'])
def createProperty():
    form = PropertyForm()
    if form.validate_on_submit():
        title = form.title.data
        numBedrooms = form.numBedrooms.data
        numBathrooms = form.numBathrooms.data
        location = form.location.data
        price = form.price.data
        propertyType = form.propertyType.data
        description = form.description.data
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        newProperty =  Property( title=title, numBedrooms=numBedrooms, numBathrooms=numBathrooms,
                                location=location, price=price, propertyType=propertyType,
                                description=description, photo=filename)
        db.session.add(newProperty)
        db.session.commit()
        flash('Property added successfully', 'success')
        return redirect(url_for('listProperties'))
    return render_template("create_property.html", form=form)

@app.route("/properties")
def listProperties():
    properties = db.session.execute(db.select(Property)).scalars()
    return render_template("properties_list.html", properties = properties)

@app.route("/properties/<propertyRequested>")
def getProperty(propertyRequested):
    query = db.select(Property).filter_by(id = propertyRequested)
    propertyRequested = db.session.execute(query).scalar_one()
    return render_template("property_details.html", propertyRequested = propertyRequested)


@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(UserProfile).filter_by(id=id)).scalar()

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
