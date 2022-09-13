
from app import app
from flask import render_template, request, redirect
from models import providers_list
import random
from function import getProviderIndex, build_provider_obj

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

@app.route('/register')
def register():
    return render_template('register.html', title="Register")

@app.route('/login')
def login():
    return render_template('login.html', title="Login")

@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html', title="Forgot Password")


#GET ALL
@app.route('/providers')
def providers():
    return render_template('providers/providers-list.html', title="Providers", providers=providers_list)


#POST - ADD
@app.route('/providers/add-provider', methods=["GET","POST"])
def add():
    #adding provider information
    if request.method == 'POST':
        id = random.randint(100000,999999)
        provider = build_provider_obj(request, id)
        providers_list.append(provider)
        #return to provider page
        return redirect('/providers')
    
    return render_template('providers/provider-add-form.html', title="Add Provider", providers=providers_list)

#EDIT - UPDATE
@app.route('/providers/edit/<id>', methods=["GET","POST"])
#this (id) must match <id>
def edit(id):
    provider = None
    index = getProviderIndex(id, providers_list)
    if request.method == 'POST':
        provider = build_provider_obj(request, int(id))
        if index is not None:
            providers_list[index]=provider
        #return to provider page
        return redirect('/providers')
    
    if index is not None:
        provider = providers_list[index] 
    return render_template('providers/provider-edit-form.html', title="Update Provider", provider=provider, id=id)

#Delete
@app.route('/providers/delete/<id>')
def delete(id):
    index = getProviderIndex(id, providers_list)
    if index is not None:
        del providers_list[index]
    return redirect('/providers')