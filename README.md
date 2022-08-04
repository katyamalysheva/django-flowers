# django-flowers
1. Models are stored in flower_site -> models -> models.py. 
Created models:
 - CustomUser, inherited from AbstractUser, additional fields: (created to track users)
    user_type (choices - Seller, Customer)
    
 - Lot, fields: (created to track lots)
   flower_type - flower name
   flower_color - color of flower with choices
   flower_num - amount of flowers in a lot
   flower_price_of_single - price per flower
   is_visible - seller can choose whether customers can see this lot
   flower_seller - foreign key for sellers(CustomUser)
   
- Deals, fields: (created to track deals)
  time - time the deal was saved
  lot - FK for lot customer choosed
  amount - number of flowers from lot customer wants to buy 
  customer - FK for customer 
  total_check - price per flower from lot * amount 
  
- LotsReview, fields (created to track customer reviews for lot)
  reviewed_lot - FK for lot 
  author - FK for customer making the review
  review 
  
- LotsReview, fields (created to track customer reviews for sellers)
  reviewed_seller - FK for seller
  author - FK for customer making the review
  review 
  
  
 2. Fuction seller (stored in views.py) 
    retuns a dictionary, where keys are sellers and values are dicts with customers and checks for each customer made from buying flowers from a particular seller) 

  
  
  
  
  
