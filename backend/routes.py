from flask import current_app as app, request, jsonify, make_response
from flask_security import auth_required, hash_password, verify_password
from backend.models import *

datastore = app.security.datastore

@app.route("/protected", methods=['POST'])
@auth_required()
def protected():
    return "Protected Route"

@app.route('/', methods=['GET'])
def home():
    return "<h3> Backend App or Api app Running Fine.</h3>"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get('email').strip()
    password = data.get('password').strip()

    if not email or not password:
        return jsonify({"message": "Invalid input"}), 404

    user = datastore.find_user(email=email)
    
    if not user:
        return jsonify({"message": "User not found"}), 404

    if verify_password(password, user.password):
        return jsonify({"token": user.get_auth_token(), "email": user.email, "role": user.roles[0].name, "id": user.id}), 200
    
    return jsonify({"message": "Incorrect Password"}), 401

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    email = data.get('email')
    f_name = data.get('first_name')
    l_name = data.get('last_name', None)
    gender = data.get('gender', None)
    dob = data.get('dob')
    bio = data.get('bio', None)
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    missing_fields = []
    if not email:
        missing_fields.append("email")
    if not f_name:
        missing_fields.append("first_name")
    if not dob:
         missing_fields.append("dob")
    if not password:
        missing_fields.append("password")
    if not confirm_password:
        missing_fields.append("confirm_password")

    if missing_fields:
        return make_response(jsonify({
            "status": "failure",
            "message": "Missing required fields.",
            "missing_fields": missing_fields,
        }), 400)

    # Parse date in dd-mm-yyyy format
    try:
        dob = datetime.strptime(data['dob'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Use yyyy-mm-dd"}), 400


    # Check if password and confirm password match
    if password != confirm_password:
        return make_response(jsonify({
            "status": "failure",
            "message": "Password and confirm password do not match.",
        }), 400)

    try:
        if not datastore.find_user(email=email):
            # Create the user
            user = datastore.create_user(email=email, password=hash_password(password), roles=['User'])
            
            # Create and assign UserDetail
            user.user_detail = UserDetail(
                first_name=f_name,
                last_name=l_name,
                dob=dob,
                bio=bio,
                gender=gender
            )
            db.session.add(user)
        else:
            return jsonify({"message": "User Already Exists."}), 409
        db.session.commit()
        return jsonify({"message": "User Created."}), 200
    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({"message":str(e)}), 500