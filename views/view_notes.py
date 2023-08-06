from viewhome import views
from flask_login import login_required
from services.note_services import NoteServices


@views.route('/home', methods=['GET', 'POST'])
def new_reminders():
        return NoteServices.new_reminder()

@views.route('/home/delete-note', methods=['GET', 'DELETE'])
def delete_note():
        return NoteServices.delete_reminder()

@views.route('/home/all-reminders')
def get_notes():
        return NoteServices.get_all_notes()

@views.route('/home/next-reminder')
def next_reminder():
        return NoteServices.get_next_note()