from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q
from .form import *
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.

def Home(request):
    user = request.user
    if 'cart_data' in request.session:
        cart = request.session['cart_data']
    else:
        cart = []
    data = Banner.objects.all()
    post = Post.objects.all()
    filter = Nation.objects.all()
    
    if user.is_authenticated:
        bookings = Booking.objects.filter(user=user).first()
    else:
        bookings = None

    return render(request, 'home.html', {
        'data': data,
        'post': post,
        'filter': filter,
        'category': 'nation',
        'user': user,
        'cart': cart,
        'booking': bookings
    })

@login_required
def UserBookings(request):
    user = request.user
    if user.is_authenticated:
        data = Booking.objects.filter(user=user)
    else:
        data = []
    
    booking_post_data = []
    
    for booking in data:
        posts_with_creation_time = []  # Create a list to store post data with creation time
        for post in booking.post.all():
            post_data = {
                'post': post,
                'created_at': booking.created_at,  # Access the creation time of the booking
            }
            posts_with_creation_time.append(post_data)
        
        booking_post_data.extend(posts_with_creation_time)  # Extend the list with post data
    
    return render(request, 'applications.html', {'data': booking_post_data,'user':user})
 
    

def FilterPost(request):
    if request.method == 'GET':
        action = request.GET.get("action")
        if action=='nation':
            print(action,'sdfsdfsdfsdf')
            print('data here super donvweedlfksadjklf')
            # Process the AJAX request data here
            data = Nation.objects.all()
            # Perform some actions and prepare the response
            response_data = {'message': 'Success', 'data': data}
            t = render_to_string('filter.html', {'data': data,'category':action})
            return JsonResponse({'data': t})
        
        if action=='state':
            print(action,'sdfsdfsdfsdf')
            print('data here super donvweedlfksadjklf')
            # Process the AJAX request data here
            data = State.objects.all()
            # Perform some actions and prepare the response
            response_data = {'message': 'Success', 'data': data}
            t = render_to_string('filter.html', {'data': data,'category':action})
            return JsonResponse({'data': t})
        

        if action=='district':
            print(action,'sdfsdfsdfsdf')
            print('data here super donvweedlfksadjklf')
            # Process the AJAX request data here
            data = District.objects.all()
            # Perform some actions and prepare the response
            response_data = {'message': 'Success', 'data': data}
            t = render_to_string('filter.html', {'data': data,'category':action})
            return JsonResponse({'data': t})           
    else:
        return JsonResponse('you Oompi')

#product-filter.html
def ProductFilter(request):
    if request.method=='GET':
        id = request.GET['id']
        category=request.GET['category']
        print(id,category,)
        if category=='nation':
            nation = Nation.objects.get(id = int(id))
            print(nation,'9999999999999999999999999999')
            data = Post.objects.filter(nation=nation)
            if data:
                t = render_to_string('product-filter.html', {'data': data})
            else:
                t = render_to_string('ajax/empty-post.html')
            return JsonResponse({'data':t})

        elif category=='state':
            state = State.objects.get(id = int(id))
            data = Post.objects.filter(state=state)
            print(data,'ghfdfffffffffffffffg')
            if data:
                t = render_to_string('product-filter.html', {'data': data})
            else:
                t = render_to_string('ajax/empty-post.html')
            return JsonResponse({'data':t})
        
        elif category=='district':
            district = District.objects.get(id = int(id))
            data = Post.objects.filter(district=district)
            print(data,'ghfdfffffffffffffffg')
            if data:
                t = render_to_string('product-filter.html', {'data': data})
            else:
                t = render_to_string('ajax/empty-post.html')
            return JsonResponse({'data':t})


def ProductDeatail(request,id):
    data = Post.objects.get(id =id)
    district= data.district
    related = Post.objects.filter(district=district)
    print(related,'dskfalsdjkfasdklfasldfjklasdfjklasdfjklasjkl;a')
    return render (request,'productDetail.html',{'data':data,'related':related})


def SearchProduct(request):
    print('he dondsdfasdklfasdkjfaksljdfjklasdfkljkl')
    if request.method =='GET':
        search = request.GET["value"]
        print(search)
        data= Post.objects.filter(Q(nation__title__icontains=search) | Q(state__title__icontains=search)|Q(district__title__icontains=search) | Q(name__icontains=search) )
        if data:
            t = render_to_string('product-filter.html', {'data': data})
        else:
            t = render_to_string('ajax/empty-post.html')
        return JsonResponse({'data':t})


