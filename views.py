from django import forms
from django.shortcuts import render

# Define StudentForm directly in views.py
class StudentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    dob = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(label="Address", widget=forms.Textarea)
    contact = forms.CharField(label="Contact Number", max_length=15)
    email = forms.EmailField(label="Email ID")
    english_marks = forms.IntegerField(label="English Marks", min_value=0, max_value=100)
    physics_marks = forms.IntegerField(label="Physics Marks", min_value=0, max_value=100)
    chemistry_marks = forms.IntegerField(label="Chemistry Marks", min_value=0, max_value=100)

# View to handle form submission
def student_form(request):
    details = ""
    percentage = ""

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            dob = form.cleaned_data['dob']
            address = form.cleaned_data['address']
            contact = form.cleaned_data['contact']
            email = form.cleaned_data['email']
            english_marks = form.cleaned_data['english_marks']
            physics_marks = form.cleaned_data['physics_marks']
            chemistry_marks = form.cleaned_data['chemistry_marks']

            total_marks = english_marks + physics_marks + chemistry_marks
            percentage = round(total_marks / 3, 2)

            details = f"""
            <strong>Name:</strong> {name}<br>
            <strong>Date of Birth:</strong> {dob}<br>
            <strong>Address:</strong> {address}<br>
            <strong>Contact:</strong> {contact}<br>
            <strong>Email:</strong> {email}<br>
            <strong>Marks:</strong> English - {english_marks}, Physics - {physics_marks}, Chemistry - {chemistry_marks}<br>
            """

    else:
        form = StudentForm()

    return render(request, 'student_form.html', {'form': form, 'details': details, 'percentage': percentage})
