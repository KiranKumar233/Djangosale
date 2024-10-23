from django.shortcuts import render,redirect,HttpResponse
from .models import ContactForm,ClientData,NewPropertyData,NewPropertyTypeData,NewstatusData,SendEnquiry,PostReport
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')









def contactus(request):

    if request.method=="GET":
        return render(request,'contact.html')
    else:

        ContactForm(
            name = request.POST.get('contact_name'),
            email = request.POST.get('contact_email'),
            phone = request.POST.get('contact_phone'),
            message = request.POST.get('contact_message')
        ).save()
        return render(request,'contact.html')



'''
def clientdata(request):
    if request.method=="GET":
        return render(request,'registrationpage.html')
    else:


        # Create and save the Client object
        ClientData(
        client_name = request.POST.get('client_name'),
        client_login_id = request.POST.get('client_login_id'),
        client_password = request.POST.get('client_password'),
        client_confirm_password=request.POST.get('client_confirm_password'),
        client_gender = request.POST.get('client_gender'),
        client_email = request.POST.get('client_email'),
        client_number = request.POST.get('client_number'),
        client_DOB = request.POST.get('client_DOB'),
        client_address1 = request.POST.get('client_address1'),
        client_address2 = request.POST.get('client_address2'),
        client_city = request.POST.get('client_city'),
        client_state = request.POST.get('client_state'),
        client_country = request.POST.get('client_country'),

        client_picture = request.FILES.get('client_picture')  # Get the uploaded file

        ).save()
        return render(request,'homepage.html')
'''













'''
def clientdata(request):
    if request.method=="GET":
        return render(request,'registrationpage.html')
    else:

        client_name = request.POST.get('client_name')
        client_login_id = request.POST.get('client_login_id')


        if client_name and client_login_id and client_name!= client_login_id:
            return HttpResponse('please enter same username  and login id')
        else:
            client_password = request.POST.get('client_password')
            client_confirm_password=request.POST.get('client_confirm_password')

            if client_password and client_confirm_password and client_password != client_confirm_password:
                return HttpResponse('please enter same  passwordds')
            else:
                client_gender = request.POST.get('client_gender')
                client_email = request.POST.get('client_email')
                client_number = request.POST.get('client_number')

                client_DOB = request.POST.get('client_DOB')
                client_address1 = request.POST.get('client_address1')
                client_address2 = request.POST.get('client_address2')
                client_city = request.POST.get('client_city')
                client_state = request.POST.get('client_state')
                client_country = request.POST.get('client_country')

                client_picture = request.FILES.get('client_picture')

                ClientData(
                    client_name=client_name,
                    client_login_id=client_login_id,
                    client_password=client_password,
                    client_confirm_password=client_confirm_password,
                    client_gender=client_gender,
                    client_email=client_email,
                    client_number=client_number,
                    client_DOB=client_DOB,
                    client_address1=client_address1,
                    client_address2=client_address2,
                    client_city=client_city,
                    client_state=client_state,
                    client_country=client_country,
                    client_picture=client_picture
                ).save()



                my_user=User.objects.create_user(username=client_name, email=client_email, password=client_password)
                my_user.is_staff = True
                my_user.save()


                return render(request,'loginp.html')

'''
'''
def clientdata(request):
    if request.method == "GET":
        return render(request, 'registrationpage.html')
    else:
        client_name = request.POST.get('client_name')
        client_login_id = request.POST.get('client_login_id')

        if client_name and client_login_id and client_name != client_login_id:
            return HttpResponse('Please enter the same username and login id')
        else:
            client_password = request.POST.get('client_password')
            client_confirm_password = request.POST.get('client_confirm_password')

            # Check if the password meets the criteria
            if not is_valid_password(client_password):
                message='Password must contain at least one letter, one digit, and one special character. It should be at least 8 characters long.'
                return   render(request, 'registrationpage.html',{'message':message})# Adjust the URL name based on your actual URL configuration

            # Check if the passwords match
            if client_password and client_confirm_password and client_password != client_confirm_password:
                return HttpResponse('Please enter the same passwords')
            else:
                # Rest of your code for processing other form fields
                client_gender = request.POST.get('client_gender')
                client_email = request.POST.get('client_email')
                client_number = request.POST.get('client_number')

                client_DOB = request.POST.get('client_DOB')
                client_address1 = request.POST.get('client_address1')
                client_address2 = request.POST.get('client_address2')
                client_city = request.POST.get('client_city')
                client_state = request.POST.get('client_state')
                client_country = request.POST.get('client_country')

                client_picture = request.FILES.get('client_picture')

                # Save the ClientData instance
                client_data = ClientData(
                    client_name=client_name,
                    client_login_id=client_login_id,
                    client_password=client_password,
                    client_confirm_password=client_confirm_password,
                    client_gender=client_gender,
                    client_email=client_email,
                    client_number=client_number,
                    client_DOB=client_DOB,
                    client_address1=client_address1,
                    client_address2=client_address2,
                    client_city=client_city,
                    client_state=client_state,
                    client_country=client_country,
                    client_picture=client_picture

                    # ... (other fields)
                )
                client_data.save()

                # Create a user using the provided credentials
                my_user = User.objects.create_user(username=client_name, email=client_data.client_email, password=client_password)
                my_user.is_staff = True
                my_user.save()

                return render(request, 'loginp.html')

def is_valid_password(password):
    # Password validation logic using the same regex pattern
    import re
    pattern = re.compile(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[\W_]).{8,}$')
    return bool(pattern.match(password))

'''


