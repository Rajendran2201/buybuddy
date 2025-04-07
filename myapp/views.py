from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
import datetime

menu_items = [
        {'item_id': 21, 'dish_name': 'Paneer Butter Masala', 'price': '180', 'image': 'assets/paneer-butter-masala.jpg', 'category': 'main-course'},
        {'item_id': 22, 'dish_name': 'Aloo Paratha', 'price': '70', 'image': 'assets/aloo-paratha.jpg', 'category': 'main-course'},
        {'item_id': 23, 'dish_name': 'Samosa', 'price': '40', 'image': 'assets/samosa.jpg', 'category': 'snacks'},
        {'item_id': 24, 'dish_name': 'Tandoori Chicken', 'price': '250', 'image': 'assets/tandoori-chicken.jpg', 'category': 'non-veg'},
        {'item_id': 25, 'dish_name': 'Dosa', 'price': '60', 'image': 'assets/dosa.jpg', 'category': 'main-course'},
        {'item_id': 26, 'dish_name': 'Pav Bhaji', 'price': '90', 'image': 'assets/pav-bhaji.jpg', 'category': 'street-food'},
        {'item_id': 27, 'dish_name': 'Methi Thepla', 'price': '80', 'image': 'assets/methi-thepla.jpg', 'category': 'main-course'},
        {'item_id': 28, 'dish_name': 'Bhel Puri', 'price': '50', 'image': 'assets/bhel-puri.jpg', 'category': 'street-food'},
        {'item_id': 29, 'dish_name': 'Vada Pav', 'price': '40', 'image': 'assets/vada-pav.jpg', 'category': 'street-food'},
        {'item_id': 30, 'dish_name': 'Lassi (Mango)', 'price': '60', 'image': 'assets/mango-lassi.jpg', 'category': 'beverages'},
         {'item_id': 1, 'dish_name': 'Biryani', 'price': '120', 'image': 'assets/biryani.jpg', 'category': 'biryani'},
         {'item_id': 2, 'dish_name': 'Peri peri shawarma', 'price': '90', 'image': 'assets/peri-peri-shawarma.jpg', 'category': 'shawarma'},
         {'item_id': 3, 'dish_name': 'Rose milk', 'price': '50', 'image': 'assets/rose-milk.jpg', 'category': 'beverages'},
         {'item_id': 4, 'dish_name': 'Puttu ice cream', 'price': '150', 'image': 'assets/puttu-ice-cream.jpg', 'category': 'icecream'},
         {'item_id': 35, 'dish_name': 'Hyderabadi Biryani', 'price': '140', 'image': 'assets/hyderabadi-chicken-biryani.jpg', 'category': 'biryani'},
         {'item_id': 36, 'dish_name': 'Classic Shawarma', 'price': '80', 'image': 'assets/classic-shawarma.jpg', 'category': 'shawarma'},
         {'item_id': 37, 'dish_name': 'Mint Mojito', 'price': '60', 'image': 'assets/mint-mojito.jpg', 'category': 'beverages'},
         {'item_id': 38, 'dish_name': 'Falooda Ice Cream', 'price': '120', 'image': 'assets/falooda-ice-cream.jpg', 'category': 'icecream'},
         {'item_id': 39, 'dish_name': 'Paneer Biryani', 'price': '130', 'image': 'assets/paneer-biryani.jpg', 'category': 'biryani'},
         {'item_id': 40, 'dish_name': 'Mexican Shawarma', 'price': '100', 'image': 'assets/mexican-shawarma.jpg', 'category': 'shawarma'},
         {'item_id': 41, 'dish_name': 'Lemon Soda', 'price': '40', 'image': 'assets/lemon-soda.jpg', 'category': 'beverages'},
         {'item_id': 42, 'dish_name': 'Kulfi Stick', 'price': '70', 'image': 'assets/kulfi-stick.jpg', 'category': 'icecream'},
      {'item_id': 5, 'dish_name': 'Masala Dosa', 'price': '80', 'image': 'assets/masala-dosa.jpg', 'category': 'south-indian'},
         {'item_id': 6, 'dish_name': 'Paneer Butter Masala', 'price': '160', 'image': 'assets/paneer-butter-masala.jpg', 'category': 'north-indian'},
         {'item_id': 7, 'dish_name': 'Chicken Tikka', 'price': '200', 'image': 'assets/chicken-tikka.jpg', 'category': 'non-veg-specials'},
         {'item_id': 8, 'dish_name': 'Tandoori Roti', 'price': '30', 'image': 'assets/tandoori-roti.jpg', 'category': 'breads'},
         {'item_id': 9, 'dish_name': 'Hyderabadi Chicken Biryani', 'price': '250', 'image': 'assets/hyderabadi-chicken-biryani.jpg', 'category': 'non-veg-specials'},
         {'item_id': 10, 'dish_name': 'Pani Puri', 'price': '60', 'image': 'assets/pani-puri.jpg', 'category': 'street-food'},
         {'item_id': 11, 'dish_name': 'Rajma Chawal', 'price': '130', 'image': 'assets/rajma-chawal.jpg', 'category': 'north-indian'},
         {'item_id': 12, 'dish_name': 'Aloo Paratha', 'price': '90', 'image': 'assets/aloo-paratha.jpg', 'category': 'north-indian'},
         {'item_id': 13, 'dish_name': 'Gulab Jamun', 'price': '70', 'image': 'assets/gulab-jamun.jpg', 'category': 'desserts'},
         {'item_id': 14, 'dish_name': 'Lassi', 'price': '50', 'image': 'assets/lassi.jpg', 'category': 'beverages'},
         {'item_id': 15, 'dish_name': 'Butter Naan', 'price': '40', 'image': 'assets/butter-naan.jpg', 'category': 'breads'},
         {'item_id': 16, 'dish_name': 'Palak Paneer', 'price': '170', 'image': 'assets/palak-paneer.jpg', 'category': 'north-indian'},
         {'item_id': 17, 'dish_name': 'Chole Bhature', 'price': '120', 'image': 'assets/chole-bhature.jpg', 'category': 'north-indian'},
         {'item_id': 18, 'dish_name': 'Fish Curry', 'price': '220', 'image': 'assets/fish-curry.jpg', 'category': 'non-veg-specials'},
         {'item_id': 19, 'dish_name': 'Rasgulla', 'price': '80', 'image': 'assets/rasgulla.jpg', 'category': 'desserts'},
         {'item_id': 20, 'dish_name': 'Mango Kulfi', 'price': '90', 'image': 'assets/mango-kulfi.jpg', 'category': 'desserts'},
      
]


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

