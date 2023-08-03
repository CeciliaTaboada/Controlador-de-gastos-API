from flask import request, render_template
from flask_login import current_user
from models.db_models import Note
from settings.settings_db import db
from datetime import datetime
import pandas as pd


class NoteServices():

    def new_reminder():
        if request.method == 'POST':
            notes = request.form.get("remider-div")
            date = request.form.get("date")
            reminder = Note(note = notes, setDate = date, user_id = current_user.id)
            db.session.add(reminder)
            db.session.commit()
        return render_template("home.html", user=current_user)

    def delete_reminder():
        if request.method == 'POST':
            delete_button = request.form.get("delete") #need to create a button to delete
            get_note = request.form.get("note") #need to create this div
            if delete_button:
                note = db.session.execute(db.select(Note).where(Note.note == get_note))
                if note.user_id == current_user.id:
                    db.session.delete(note)
                    db.session.commit()
        return render_template("home.html", user=current_user)
    
    @staticmethod
    def get_all_notes():
        all_notes = db.session.execute(db.select(Note).order_by(Note.setDate).where(Note.user_id == current_user.id)).scalars()
        #df = pd.DataFrame(all_notes)
        return all_notes

    @staticmethod
    def get_next_note():
        next_note = db.session.execute(db.select(Note).order_by(Note.setDate).where(Note.user_id==current_user.id and Note.setDate > datetime.now()).first())
        return next_note