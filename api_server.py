#! /usr/share/python3 

from flask import Flask, request, jsonify

app = Flask(__name__)

local_database = []

def did_generate(data):

    username = data['username']
    location = data['location']
    email = data['email']

    did = ""
    concat = username + location + email
    for i in range(len(concat)):
        index = (i + len(concat)) / 2
        if (concat[int(index)] != '@' or concat[int(index)] != '.'):
            did = did + concat[int(index)]

    add_num = ((len(concat) * 33) + 427) / 2
    did = did + str(int(add_num))
    local_database.append(did)
    print(local_database)

    return did

@app.route('/create_did', methods=['POST'])
def create_did():
    try:
        data = request.get_json()
        did = did_generate(data)
        return jsonify({'status': "success", "did": did})

    except Exception as e:
        print(str(e))
        return jsonify({'status': 'failed'})

@app.route('/verify', methods=['POST'])
def verification():
    try:
        data = request.get_json()
        did = data['did']
        if did in local_database:
            return jsonify({'status': 'success', 'signal': 'verified'})
        return jsonify({'status': 'success', 'signal': 'unverified'})
        
    except Exception as e:
        print(str(e))
        return jsonify({'status': 'failed'})

'''
{
    'username': 'Aditya',
    'location': 'India',
    'email': 'adityapatil24680@gmail.com'
}

{
    'did': 'kf8j76fhj98fh7a79d8jfh454dha87h5f4jd3h54jfs67hd36563ksdjf22hs'
}
'''