def registerevent(request):
   return render(request, 'registerevent.html')




def update_cart_quantity(request):
    item_id = str(request.POST.get('item_id'))
    action = request.POST.get('action')
    
    cart = request.session.get('cart', {})

    if item_id in cart:
        if action == 'increase':
            cart[item_id]['quantity'] += 1
        elif action == 'decrease' and cart[item_id]['quantity'] > 1:
            cart[item_id]['quantity'] -= 1
        # You can also check min/max limits here

    request.session['cart'] = cart
    return redirect('cart')  # redirect back to cart page



def remove_from_cart(request):
    item_id = str(request.POST.get('item_id'))

    cart = request.session.get('cart', {})
    if item_id in cart:
        del cart[item_id]

    request.session['cart'] = cart
    return redirect('cart')

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
      {'item_id': 1, 'dish_name': 'Biryani', 'price': '120', 'image': 'assets/biryani.jpg', 'category': 'biryani'},
      {'item_id': 2, 'dish_name': 'Peri peri shawarma', 'price': '90', 'image': 'assets/peri-peri-shawarma.jpg', 'category': 'shawarma'},
      {'item_id': 3, 'dish_name': 'Rose milk', 'price': '50', 'image': 'assets/rose-milk.jpg', 'category': 'beverages'},
      {'item_id': 4, 'dish_name': 'Puttu ice cream', 'price': '150', 'image': 'assets/puttu-ice-cream.jpg', 'category': 'icecream'},
      {'item_id': 35, 'dish_name': 'Hyderabadi Biryani', 'price': '140', 'image': 'assets/hyderabadi-chicken-biryani.jpg', 'category': 'biryani'},
      {'item_id': 36, 'dish_name': 'Classic Shawarma', 'price': '80', 'image': 'assets/classic-shawarma.jpg', 'category': 'shawarma'},
      {'item_id': 37, 'dish_name': 'Mint Mojito', 'price': '60', 'image': 'assets/mint-mojito.jpg', 'category': 'beverages'},
      {'item_id': 38, 'dish_name': 'Falooda Ice Cream', 'price': '120', 'image': 'assets/falooda-ice-cream.jpg', 'category': 'icecream'},
      {'item_id': 39, 'dish_name': 'Paneer Biryani', 'price': '130', 'image': 'assets/paneer-biryani.jpg', 'category': 'biryani'},
      {'item_id': 40, 'dish_name': 'Mexican Shawarma', 'price': '100', 'image': 'assets/mexican-shawarma.jpg', 'category': 'shawarma'},
      {'item_id': 41, 'dish_name': 'Lemon Soda', 'price': '40', 'image': 'assets/lemon-soda.jpg', 'category': 'beverages'},
      {'item_id': 42, 'dish_name': 'Kulfi Stick', 'price': '70', 'image': 'assets/kulfi-stick.jpg', 'category': 'icecream'},
   ]

   return render(request, 'preorder.html', {'menu': menu})