def Add_To_cart(request):
    productID= request.GET['id']
    cart_P=[productID]
   
    if 'cart_data' in request.session:

        print('cart_data in also exist',request.session['cart_data'])
        if str(request.GET['id']) in request.session['cart_data']:
            print('yes exist product jid')
            return JsonResponse('ydsdfsdf exist' ,safe=False)

        else:
            cart_data = request.session['cart_data']
            cart_data.append(productID)
            request.session['cart_data']=cart_data
           
    else:
        request.session['cart_data'] = cart_P
        print(request.session['cart_data'],'no cart data in session case is this ')

    return JsonResponse({'data': 343})


@login_required
def Cart(request):
    user =request.user
    if 'cart_data' in request.session:
        ids = request.session['cart_data']
        print(ids,'checking this ids')
        data = Post.objects.filter(id__in=ids)
        return render(request, 'cart.html', {'data': data,'user':user})
    else:
        return render(request, 'cart.html')


@login_required
def Delete_cart(request):
    if request.method == 'GET':
        id = request.GET['id']
        print(id,'sdfsdfsd',request.session['cart_data'])
        if 'cart_data' in request.session:
            print('fisrt layer')
            if id in request.session['cart_data']:
                print('second layer')
                cart_data=request.session['cart_data']
                cart_data.remove(id)
                request.session['cart_data'] = cart_data
                ids = request.session['cart_data']
                print(ids)
                data = Post.objects.filter(id__in=ids)
                t=render_to_string('ajax/cart_list.html',{'data':data})
                return JsonResponse({'data':t})
            else:
                print('not id found')
        else:
            print('no cart found pundo')

def Signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        print(request.POST,request.FILES,'lljkljkjkljklkljjklljk')
        if form.is_valid():
            form.save()  # Save the user object to the database
            return redirect('home')  # Replace 'home' with the desired URL after successful signup
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def user_update(request):
    user = request.user

    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect('user')  # Replace 'profile' with the URL name of the user's profile page
    else:
        form = RegistrationForm(instance=user)

    return render(request, 'user.html', {'form': form})
         
        


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
    
        if user :
            login(request, user)
            return redirect('home')  # Replace 'home' with the desired URL after successful login
        else:
            return redirect('signup')  # Replace 'login' with the URL for the login page
    else:
        return render(request, 'login.html')




@login_required
def Logout(request):
    logout(request)
    return redirect('home')

@login_required
def user(request):
    user = request.user
    rating=UserRating.objects.filter(user=user)

    # finding user average rating using without aggretion 
    try:
            NumberOFuserRated = len(rating)
            totalSumOfRationgByuser=0
            for i in rating:
                totalSumOfRationgByuser += i.rating
            rating=totalSumOfRationgByuser//NumberOFuserRated
            print(rating,'oh this is out new rating')
    except:
        print('user is not rated')
        rating=0
          
    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect('user')
        
        # redemm time to money
    if request.method == 'POST' :
        print('done',request.POST)
        Redeemtime = request.POST['time']
        curruncy = request.POST['currency']
        if int(Redeemtime)>0:
            OldTime=user.time
            print(Redeemtime,curruncy,'done taking value from post filed')
            user.time=int(OldTime)-int(Redeemtime)
            PreviousCurruncy = user.currency
            user.currency = int(curruncy) + int(PreviousCurruncy)
            user.save()
            return render(request,'success.html')
        elif int(Redeemtime) <=0 :
            return render(request,'fail.html')
        # redeemForm = RedeemForm(request.POST)
        # if redeemForm.is_valid():
        #     redeemInstance = redeemForm.save(commit=False)
        #     redeemTime = redeemForm.cleaned_data['time']
        #     availableTime = user.time
        #     newTime = availableTime - redeemTime
        #     print(newTime, 'diff', redeemTime, availableTime)

            # Update the "time" field of the redeemForm instance
            # redeemInstance.time = newTime
            # print(redeemInstance)

            # # Save the form to the database with the updated "time" value
            # redeemInstance.save()

    else:
        form = RegistrationForm(instance=user)
        redeemForm =RedeemForm(instance=user)
    return render(request, 'user.html', {'user': user, 'form':form,'rating':rating,'redeemForm':redeemForm})

@login_required
def Bookings(request):
    id = request.GET.get('id')
    post = get_object_or_404(Post, id=id)
    user = request.user

    booking, created = Booking.objects.get_or_create(user=user)  # Get or create a booking for the user

    if created:
        # This is a newly created booking, set the created_at datetime
        booking.created_at = timezone.now()
        booking.save()

    if post not in booking.post.all():
        booking.post.add(post)  # Add the post to the booking

    return JsonResponse('done it', safe=False)

@login_required
def RedemmCurruncy(request):
    if request.method=='POST':
        UserDetail=CustomUser.objects.filter(user=request.user)
        print(request.POST['curruncy'],request.POST['time'])