def clientdata(request):
    if request.method == "GET":
        return render(request, 'registrationpage.html')
    else:
        client_name = request.POST.get('client_name')
        client_login_id = request.POST.get('client_login_id')

        if client_name and client_login_id and client_name != client_login_id:
            msg = 'Please enter the same username and login id'
            return render(request, 'registrationpage.html',{'msg':msg})

        if ClientData.objects.filter(client_name=client_name).exists():
            msg2= 'Client name already exists. Please choose a different client name.'
            return render(request, 'registrationpage.html',{'msg2':msg2})

        else:
            client_password = request.POST.get('client_password')
            client_confirm_password = request.POST.get('client_confirm_password')

            # Check if the password meets the criteria
            if not is_valid_password(client_password):
                message='Password must contain at least one letter, one digit, and one special character. It should be at least 8 characters long.'
                return   render(request, 'registrationpage.html',{'message':message})# Adjust the URL name based on your actual URL configuration

            # Check if the passwords match
            if client_password and client_confirm_password and client_password != client_confirm_password:
                msg3='Please enter the same passwords'
                return   render(request, 'registrationpage.html',{'msg3':msg3})

            else:
                # Rest of your code for processing other form fields
                client_gender = request.POST.get('client_gender')
                client_email = request.POST.get('client_email')
                client_number = request.POST.get('client_number')

                client_DOB = request.POST.get('client_DOB')
                client_address1 = request.POST.get('client_address1')
                client_address2 = request.POST.get('client_address2')
                client_city = request.POST.get('client_city')
                client_state = request.POST.get('client_state')
                client_country = request.POST.get('client_country')

                client_picture = request.FILES.get('client_picture')

                # Save the ClientData instance
                client_data = ClientData(
                    client_name=client_name,
                    client_login_id=client_login_id,
                    client_password=client_password,
                    client_confirm_password=client_confirm_password,
                    client_gender=client_gender,
                    client_email=client_email,
                    client_number=client_number,
                    client_DOB=client_DOB,
                    client_address1=client_address1,
                    client_address2=client_address2,
                    client_city=client_city,
                    client_state=client_state,
                    client_country=client_country,
                    client_picture=client_picture

                    # ... (other fields)
                )
                client_data.save()

                # Create a user using the provided credentials
                my_user = User.objects.create_user(username=client_name, email=client_data.client_email, password=client_password)
                my_user.is_staff = True
                my_user.save()

                return redirect('loginpage')

def is_valid_password(password):
    # Password validation logic using the same regex pattern
    import re
    pattern = re.compile(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[\W_]).{8,}$')
    return bool(pattern.match(password))












