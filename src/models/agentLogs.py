from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AgentLogs(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    os = db.Column(db.Text)
    release = db.Column(db.Text)
    version = db.Column(db.Text)
    machine = db.Column(db.Text)
    processor = db.Column(db.Text)
    hostname = db.Column(db.Text)
    ip4 = db.Column(db.Text)
    ip6 = db.Column(db.Text)
    mac = db.Column(db.Text)
    potentially_unwanted_softwares = db.Column(db.Text)
    running_process = db.Column(db.Text)
    firewall_status = db.Column(db.Text)
    usb_status = db.Column(db.Text)
    json_data = db.Column(db.JSON())
    created_on = db.Column(db.DateTime())
    created_by = db.Column(db.Text)
    updated_on = db.Column(db.DateTime())
    updated_by = db.Column(db.Text)
