#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar
import cgi

def build_page(original_textarea, encrypt_textarea, rotation):
    title = "<h1>Enter your message into Web Caesar:</h1>"
    input_rotation = "<label><strong>Enter a rotation number: </strong></br><input type='number' name='rotation' value='{}'></label>".format(rotation)
    original_textarea = "<label><strong>Enter in your message: </strong></br> <textarea name='original_message' rows='8' cols='55'>" + original_textarea + "</textarea></label>"
    encrypt_textarea = "<label><strong>Encrypted message: </strong></br> <textarea name='encrypt_message' rows='8' cols='55'>" + encrypt_textarea + "</textarea></label>"

    table = "<table><tr><td>" + original_textarea + "</td><td>" + encrypt_textarea + "</td></tr></table>"

    submit = "<input type='submit'/>"
    form = "<form method='post'>" + input_rotation + "</br></br>" + table + "</br></br>" + submit + "</form>"
    content = title + form
    return content

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("", "","")
        self.response.write(content)

    def post(self):
        original_message = ""
        rotation = 0

        if self.request.get("original_message") != "":
            original_message = self.request.get("original_message")

        if self.request.get("rotation") != "":
            rotation = int(self.request.get("rotation"))
        encrypted_message = caesar.encrypt(original_message, rotation)
        escaped_message = cgi.escape(encrypted_message)
        content = build_page(original_message, escaped_message, int(rotation))

        self.response.write(content)
        # self.response.write("<strong>Secret Message: </strong>" + encrypted_message)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
