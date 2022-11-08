class Category:
#Defining all list as a class paramater to store the names of the objects in case we needed them later    
    all=[]

    def __init__(self,name):
        # Defining ledger paramater for intences
        self.ledger=list()
        self.name=name
        # Total_spending will store the sum of all withdrawals for one category
        self.total_spending=float()
        Category.all.append(self)# Adding names of the objects to all list 
        
    """
    A deposit method that accepts an amount and description. 
    If no description is given, it should default to an empty string. 
    The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
    """
    
    def deposit(self,amount,description=''):
        self.ledger.append({'amount':amount, 'description':description})
    
    """
    A withdraw method that is similar to the deposit method, 
    but the amount passed in should be stored in the ledger as a negative number. 
    If there are not enough funds, nothing should be added to the ledger. 
    This method should return True if the withdrawal took place, and False otherwise.
    """
    
    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount':(-amount), 'description':description})
          #Defining total spending we will need it later
            self.total_spending+=amount 
            return(True)
        else:
            return(False)
    
    """
    A get_balance method that returns the current balance of the budget category 
    based on the deposits and withdrawals that have occurred.
    """
    
    def get_balance(self):
        self.balance=0
        for i in self.ledger:
            self.balance+=i['amount']
        return(self.balance)
    
    def check_funds(self,control_amount):
        if control_amount>self.get_balance():
            return(False)
        else:
            return(True)
    
    """
    A transfer method that accepts an amount and another budget category as arguments. 
    The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
    The method should then add a deposit to the other budget category
    with the amount and the description "Transfer from [Source Budget Category]". 
    If there are not enough funds, nothing should be added to either ledgers. 
    This method should return True if the transfer took place, and False otherwise.
    """
    
    def transfer(self,transfer_amount,budget_category):
        if self.check_funds(transfer_amount):
            self.ledger.append({'amount':(-transfer_amount), 'description':(f'Transfer to {budget_category.name}')})
            budget_category.deposit(transfer_amount,f'Transfer from {self.name}')# Using previously defined method 
            return(True)
        else:
            return(False)
    # Formatting object table 
    def __repr__(self):
        rows=''
        for i in self.ledger:
            rows=rows+i['description'][0:23].ljust(23)+str(format(i['amount'],'.2f'))[0:7].rjust(7)+'\n'
        return f"{(self.name).center(30,'*')}\n{rows.strip()}\nTotal: {self.get_balance()}"

#Creating chart 
def create_spend_chart(list_of_categories):
    overall_spending=0
    max_len=0
    for i in list_of_categories:
        overall_spending+=i.total_spending
    percentages={}
    #Percentages are actually 0-10 integer in following code
    #This format will enable us to create chart 
    for i in list_of_categories:
        percentages[i.name]=int((i.total_spending/overall_spending*100)/10)
        if len(i.name)>max_len:
            max_len=len(i.name)
    chart='Percentage spent by category\n'
    for i in range (100,-1,-10):
        chart+=f'{str(i).rjust(3)}|'
        for a in percentages:
            if percentages[a]<i/10:
                chart+=3*' '
            else:
                chart+=' o '
        chart+=' \n'
    dashes=len(list_of_categories)*3*'-'+'-'
    chart+=f'    {dashes}\n'
    

    for i in range(max_len):
        chart+=' '*4
        for k in percentages.keys():
            if i<len(k):
                chart+=' '+k[i]+' '
            else:
                chart+=' '*3
        chart+=' \n'
    return(chart).rstrip('\n')
    