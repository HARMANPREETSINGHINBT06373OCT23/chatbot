from flask import Flask, render_template, request, jsonify
import random
from database import init_db, save_conversation, get_conversations

app = Flask(__name__)

# Initialize the database
init_db()

# Predefined responses for the chatbot
responses = {
    
    "hi bejejjee": "Hello! How can I assist you today?",
    "how are you": "I'm good, thank you! How about you?",
        "who is your owner": "an 3rd yr engineering student",
 "Help":"yes ask me",
    "bye": "Goodbye! Have a great day!"
   
   
  "WHAT DEVICES DO YOU SELL" "We offer a wide range of tech devices including smartphones, laptops, tablets, headphones, and smartwatches.",
  "can i track my order": "Yes, once your order is shipped, you will receive a tracking number to monitor its status.",
  "CAN I TRACK MY ORDER": "Yes, once your order is shipped, you will receive a tracking number to monitor its status.",
  "how long does delivery take": "Delivery times vary based on your location, but typically it takes between 3 to 7 business days.",
  "HOW LONG DOES DELIVERY TAKE": "Delivery times vary based on your location, but typically it takes between 3 to 7 business days.",
  "do you offer international shipping": "Yes, we do offer international shipping to many countries. You can check the shipping options at checkout.",
  "DO YOU OFFER INTERNATIONAL SHIPPING": "Yes, we do offer international shipping to many countries. You can check the shipping options at checkout.",
  "what payment methods do you accept": "We accept payments via credit/debit cards, PayPal, Apple Pay, and Google Pay.",
  "WHAT PAYMENT METHODS DO YOU ACCEPT": "We accept payments via credit/debit cards, PayPal, Apple Pay, and Google Pay.",
  "is there a warranty on products": "Yes, most products come with a manufacturer's warranty. Please check the specific product details for more information.",
  "IS THERE A WARRANTY ON PRODUCTS": "Yes, most products come with a manufacturer's warranty. Please check the specific product details for more information.",
  "can i return an item": "Yes, we accept returns within 30 days of purchase, as long as the item is in its original condition.",
  "CAN I RETURN AN ITEM": "Yes, we accept returns within 30 days of purchase, as long as the item is in its original condition.",
  "how do i return an item": "You can initiate a return through your account or contact our customer service team for assistance.",
  "HOW DO I RETURN AN ITEM": "You can initiate a return through your account or contact our customer service team for assistance.",
  "do you have a loyalty program": "Yes, we offer a rewards program where you can earn points on purchases and redeem them for discounts.",
  "DO YOU HAVE A LOYALTY PROGRAM": "Yes, we offer a rewards program where you can earn points on purchases and redeem them for discounts.",
  "can i use multiple discount codes": "No, you can only use one discount code per order.",
  "CAN I USE MULTIPLE DISCOUNT CODES": "No, you can only use one discount code per order.",
  "do you offer gift cards": "Yes, we offer gift cards in various denominations. You can purchase them on our website.",
  "DO YOU OFFER GIFT CARDS": "Yes, we offer gift cards in various denominations. You can purchase them on our website.",
  "how do i cancel my order": "Orders can be canceled before they are shipped. Please contact our customer service team for assistance.",
  "HOW DO I CANCEL MY ORDER": "Orders can be canceled before they are shipped. Please contact our customer service team for assistance.",
  "can i change my shipping address": "If your order has not been shipped yet, we can update your shipping address. Please contact us immediately.",
  "CAN I CHANGE MY SHIPPING ADDRESS": "If your order has not been shipped yet, we can update your shipping address. Please contact us immediately.",
  "is my information secure": "Yes, we use the latest encryption technology to ensure your personal and payment details are secure.",
  "IS MY INFORMATION SECURE": "Yes, we use the latest encryption technology to ensure your personal and payment details are secure.",
  "how do i contact customer service": "You can contact our customer service through email, phone, or live chat on our website.",
  "HOW DO I CONTACT CUSTOMER SERVIC": "You can contact our customer service through email, phone, or live chat on our website.",
  "can i get a discount on bulk orders": "Yes, we offer discounts for bulk purchases. Please contact us for more details.",
  "CAN I GET A DISCOUNT ON BULK ORDERS": "Yes, we offer discounts for bulk purchases. Please contact us for more details.",
  "what is the return policy": "You can return products within 30 days of receipt as long as the item is unused and in its original packaging.",
  "WHAT IS THE RETURN POLICY": "You can return products within 30 days of receipt as long as the item is unused and in its original packaging.",
  "do you offer student discounts": "Yes, we offer student discounts on select products. Please verify your student status during checkout.",
  "DO YOU OFFER STUDENT DISCOUNTS": "Yes, we offer student discounts on select products. Please verify your student status during checkout.",
  "can i pre-order an item": "Yes, you can pre-order items that are not yet released. You will be notified when the product ships.",
  "CAN I PRE-ORDER AN ITEM": "Yes, you can pre-order items that are not yet released. You will be notified when the product ships.",
  "are there any hidden fees": "No, all fees are disclosed at checkout before you confirm your order.",
  "ARE THERE ANY HIDDEN FEES": "No, all fees are disclosed at checkout before you confirm your order.",
  "do you accept returns on electronics" : "Yes, electronics can be returned if they are unopened and in their original condition.",
  "DO YOU ACCEPT RETURNS ON ELECTRONICS": "Yes, electronics can be returned if they are unopened and in their original condition.",
  "do you offer extended warranties" : "Yes, extended warranties are available for many of our products. Check the product page for options.",
  "DO YOU OFFER EXTENDED WARRANTIES": "Yes, extended warranties are available for many of our products. Check the product page for options.",
  "are the devices refurbished" : "Some of our devices are refurbished and come with a warranty. You can find this information on the product page.",
  "ARE THE DEVICES REFURBISHED": "Some of our devices are refurbished and come with a warranty. You can find this information on the product page.",
  "can i get technical support" : "Yes, we provide technical support for all products. You can contact us for troubleshooting and assistance.",
  "CAN I GET TECHNICAL SUPPORT": "Yes, we provide technical support for all products. You can contact us for troubleshooting and assistance.",
  "what brands do you carry" : "We carry top tech brands like Apple, Samsung, Dell, HP, Bose, and more.",
  "WHAT BRANDS DO YOU CARRY": "We carry top tech brands like Apple, Samsung, Dell, HP, Bose, and more.",
  "how do i know if a product is in stock?" : "The product page will show if an item is in stock. If it's out of stock, we will notify you when it's available.",
  "HOW DO I KNOW IF A PRODUCT IS IN STOCK?": "The product page will show if an item is in stock. If it's out of stock, we will notify you when it's available.",
  "do you have a physical store?" : "We operate online only, but we do have partner locations where you can see some products in person.",
  "DO YOU HAVE A PHYSICAL STORE?": "We operate online only, but we do have partner locations where you can see some products in person.",
  "can i gift wrap my order?" : "Yes, we offer gift wrapping services at checkout.",
  "CAN I GIFT WRAP MY ORDER?": "Yes, we offer gift wrapping services at checkout.",
  "is there an option for express shipping?" : "Yes, we offer express shipping options at checkout for faster delivery.",
  "IS THERE AN OPTION FOR EXPRESS SHIPPING?": "Yes, we offer express shipping options at checkout for faster delivery.",
  "can i get a product demo?" : "We offer product demos in certain locations. Please contact us for more information.",
  "CAN I GET A PRODUCT DEMO?": "We offer product demos in certain locations. Please contact us for more information.",
  "how do i unsubscribe from emails?" : "You can unsubscribe from our emails by clicking the unsubscribe link at the bottom of any email we send.",
  "HOW DO I UNSUBSCRIBE FROM EMAILS?": "You can unsubscribe from our emails by clicking the unsubscribe link at the bottom of any email we send.",
  "do you offer free shipping?" : "Yes, we offer free standard shipping on orders over a certain amount. Check our shipping page for more details.",
  "DO YOU OFFER FREE SHIPPING?": "Yes, we offer free standard shipping on orders over a certain amount. Check our shipping page for more details.",
  "are your products certified?" : "Yes, all of our products are certified and meet the necessary safety and quality standards.",
  "ARE YOUR PRODUCTS CERTIFIED?": "Yes, all of our products are certified and meet the necessary safety and quality standards.",
  "which laptops do you recommend for gaming?" : "We recommend laptops like the ASUS ROG series, Alienware, and MSI gaming laptops for a great gaming experience.",
  "WHICH LAPTOPS DO YOU RECOMMEND FOR GAMING?": "We recommend laptops like the ASUS ROG series, Alienware, and MSI gaming laptops for a great gaming experience.",
  "what is the best smartphone for photography?" : "The latest iPhone 15 Pro and Samsung Galaxy S24 Ultra are known for their excellent camera quality.",
  "WHAT IS THE BEST SMARTPHONE FOR PHOTOGRAPHY?": "The latest iPhone 15 Pro and Samsung Galaxy S24 Ultra are known for their excellent camera quality.",
  "do you offer budget smartphones?" : "Yes, we offer affordable smartphones from brands like Xiaomi, Realme, and Motorola.",
  "DO YOU OFFER BUDGET SMARTPHONES?": "Yes, we offer affordable smartphones from brands like Xiaomi, Realme, and Motorola.",
  "what tablets are good for drawing?" : "The Apple iPad Pro with Apple Pencil and the Samsung Galaxy Tab S8 are great options for digital artists.",
  "WHAT TABLETS ARE GOOD FOR DRAWING?": "The Apple iPad Pro with Apple Pencil and the Samsung Galaxy Tab S8 are great options for digital artists.",
  "which smartwatch is best for fitness?" : "The Apple Watch Series 9 and Garmin Forerunner series are excellent choices for fitness tracking.",
  "WHICH SMARTWATCH IS BEST FOR FITNESS?": "The Apple Watch Series 9 and Garmin Forerunner series are excellent choices for fitness tracking.",
  "can i upgrade the RAM in my laptop?" : "Some laptops allow RAM upgrades, but it depends on the model. Please check the product specifications for details.",
   "ok": "okay",
   "ji":"ji",
   "what devices do you sell?": "We offer a wide range of tech devices including smartphones, laptops, tablets, headphones, and smartwatches.",
  "WHAT DEVICES DO YOU SELL?": "We offer a wide range of tech devices including smartphones, laptops, tablets, headphones, and smartwatches.",
  "can i track my order?": "Yes, once your order is shipped, you will receive a tracking number to monitor its status.",
  "CAN I TRACK MY ORDER?": "Yes, once your order is shipped, you will receive a tracking number to monitor its status.",
  "how long does delivery take?": "Delivery times vary based on your location, but typically it takes between 3 to 7 business days.",
  "HOW LONG DOES DELIVERY TAKE?": "Delivery times vary based on your location, but typically it takes between 3 to 7 business days.",
  "do you offer international shipping?": "Yes, we do offer international shipping to many countries. You can check the shipping options at checkout.",
  "DO YOU OFFER INTERNATIONAL SHIPPING?": "Yes, we do offer international shipping to many countries. You can check the shipping options at checkout.",
  "what payment methods do you accept?": "We accept payments via credit/debit cards, PayPal, Apple Pay, and Google Pay.",
  "WHAT PAYMENT METHODS DO YOU ACCEPT?": "We accept payments via credit/debit cards, PayPal, Apple Pay, and Google Pay.",
  "is there a warranty on products?": "Yes, most products come with a manufacturer's warranty. Please check the specific product details for more information.",
  "IS THERE A WARRANTY ON PRODUCTS?": "Yes, most products come with a manufacturer's warranty. Please check the specific product details for more information.",
  "can i return an item?": "Yes, we accept returns within 30 days of purchase, as long as the item is in its original condition.",
  "CAN I RETURN AN ITEM?": "Yes, we accept returns within 30 days of purchase, as long as the item is in its original condition.",
  "how do i return an item?": "You can initiate a return through your account or contact our customer service team for assistance.",
  "HOW DO I RETURN AN ITEM?": "You can initiate a return through your account or contact our customer service team for assistance.",
  "do you have a loyalty program?": "Yes, we offer a rewards program where you can earn points on purchases and redeem them for discounts.",
  "DO YOU HAVE A LOYALTY PROGRAM?": "Yes, we offer a rewards program where you can earn points on purchases and redeem them for discounts.",
  "can i use multiple discount codes?": "No, you can only use one discount code per order.",
  "CAN I USE MULTIPLE DISCOUNT CODES?": "No, you can only use one discount code per order.",
  "do you offer gift cards?": "Yes, we offer gift cards in various denominations. You can purchase them on our website.",
  "DO YOU OFFER GIFT CARDS?": "Yes, we offer gift cards in various denominations. You can purchase them on our website.",
  "how do i cancel my order?": "Orders can be canceled before they are shipped. Please contact our customer service team for assistance.",
  "HOW DO I CANCEL MY ORDER?": "Orders can be canceled before they are shipped. Please contact our customer service team for assistance.",
  "can i change my shipping address?": "If your order has not been shipped yet, we can update your shipping address. Please contact us immediately.",
  "CAN I CHANGE MY SHIPPING ADDRESS?": "If your order has not been shipped yet, we can update your shipping address. Please contact us immediately.",
  "is my information secure?": "Yes, we use the latest encryption technology to ensure your personal and payment details are secure.",
  "IS MY INFORMATION SECURE?": "Yes, we use the latest encryption technology to ensure your personal and payment details are secure.",
  "how do i contact customer service?": "You can contact our customer service through email, phone, or live chat on our website.",
  "HOW DO I CONTACT CUSTOMER SERVICE?": "You can contact our customer service through email, phone, or live chat on our website.",
  "can i get a discount on bulk orders?": "Yes, we offer discounts for bulk purchases. Please contact us for more details.",
  "CAN I GET A DISCOUNT ON BULK ORDERS?": "Yes, we offer discounts for bulk purchases. Please contact us for more details.",
  "what is the return policy?": "You can return products within 30 days of receipt as long as the item is unused and in its original packaging.",
  "WHAT IS THE RETURN POLICY?": "You can return products within 30 days of receipt as long as the item is unused and in its original packaging.",
  "do you offer student discounts?": "Yes, we offer student discounts on select products. Please verify your student status during checkout.",
  "DO YOU OFFER STUDENT DISCOUNTS?": "Yes, we offer student discounts on select products. Please verify your student status during checkout.",
  "can i pre-order an item?": "Yes, you can pre-order items that are not yet released. You will be notified when the product ships.",
  "CAN I PRE-ORDER AN ITEM?": "Yes, you can pre-order items that are not yet released. You will be notified when the product ships.",
  "are there any hidden fees?": "No, all fees are disclosed at checkout before you confirm your order.",
  "ARE THERE ANY HIDDEN FEES?": "No, all fees are disclosed at checkout before you confirm your order.",
  "do you accept returns on electronics?" : "Yes, electronics can be returned if they are unopened and in their original condition.",
  "DO YOU ACCEPT RETURNS ON ELECTRONICS?": "Yes, electronics can be returned if they are unopened and in their original condition.",
  "do you offer extended warranties?" : "Yes, extended warranties are available for many of our products. Check the product page for options.",
  "DO YOU OFFER EXTENDED WARRANTIES?": "Yes, extended warranties are available for many of our products. Check the product page for options.",
  "are the devices refurbished?" : "Some of our devices are refurbished and come with a warranty. You can find this information on the product page.",
  "ARE THE DEVICES REFURBISHED?": "Some of our devices are refurbished and come with a warranty. You can find this information on the product page.",
  "can i get technical support?" : "Yes, we provide technical support for all products. You can contact us for troubleshooting and assistance.",
  "CAN I GET TECHNICAL SUPPORT?": "Yes, we provide technical support for all products. You can contact us for troubleshooting and assistance.",
  "what brands do you carry?" : "We carry top tech brands like Apple, Samsung, Dell, HP, Bose, and more.",
  "WHAT BRANDS DO YOU CARRY?": "We carry top tech brands like Apple, Samsung, Dell, HP, Bose, and more.",
  "how do i know if a product is in stock?" : "The product page will show if an item is in stock. If it's out of stock, we will notify you when it's available.",
  "HOW DO I KNOW IF A PRODUCT IS IN STOCK?": "The product page will show if an item is in stock. If it's out of stock, we will notify you when it's available.",
  "do you have a physical store?" : "We operate online only, but we do have partner locations where you can see some products in person.",
  "DO YOU HAVE A PHYSICAL STORE?": "We operate online only, but we do have partner locations where you can see some products in person.",
  "can i gift wrap my order?" : "Yes, we offer gift wrapping services at checkout.",
  "CAN I GIFT WRAP MY ORDER?": "Yes, we offer gift wrapping services at checkout.",
  "is there an option for express shipping?" : "Yes, we offer express shipping options at checkout for faster delivery.",
  "IS THERE AN OPTION FOR EXPRESS SHIPPING?": "Yes, we offer express shipping options at checkout for faster delivery.",
  "can i get a product demo?" : "We offer product demos in certain locations. Please contact us for more information.",
  "CAN I GET A PRODUCT DEMO?": "We offer product demos in certain locations. Please contact us for more information.",
  "how do i unsubscribe from emails?" : "You can unsubscribe from our emails by clicking the unsubscribe link at the bottom of any email we send.",
  "HOW DO I UNSUBSCRIBE FROM EMAILS?": "You can unsubscribe from our emails by clicking the unsubscribe link at the bottom of any email we send.",
  "do you offer free shipping?" : "Yes, we offer free standard shipping on orders over a certain amount. Check our shipping page for more details.",
  "DO YOU OFFER FREE SHIPPING?": "Yes, we offer free standard shipping on orders over a certain amount. Check our shipping page for more details.",
  "are your products certified?" : "Yes, all of our products are certified and meet the necessary safety and quality standards.",
  "ARE YOUR PRODUCTS CERTIFIED?": "Yes, all of our products are certified and meet the necessary safety and quality standards."
  "CAN I UPGRADE THE RAM IN MY LAPTOP?" "Some laptops allow RAM upgrades, but it depends on the model. Please check the product specifications for details."
 

}

# Default chatbot response
def get_bot_reply(user_message):
    return responses.get(user_message.lower(), "Sorry, I don't understand that.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    bot_reply = get_bot_reply(user_message)
    
    # Save conversation in the database
    save_conversation(user_message, bot_reply)
    
    # Send response back to the frontend
    return jsonify({"user_message": user_message, "bot_reply": bot_reply})

@app.route('/history', methods=['GET'])
def history():
    conversations = get_conversations()
    return jsonify(conversations)

if __name__ == '__main__':
    app.run(debug=True)
