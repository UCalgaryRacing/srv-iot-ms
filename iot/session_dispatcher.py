# Copyright Schulich Racing FSAE
# Written By Justin Tijunelis

from iot.app import app
from flask import request
from iot.auth import require_api_key
from iot.session_coordinator import SessionCoordinator

class SessionDispatcher:
  def __init__(self):
    self.session_coordinators = {}

  # http://localhost:5000/iot/1/

  @app.route('/iot/<string:serial_number>/start', methods=['POST'])
  @require_api_key
  def start_session(self, key, serial_number):
    new_session = SessionCoordinator(self, key, serial_number, request.remote_addr)
    self.session_coordinators[serial_number] = new_session
    return 200 

  def stop_session(self, serial_number):
    self.session_coordinators.pop(serial_number)