def loginpage(request):
    if request.method == 'GET':
        return render(request, 'loginp.html')
    else:
        username1 = request.POST.get('user')
        password1 = request.POST.get('pass')
        client_type = request.POST.get('client_type')

        user = authenticate(username=username1, password=password1)

        if user is not None:
            if client_type == 'Seller':
                login(request, user)
                return redirect('dashboard')
            elif client_type == 'Buyer':
                login(request, user)
                return redirect('buyerdashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'loginp.html')


def aboutpage(request):
    return render(request,'about.html')





@login_required(login_url='loginpage')
def adminhome(request):
    return render(request,'adminhme.html')



@login_required(login_url='loginpage')
def adminabout(request):
    return render(request,'adminabout.html')





@login_required(login_url='loginpage')
def dashboardpage(request):
    return render(request,'admindashboard.html')



@login_required(login_url='loginpage')
def addnewprop(request):
    if request.method == 'POST':
        seller_name = request.user.username
        property_name = request.POST.get("property-name")
        property_type = request.POST.get("property-type")
        status_name = request.POST.get("status-name")
        property_cost = request.POST.get("property-cost")
        property_size = request.POST.get("property-size")
        seller_contact_details = request.POST.get("seller-contact-details")
        email_property = request.POST.get("email-property")
        property_amenities = request.POST.get("property-amenities")
        property_specifications = request.POST.get("property-specifications")
        property_total_rooms = request.POST.get("property-total-rooms")
        property_balcony = request.POST.get("property-balcony")
        property_total_bathrooms = request.POST.get("property-total-bathrooms")
        property_address = request.POST.get("property-address")
        property_image = request.FILES.get("property-image-upload-type")
        property_description = request.POST.get("property-description")

        new_property_data = NewPropertyData(
            seller_name=seller_name,
            property_name=property_name,
            property_type=property_type,
            status_name=status_name,
            property_cost=property_cost,
            property_size=property_size,
            seller_contact_details=seller_contact_details,
            email_property=email_property,
            property_amenities=property_amenities,
            property_specifications=property_specifications,
            property_total_rooms=property_total_rooms,
            property_balcony=property_balcony,
            property_total_bathrooms=property_total_bathrooms,
            property_address=property_address,
            property_image=property_image,
            property_description=property_description
        )
        new_property_data.save()
        return render(request, 'adminhme.html')
    else:
        return render(request, 'addnewpro.html')




@login_required(login_url='loginpage')
def addnewproptype(request):

    if request.method == 'POST':
        type_name = request.POST.get("add_type_name")
        type_description = request.POST.get("add_type_description")
        seller_name = request.user.username


        if type_name and type_description and seller_name:
            NewPropertyTypeData.objects.create(
                add_type_name=type_name,
                add_type_description=type_description,
                seller_name=seller_name
            )
            return render(request, 'addnewproptype.html')

    else:

        return render(request, 'addnewproptype.html')

@login_required(login_url='loginpage')
def addstatus(request):
    if request.method == 'POST':
        sts_name = request.POST.get("Status_name")
        sts_description = request.POST.get("Status_description")
        seller_name = request.user.username

        if sts_name and sts_description and seller_name:
            NewstatusData.objects.create(
                status_name=sts_name,
                status_description=sts_description,
                seller_name = request.user.username
            )
            return render(request, 'addstatus.html')

    else:

        return render(request, 'addstatus.html')


@login_required(login_url='loginpage')
def display_properties(request):
    properties = NewPropertyData.objects.filter(seller_name=request.user.username)

    return render(request, 'propertyreport.html', {'properties': properties})


@login_required(login_url='loginpage')
def statusreports(request):

    report=NewstatusData.objects.filter(seller_name=request.user.username)
    return render(request,"statusreport.html",{'report':report})



@login_required(login_url='loginpage')
def type_report(request):
    reporttype=NewPropertyTypeData.objects.filter(seller_name=request.user.username)
    return render(request,"propertytypereport.html",{'reporttype':reporttype})




@login_required(login_url='loginpage')
def my_account(request):
    # Assuming you have a OneToOneField relationship with a custom user model
    logged_in_user = ClientData.objects.filter(client_name=request.user.username).first()

    if request.method == 'GET':
        message = "You can edit your details here."
        return render(request, 'my_account.html', {'user': logged_in_user, 'message': message})
    else:
        # Get the new client_picture from the form
        new_client_picture = request.FILES.get('client_picture')

        # Check if a new image has been provided
        if new_client_picture:
            logged_in_user.client_picture = new_client_picture

        # Update other fields
        new_client_name = request.POST['client_name']

        # Check if the new client name already exists in ClientData
        if ClientData.objects.filter(client_name=new_client_name).exclude(id=logged_in_user.id).exists():
            msg = 'Client name already exists. Please choose a different client name.'
            return render(request, 'my_account.html', {'msg': msg, 'user': logged_in_user, 'message': "You can edit your details here."})

        # Update other fields
        logged_in_user.client_name = new_client_name
        logged_in_user.client_login_id = request.POST['client_name']  # Assuming you also want to update login_id
        logged_in_user.client_gender = request.POST['client_gender']
        logged_in_user.client_email = request.POST['client_email']
        logged_in_user.client_number = request.POST['client_number']
        logged_in_user.client_address1 = request.POST['client_address1']
        logged_in_user.client_address2 = request.POST['client_address2']
        logged_in_user.client_city = request.POST['client_city']
        logged_in_user.client_state = request.POST['client_state']
        logged_in_user.client_country = request.POST['client_country']

        # Save the ClientData object
        logged_in_user.save()

        # Update the associated User instance with client_name and client_email
        user_instance = request.user
        user_instance.username = new_client_name
        user_instance.email = request.POST['client_email']
        user_instance.save()

        return redirect('adminhome')






def allprop(request):
    allproperty_details = NewPropertyData.objects.all()
    return render(request,'allpropert.html',{'allproperty_details':allproperty_details})


def appartment(request):
    appartments = NewPropertyData.objects.filter(property_type='Appartment')
    return render(request,'Appartment.html',{'appartments':appartments})


def independent(request):
    independents = NewPropertyData.objects.filter(property_type='Independent Floor')
    return render(request,'independent.html',{'independents':independents})


def builderfloor(request):
    builderfloors=NewPropertyData.objects.filter(property_type='Builder Floor')
    return render(request,'builderfloor.html',{'builderfloors':builderfloors})

def villas(request):
    villas=NewPropertyData.objects.filter(property_type='Villa')
    return render(request,'villa.html',{'villas':villas})



@login_required(login_url='loginpage')
def logoutuser(request):
    logout(request)
    return render(request, 'homepage.html')



@login_required(login_url='loginpage')
def changepasswrd(request):
    log_user = ClientData.objects.filter(client_name=request.user.username).first()

    if request.method == 'POST':
        current_password = request.POST.get('currentpassword')
        new_pass1 = request.POST.get('newpassword1')
        new_pass2 = request.POST.get('newpassword2')

        user = authenticate(username=request.user.username, password=current_password)

        if not current_password or not new_pass1 or not new_pass2:
            message = "Please fill in all the fields."
            return render(request, 'changepass.html', {'message': message, 'log_user': log_user})

        elif user is None or not check_password(current_password, user.password):
            message = "Check your current password."
            return render(request, 'changepass.html', {'message': message, 'log_user': log_user})

        elif is_valid_password(new_pass1) is False:
            message = "Your password must contain letters, digits, and special characters."
            return render(request, 'changepass.html', {'message': message, 'log_user': log_user})

        else:
            if new_pass1 != new_pass2:
                message = "Your new passwords don't match."
                return render(request, 'changepass.html', {'message': message, 'log_user': log_user})

            else:
                user.set_password(new_pass1)
                user.save()
                login(request, user)  # Log in the user with the new password
                messages.success(request, 'Your password has been changed successfully.')
                return redirect('changepassword')

    return render(request, 'changepass.html', {'log_user': log_user})



@login_required(login_url='loginpage')
def deletestudent(request,id):
    data = NewPropertyData.objects.get(id = id)
    data.delete()
    return redirect('adminhome')


@login_required(login_url='loginpage')
def edit_property(request, id):
    edit_data = NewPropertyData.objects.get(id=id)

    if request.method == 'POST':
        # Update fields based on your model structure
        edit_data.seller_name = request.POST.get('seller-name')
        edit_data.property_name = request.POST.get('property-name')
        edit_data.property_type = request.POST.get('property-type')
        edit_data.status_name = request.POST.get('status-name')
        edit_data.property_cost = request.POST.get('property-cost')
        edit_data.property_size = request.POST.get('property-size')
        edit_data.seller_contact_details = request.POST.get('seller-contact-details')
        edit_data.email_property = request.POST.get('email-property')
        edit_data.property_amenities = request.POST.get('property-amenities', 'Default Amenities')
        edit_data.property_specifications = request.POST.get('property-specifications')
        edit_data.property_total_rooms = request.POST.get('property-total-rooms')
        edit_data.property_balcony = request.POST.get('property-balcony')
        edit_data.property_total_bathrooms = request.POST.get('property-total-bathrooms')
        edit_data.property_address = request.POST.get('property-address')
        edit_data.property_description = request.POST.get('property-description')

        # Handle property image update
        if 'property-image-upload-type' in request.FILES:
            edit_data.property_image = request.FILES['property-image-upload-type']

        # Save the updated data
        edit_data.save()

        # Redirect to the display_properties page after successful update
        return redirect('propertyreport')

    return render(request, 'edit_property.html', {'property': edit_data})





def forgot_password(request):
    # getting user input from forgot password.
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        npw1 = request.POST.get('new_password_1')
        npw2 = request.POST.get('new_password_2')

        # Checking for invalid username and email.
        if not username or not email or not npw1 or not npw2:
            message = "Don't leave empty!"
            return render(request, 'sellforgetpass.html', {'message': message})

        elif not is_valid_password(npw1):
            message = "Your password must contain letters, digits, and special characters."
            return render(request, 'sellforgetpass.html', {'message': message})

        elif not User.objects.filter(email=email, username=username).exists():
            message = "Check your registered email or Username."
            return render(request, 'sellforgetpass.html', {'message': message})
        else:
            # Checking if passwords are NOT the same.
            if npw1 != npw2:
                message = "Both passwords are not the same."
                return render(request, 'sellforgetpass.html', {'message': message})

            user = User.objects.filter(email=email).first()
            tab_user = ClientData.objects.filter(client_email=email).first()

            user.set_password(npw1)
            user.save()  # saved in auth_user table

            tab_user.client_password = make_password(npw1)
            tab_user.client_confirm_password = make_password(npw2)
            tab_user.save()  # saved in clientdata table

            # Add a success message
            messages.success(request, 'Password changed successfully. Please login with your new password.')

            return redirect('loginpage')
    else:
        return render(request, 'sellforgetpass.html')




@login_required(login_url='loginpage')
def enquiryreport(request):
    enquiryrep = SendEnquiry.objects.filter(seller_name=request.user.username)

    return render(request,'enquiryreport.html',{'enquiryrep':enquiryrep})


@login_required(login_url='loginpage')
def viewflat(request,id):
    viewflat = NewPropertyData.objects.get(id = id)
    return render(request,'adminviewflat.html',{'viewflat':viewflat})





from django.shortcuts import get_object_or_404, redirect, render
from .models import SendEnquiry, SoldProperty, NewPropertyData
from django.contrib.auth.decorators import login_required

@login_required(login_url='loginpage')
def customer_report(request):
    if request.method == "POST":
        confirmation = request.POST.get('confirmation')
        enquiry_id = request.POST.get('enquiry_id')

        # Get the specific SendEnquiry instance
        enquiry = get_object_or_404(SendEnquiry, id=enquiry_id)

        if confirmation == 'Purchased':
            # Confirm the purchase and save the property ID
            enquiry.confirmation = confirmation
            enquiry.save()

            # Retrieve the corresponding NewPropertyData instance
            new_property_data = get_object_or_404(NewPropertyData, id=enquiry.property_id)

            # Create a SoldProperty instance with details from NewPropertyData
            sold_property = SoldProperty.objects.create(
                property_id=new_property_data.id,  # Set property_id to the id of NewPropertyData
                seller_name=new_property_data.seller_name,
                property_name=new_property_data.property_name,
                property_type=new_property_data.property_type,
                status_name=new_property_data.status_name,
                property_cost=new_property_data.property_cost,
                property_size=new_property_data.property_size,
                seller_contact_details=new_property_data.seller_contact_details,
                email_property=new_property_data.email_property,
                property_amenities=new_property_data.property_amenities,
                property_specifications=new_property_data.property_specifications,
                property_total_rooms=new_property_data.property_total_rooms,
                property_balcony=new_property_data.property_balcony,
                property_total_bathrooms=new_property_data.property_total_bathrooms,
                property_address=new_property_data.property_address,
                property_image=new_property_data.property_image,
                property_description=new_property_data.property_description,
                buyer_name=enquiry.buyer_name  # Add buyer_name to the SoldProperty instance
            )

            # Delete the NewPropertyData instance
            new_property_data.delete()

            # Delete all other SendEnquiry instances with the same property ID
            SendEnquiry.objects.filter(property_id=enquiry.property_id).exclude(id=enquiry_id).delete()

        elif confirmation == 'Purchase Declined':
            # Delete the enquiry if "Decline Enquiry" option is selected
            enquiry.delete()

        return redirect('customer_report')
    else:
        # If method is GET, display SendEnquiry instances for the logged-in user
        enquiryrep = SendEnquiry.objects.filter(seller_name=request.user.username)
        return render(request, 'customer_report.html', {'enquiryrep': enquiryrep})



#buyer side
@login_required(login_url='loginpage')
def buyhme(request):
    return render(request,'buyhome.html')




@login_required(login_url='loginpage')
def buyabout(request):
    return render(request,'buyabout.html')

@login_required(login_url='loginpage')
def buydashboard(request):
    return render(request,'buydash.html')


@login_required(login_url='loginpage')
def buyallprop(request):
    buyallproperty_details = NewPropertyData.objects.all()
    return render(request,'buyallprop.html',{'buyallproperty_details':buyallproperty_details})


@login_required(login_url='loginpage')
def buyappartment(request):
    buyappartments = NewPropertyData.objects.filter(property_type='Appartment')
    return render(request,'buyappartment.html',{'buyappartments':buyappartments})


@login_required(login_url='loginpage')
def buyindependent(request):
    buyindependents = NewPropertyData.objects.filter(property_type='Independent Floor')
    return render(request,'buyindependent.html',{'buyindependents':buyindependents})


@login_required(login_url='loginpage')
def buybuilder(request):
    buybuilderfloors=NewPropertyData.objects.filter(property_type='Builder Floor')
    return render(request,'buybuilderfloor.html',{'buybuilderfloors':buybuilderfloors})


@login_required(login_url='loginpage')
def buyvilla(request):
    buyvillas=NewPropertyData.objects.filter(property_type='Villa')
    return render(request,'buyvilla.html',{'buyvillas':buyvillas})


@login_required(login_url='loginpage')
def viewdetails(request,id):
    property_data=NewPropertyData.objects.get(id=id)
    return render(request,'fetchingdetailsofproduct.html',{'property_data':property_data})




@login_required(login_url='loginpage')
def sendenquiry(request, id):
    property_data = NewPropertyData.objects.get(id=id)
    buy_data = ClientData.objects.filter(client_name=request.user.username)

    for data in buy_data:
        buy_name = data.client_name
        buy_mobile = data.client_number
        buy_email = data.client_email
        buy_dob = data.client_DOB
        buy_image = data.client_picture

    SendEnquiry(
        seller_name=property_data.seller_name,
        buyer_name=buy_name,
        buy_mobile=buy_mobile,
        buy_email=buy_email,
        buy_dob=buy_dob,
        buy_image=buy_image,
        property_id=id
    ).save()



    return redirect('buyerallproperty')




@login_required(login_url='loginpage')
def my_property(request):
    buyer_name = request.user.username
    my_properties = SoldProperty.objects.filter(buyer_name=buyer_name)
    return render(request, 'myproperty.html', {'my_properties': my_properties})





@login_required(login_url='loginpage')
def myaccpropdetails(request,id):
    viewflat = SoldProperty.objects.get(id = id)
    return render(request,'myaccpropdetais.html',{'viewflat':viewflat})

@login_required(login_url='loginpage')
def buyer_acc_details(request):
    # Assuming you have a OneToOneField relationship with a custom user model
    logged_in_user = ClientData.objects.filter(client_name=request.user.username).first()

    if request.method == 'GET':
        message = "You can edit your details here."
        return render(request, 'buy_my_account.html', {'user': logged_in_user, 'message': message})
    else:
        # Get the new client_picture from the form
        new_client_picture = request.FILES.get('client_picture')

        # Check if a new image has been provided
        if new_client_picture:
            logged_in_user.client_picture = new_client_picture

        # Update other fields
        new_client_name = request.POST['client_name']

        # Check if the new client name already exists in ClientData
        if ClientData.objects.filter(client_name=new_client_name).exclude(id=logged_in_user.id).exists():
            msg = 'Client name already exists. Please choose a different client name.'
            return render(request, 'buy_my_account.html', {'msg': msg, 'user': logged_in_user, 'message': "You can edit your details here."})

        # Update other fields
        logged_in_user.client_name = new_client_name
        logged_in_user.client_login_id = request.POST['client_name']  # Assuming you also want to update login_id
        logged_in_user.client_gender = request.POST['client_gender']
        logged_in_user.client_email = request.POST['client_email']
        logged_in_user.client_number = request.POST['client_number']
        logged_in_user.client_address1 = request.POST['client_address1']
        logged_in_user.client_address2 = request.POST['client_address2']
        logged_in_user.client_city = request.POST['client_city']
        logged_in_user.client_state = request.POST['client_state']
        logged_in_user.client_country = request.POST['client_country']

        # Save the ClientData object
        logged_in_user.save()

        # Update the associated User instance with client_name and client_email
        user_instance = request.user
        user_instance.username = new_client_name
        user_instance.email = request.POST['client_email']
        user_instance.save()

        return redirect('buyerhome')



@login_required(login_url='loginpage')
def buyer_changepass(request):
    log_user = ClientData.objects.filter(client_name=request.user.username).first()

    if request.method == 'POST':
        current_password = request.POST.get('currentpassword')
        new_pass1 = request.POST.get('newpassword1')
        new_pass2 = request.POST.get('newpassword2')

        user = authenticate(username=request.user.username, password=current_password)

        if not current_password or not new_pass1 or not new_pass2:
            message = "Please fill in all the fields."

        elif user is None or not check_password(current_password, user.password):
            return render(request, 'buy_changepass.html', {'message': message, 'log_user': log_user})
            message = "Check your current password."

        elif is_valid_password(new_pass1) is False:
            return render(request, 'buy_changepass.html', {'message': message, 'log_user': log_user})
            message = "Your password must contain letters, digits, and special characters."
            return render(request, 'buy_changepass.html', {'message': message, 'log_user': log_user})

        else:
            if new_pass1 != new_pass2:
                message = "Your new passwords don't match."
                return render(request, 'buy_changepass.html', {'message': message, 'log_user': log_user})

            else:
                user.set_password(new_pass1)
                user.save()
                login(request, user)  # Log in the user with the new password
                messages.success(request, 'Your password has been changed successfully.')
                return redirect('changepassword')

    return render(request, 'buy_changepass.html', {'log_user': log_user})







@login_required(login_url='loginpage')
def post_property_view(request):
    post_property_items = PostReport.objects.filter(user=request.user)
    context = {'post_properties': post_property_items,}
    return render(request, 'customer_cart.html', context)





@login_required(login_url='loginpage')
def add_to_post_property(request,property_id):
        # Retrieve the product object
    property = NewPropertyData.objects.get(pk=property_id)
    # Check if the user is authenticated
    if request.user.is_authenticated:

        # Check if the property already exists in the user's cart
        Property_exist = PostReport.objects.filter(user=request.user, property=property).exists()
        if not Property_exist:
            PostReport.objects.create(user=request.user, property=property)
    return redirect('post_property')



@login_required(login_url='loginpage')
def del_from_post_property(request, property_id):
    # handle property deletion
    if request.user.is_authenticated:
        # Get the product object
        property = get_object_or_404(NewPropertyData, pk=property_id)

        # Check if the property exists in the user's saved properties
        property_to_delete = PostReport.objects.filter(user=request.user, property=property).first()

        if property_to_delete:
            # If the property exists, delete it
            property_to_delete.delete()

    return redirect('post_property')






def my_enquiry_view(request):
    latest_enquiry = SendEnquiry.objects.filter(buyer_name=request.user.username)
    return render(request, 'myenquiry.html', {'send_enquiry': latest_enquiry})





def delete_enquiry(request, enquiry_id):
    enquiry = get_object_or_404(SendEnquiry, id=enquiry_id)
    if enquiry.buyer_name == request.user.username:
        enquiry.delete()
    return redirect('my_enquiry_view')
