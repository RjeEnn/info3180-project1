"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session
from flask.helpers import send_from_directory
from werkzeug.utils import secure_filename
from .forms import UploadForm
from app.models import Properties
from sqlalchemy import insert

###
# Routing for your application.
###

@app.route('/')
def home():
    buildings = Properties.query.all()
    return render_template('properties.html', buildings=buildings)


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Rojae Martin")

@app.route('/property/', methods=['POST', 'GET'])
def property():
    upload = UploadForm()

    if request.method == 'POST' and upload.validate_on_submit():
        try:
            image = request.files['img']
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            building = Properties(upload.title.data, upload.noBedrooms.data, upload.noBathrooms.data, upload.location.data, upload.price.data, upload.propertyType.data, upload.description.data, filename)
            db.session.add(building)
            db.session.commit()
            flash('Property successfully added.', 'success')
            return redirect(url_for('properties'))
        except:
            flash('Invalid Information Entered.', 'danger')

    return render_template('property.html', upload=upload)

@app.route('/get_image/<filename>')
def get_image(filename):

    root_path = os.getcwd()
    img_path = os.path.join(root_path, app.config['UPLOAD_FOLDER'])

    return send_from_directory(img_path, filename)

@app.route('/properties/')
def properties():
    buildings = Properties.query.all()

    return render_template('properties.html', buildings=buildings)

@app.route('/property/<id>')
def get_property(id):
    building = Properties.query.filter_by(id=int(id)).first()

    return render_template('housing_info.html', building=building)

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


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