def orderonline(request):
      menu = [
         {'item_id': 5, 'dish_name': 'Masala Dosa', 'price': '80', 'image': 'assets/masala-dosa.jpg', 'category': 'south-indian'},
         {'item_id': 6, 'dish_name': 'Paneer Butter Masala', 'price': '160', 'image': 'assets/paneer-butter-masala.jpg', 'category': 'north-indian'},
         {'item_id': 7, 'dish_name': 'Chicken Tikka', 'price': '200', 'image': 'assets/chicken-tikka.jpg', 'category': 'non-veg-specials'},
         {'item_id': 8, 'dish_name': 'Tandoori Roti', 'price': '30', 'image': 'assets/tandoori-roti.jpg', 'category': 'breads'},
         {'item_id': 9, 'dish_name': 'Hyderabadi Chicken Biryani', 'price': '250', 'image': 'assets/hyderabadi-chicken-biryani.jpg', 'category': 'non-veg-specials'},
         {'item_id': 10, 'dish_name': 'Pani Puri', 'price': '60', 'image': 'assets/pani-puri.jpg', 'category': 'street-food'},
         {'item_id': 11, 'dish_name': 'Rajma Chawal', 'price': '130', 'image': 'assets/rajma-chawal.jpg', 'category': 'north-indian'},
         {'item_id': 12, 'dish_name': 'Aloo Paratha', 'price': '90', 'image': 'assets/aloo-paratha.jpg', 'category': 'north-indian'},
         {'item_id': 13, 'dish_name': 'Gulab Jamun', 'price': '70', 'image': 'assets/gulab-jamun.jpg', 'category': 'desserts'},
         {'item_id': 14, 'dish_name': 'Lassi', 'price': '50', 'image': 'assets/lassi.jpg', 'category': 'beverages'},
         {'item_id': 15, 'dish_name': 'Butter Naan', 'price': '40', 'image': 'assets/butter-naan.jpg', 'category': 'breads'},
         {'item_id': 16, 'dish_name': 'Palak Paneer', 'price': '170', 'image': 'assets/palak-paneer.jpg', 'category': 'north-indian'},
         {'item_id': 17, 'dish_name': 'Chole Bhature', 'price': '120', 'image': 'assets/chole-bhature.jpg', 'category': 'north-indian'},
         {'item_id': 18, 'dish_name': 'Fish Curry', 'price': '220', 'image': 'assets/fish-curry.jpg', 'category': 'non-veg-specials'},
         {'item_id': 19, 'dish_name': 'Rasgulla', 'price': '80', 'image': 'assets/rasgulla.jpg', 'category': 'desserts'},
         {'item_id': 20, 'dish_name': 'Mango Kulfi', 'price': '90', 'image': 'assets/mango-kulfi.jpg', 'category': 'desserts'},
      ]

      return render(request, 'orderonline.html', {'menu': menu})


