#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Restaurant Management System
class RMS:
    
    def __init__(self,restaurant_name,menu):
        self.restaurant_name=restaurant_name
        self.total_bill=0
        self.menu=menu
        self.user_order=''
        self.user_paid=0
        self.ask_user=''
    #Welcome User
    def welcome_user(self): #Rohan
        return(f'welcome to {self.restaurant_name}!')
    #Display menu
    def display_menu(self):
        for i in self.menu:
            print(i.title(),self.menu[i])
        print('*'*30)
    #Take Order
    def take_order(self):
        self.user_order=input('Please place your order here:')
        
    #Prepare Order
    def preparing_order(self):
        import time
        print(f'Preparing your {self.user_order.title()}')
        time.sleep(0.3)
        self.total_bill=self.total_bill+self.menu[self.user_order.lower()]
    
    #Serve Order
    def serve_order(self):
        print(f'Your order is ready')
        print(f'Please enjoy your {self.user_order.title()}')
              
    #Display bill
    def display_bill(self):
              
        print('Your Total bill:',self.total_bill)
              
    #verify bill
    def verify_bill(self):
        self.user_paid=int(input('Please pay your bill here:'))
              
        while self.user_paid<self.total_bill:
            self.total_bill=self.total_bill-self.user_paid
            print(f'Payment Failed! Please Pay remaining: {self.total_bill}')
            self.user_paid=int(input('please pay your bill here:'))
              
        if self.user_paid>self.total_bill:
             print(f'Here is your change {self.user_paid-self.total_bill}')
              
        else:
             pass
    #Thank User
    def thank_user(self):
        print(f'Thank you for visiting {self.restaurant_name}!')
    def order_process(self):
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
           self.preparing_order()
           self.serve_order()
           self.ask_user=input('would you like to order again?')
           while self.ask_user.lower()=='yes':
               self.repeat_order()
               self.ask_user=input('would you like to order again?')
              
           self.display_bill()
           self.verify_bill()
           self.thank_user()
        else:
            print('Invalid order!')
            self.order_process()
              
              
    def repeat_order(self):
        self.take_order()
        if self.user_order.lower() in self.menu:
           self.preparing_order()
           self.serve_order()
        else:
            print('Invalid order!')
            self.repeat_order()
              
if __name__=='__main__':
    user_input_file=open('user input.txt')
    
    user_input_li=user_input_file.readlines()
    
    rn=user_input_li[0].replace('\n','')
    
    food_items=user_input_li[1].replace('\n','').split(',')
    
    food_prices=[]
    for i in user_input_li[2].split(','):
        food_prices.append(int(i))
        
    rm=dict(zip(food_items,food_prices))
    restuarant=RMS(restaurant_name=rn,menu=rm)
    import tkinter as tk
    
    
    window=tk.Tk()
    window.geometry('400x400')
    window.title(rn)
    tk.Label(window,text=restuarant.welcome_user(),font=('Helvetica',16)).pack(pady=30)
    tk.Button(window,text='MENU',command=restuarant.display_menu,width=15).pack(pady=40)
    tk.Button(window,text='START ORDER',command=restuarant.order_process,width=15).pack(pady=50)
    window.mainloop()
              
    


# In[ ]:




