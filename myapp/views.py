from django.shortcuts import render

# Primary views
def index(request):
   return render(request, 'index.html')
def foodtruck(request):
   return render(request, 'food-truck.html')
def gallery(request):
   return render(request, 'gallery.html')
def about(request):
   return render(request, 'about.html')
def contactus(request):
   return render(request, 'contactus.html')



# Secondary views

## Food Truck
def location(request):
   return render(request, 'location.html')
def orders(request):
   return render(request, 'order.html')
def events(request):
   return render(request, 'events.html')

## gallery
def moments(request):
   return render(request, 'moments.html')
def blog(request):
   return render(request, 'blog.html')

## about
def aboutus(request):
   return render(request, 'about.html')
def careers(request):
   return render(request, 'careers.html')

## contact 
def donate(request):
   return render(request, 'donate.html')

#### orders 
def preorder(request):
   menu = [
      {'item_id': 1, 'dish_name': 'Biryani', 'price': '120'},
      {'item_id': 2, 'dish_name': 'Peri peri shawarma', 'price': '90'},
      {'item_id': 3, 'dish_name': 'Rose milk', 'price': '50'},
      {'item_id': 4, 'dish_name': 'Puttu ice cream', 'price': '150'},
   ]
   return render(request, 'preorder.html', {'menu': menu})
def orderonline(request):
   menu = [
      {'item_id': 5, 'dish_name': 'Masala Dosa', 'price': '80'},
      {'item_id': 6, 'dish_name': 'Paneer Butter Masala', 'price': '160'},
      {'item_id': 7, 'dish_name': 'Chicken Tikka', 'price': '200'},
      {'item_id': 8, 'dish_name': 'Tandoori Roti', 'price': '30'},
      {'item_id': 9, 'dish_name': 'Hyderabadi Chicken Biryani', 'price': '250'},
      {'item_id': 10, 'dish_name': 'Pani Puri', 'price': '60'},
      {'item_id': 11, 'dish_name': 'Rajma Chawal', 'price': '130'},
      {'item_id': 12, 'dish_name': 'Aloo Paratha', 'price': '90'},
      {'item_id': 13, 'dish_name': 'Gulab Jamun', 'price': '70'},
      {'item_id': 14, 'dish_name': 'Lassi', 'price': '50'},
      {'item_id': 15, 'dish_name': 'Butter Naan', 'price': '40'},
      {'item_id': 16, 'dish_name': 'Palak Paneer', 'price': '170'},
      {'item_id': 17, 'dish_name': 'Chole Bhature', 'price': '120'},
      {'item_id': 18, 'dish_name': 'Fish Curry', 'price': '220'},
      {'item_id': 19, 'dish_name': 'Rasgulla', 'price': '80'},
      {'item_id': 20, 'dish_name': 'Mango Kulfi', 'price': '90'},
   ]
   return render(request, 'orderonline.html', {'menu': menu})
def storefront(request):
   menu = [
      {'item_id': 21, 'dish_name': 'Paneer Butter Masala', 'price': '180'},
      {'item_id': 22, 'dish_name': 'Aloo Paratha', 'price': '70'},
      {'item_id': 23, 'dish_name': 'Samosa', 'price': '40'},
      {'item_id': 24, 'dish_name': 'Tandoori Chicken', 'price': '250'},
      {'item_id': 25, 'dish_name': 'Dosa', 'price': '60'},
      {'item_id': 26, 'dish_name': 'Pav Bhaji', 'price': '90'},
      {'item_id': 27, 'dish_name': 'Methi Thepla', 'price': '80'},
      {'item_id': 28, 'dish_name': 'Bhel Puri', 'price': '50'},
      {'item_id': 29, 'dish_name': 'Vada Pav', 'price': '40'},
      {'item_id': 30, 'dish_name': 'Lassi (Mango)', 'price': '60'}
]
   return render(request, 'storefront.html', {'menu': menu})