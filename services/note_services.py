from flask import request, render_template
from flask_login import current_user
from models.db_models import Note
from settings.settings_db import db


class NoteServices():

    @staticmethod
    def new_reminder():
        if request.method == 'POST':
            notes = request.form.get("remider-div")
            date = request.form.get("date")
            reminder = Note(note = notes, setDate = date, user_id = current_user.id)
            db.session.add(reminder)
            db.session.commit()
        return render_template("home.html", user=current_user)

    @staticmethod
    def delete_reminder():
        if request.method == 'POST':
            deletebutton = request.form.get("delete") #need to create a button to delete
            noteId = deletebutton["noteId"]
            note = Note.query.get(noteId)
            if note:
                if note.user_id == current_user.id:
                    db.session.delete(note)
                    db.session.commit()
        return render_template("home.html", user=current_user)
    
    @staticmethod
    def get_all_notes():
        return Note.query.get(Note.note).all()

    @staticmethod
    def get_next_note():
        return Note.query.get(Note.note).filter_by(Note.date).first()