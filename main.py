import os
from flask import Flask, render_template, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from flask import send_from_directory
from image_detector import image_detector

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, static_folder='templates')
app.config['SECRET_KEY'] = 'APP_SECRET_KEY'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'uploads')

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)


class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, 'Image only!'), FileRequired('File was empty!')])
    submit = SubmitField('Upload')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        image_height, image_width, transform_img, result, score = image_detector(form.photo.data)
        filename = transform_img
        file_url = url_for('download_file', name=filename)
        return render_template('index.html',
                               form=form,
                               file_url=file_url,
                               image_height=image_height,
                               image_width=image_width,
                               result=result,
                               score=score)
    else:
        file_url = None
        return render_template('index.html', form=form, file_url=file_url)


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOADED_PHOTOS_DEST"], name)


if __name__ == '__main__':
    app.run()