def storefront(request):
    menu = [
        {'item_id': 21, 'dish_name': 'Paneer Butter Masala', 'price': '180', 'image': 'assets/paneer-butter-masala.jpg', 'category': 'main-course'},
        {'item_id': 22, 'dish_name': 'Aloo Paratha', 'price': '70', 'image': 'assets/aloo-paratha.jpg', 'category': 'main-course'},
        {'item_id': 23, 'dish_name': 'Samosa', 'price': '40', 'image': 'assets/samosa.jpg', 'category': 'snacks'},
        {'item_id': 24, 'dish_name': 'Tandoori Chicken', 'price': '250', 'image': 'assets/tandoori-chicken.jpg', 'category': 'non-veg'},
        {'item_id': 25, 'dish_name': 'Dosa', 'price': '60', 'image': 'assets/dosa.jpg', 'category': 'main-course'},
        {'item_id': 26, 'dish_name': 'Pav Bhaji', 'price': '90', 'image': 'assets/pav-bhaji.jpg', 'category': 'street-food'},
        {'item_id': 27, 'dish_name': 'Methi Thepla', 'price': '80', 'image': 'assets/methi-thepla.jpg', 'category': 'main-course'},
        {'item_id': 28, 'dish_name': 'Bhel Puri', 'price': '50', 'image': 'assets/bhel-puri.jpg', 'category': 'street-food'},
        {'item_id': 29, 'dish_name': 'Vada Pav', 'price': '40', 'image': 'assets/vada-pav.jpg', 'category': 'street-food'},
        {'item_id': 30, 'dish_name': 'Lassi (Mango)', 'price': '60', 'image': 'assets/mango-lassi.jpg', 'category': 'beverages'},
    ]
    return render(request, 'storefront.html', {'menu': menu})



def add_to_cart(request, item_id):
    # Initialize cart if it doesn't exist
    cart = request.session.get('cart', {})

    if str(item_id) in cart:
        cart[str(item_id)] += 1
    else:
        cart[str(item_id)] = 1

    request.session['cart'] = cart  # Save back to session
    return redirect('preorder')  # or use request.META.get('HTTP_REFERER') to redirect to same page


def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for item in menu_items:
      item_id = str(item['item_id'])
      if item_id in cart:
         quantity = cart[item_id]
         price = float(item['price'])  # Convert to float
         item_total = price * quantity
         total_price += item_total
         cart_items.append({
               **item,
               'quantity': quantity,
               'total': item_total
         })


    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
def checkout(request):
    cart = request.session.get('cart', {})
    
    if not cart:
        messages.warning(request, "Your cart is empty.")
        return redirect('cart')


    cart_items = []
    total_price = 0

    for item in menu_items:
        item_id = str(item['item_id'])
        if item_id in cart:
            quantity = cart[item_id]
            price = int(item['price'])  # Ensure it's an integer
            item_total = price * quantity
            total_price += item_total
            cart_items.append({
                **item,
                'quantity': quantity,
                'total': item_total
            })

    # Simulate checkout success
    request.session['cart'] = {}  # Clear cart after checkout
    messages.success(request, "Checkout successful! Your order has been placed.")
    
    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


def download_invoice(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('cart')

    cart_items = []
    total_price = 0

    for item_id, item in cart.items():
        item_total = item['quantity'] * item['price']
        total_price += item_total
        cart_items.append({
            'dish_name': item['dish_name'],
            'quantity': item['quantity'],
            'total': item_total,
        })

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'order_date': datetime.datetime.now().strftime("%d %B, %Y")
    }

    template_path = 'invoice.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('PDF generation failed')
    return response
