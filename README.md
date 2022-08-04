# django-flowers
1. Models are stored in flower_site -> models -> models.py. 
Created models:
 - CustomUser, inherited from AbstractUser, additional fields: (created to track users)
    <br> user_type (choices - Seller, Customer)
    
 - Lot, fields: (created to track lots)
   <br> flower_type - flower name
   <br> flower_color - color of flower with choices
   <br> flower_num - amount of flowers in a lot
   <br> flower_price_of_single - price per flower
   <br> is_visible - seller can choose whether customers can see this lot
   <br> flower_seller - foreign key for sellers(CustomUser)
   
- Deals, fields: (created to track deals)
  <br> time - time the deal was saved
  <br> lot - FK for lot customer choosed
  <br> amount - number of flowers from lot customer wants to buy 
  <br> customer - FK for customer 
  <br> total_check - price per flower from lot * amount 
  
- LotsReview, fields (created to track customer reviews for lot)
  <br> reviewed_lot - FK for lot 
  <br> author - FK for customer making the review
  <br> review 
  
- LotsReview, fields (created to track customer reviews for sellers)
  <br> reviewed_seller - FK for seller
  <br> author - FK for customer making the review
  <br> review 
  
  
 2. Function seller (stored in views.py) 
    <br> retuns a dictionary, where keys are sellers and values are dicts with customers and checks for each customer made from buying flowers from a particular seller) 

  
  
  
  
  
