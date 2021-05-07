# bankingsystem
You have created the foundation of our banking system. Now let's take the opportunity to deposit money into an account, make transfers and close an account if necessary.  
Now your menu should look like this:  
1. Balance 
2. Add income 
3. Do transfer 
4. Close account 
5. Log out 0.
 
<b> Exit If the user asks for Balance, you should read the balance of the account from the database and output it into the console. 
Add income item should allow us to deposit money to the account. Do transfer item should allow transferring money to another account. You should handle the following errors:</b> 
1. If the user tries to transfer more money than he/she has, output: Not enough money!
2. If the user tries to transfer money to the same account, output the following message: You can't transfer money to the same account!
3. If the receiver's card number doesn’t pass the Luhn algorithm, you should output: Probably you made a mistake in the card number. Please try again! 
4. If the receiver's card number doesn’t exist, you should output: Such a card does not exist. 
5. If there is no error, ask the user how much money they want to transfer and make the transaction. 
If the user chooses the Close account item, you should delete that account from the database.  Do not forget to commit your DB changes right after executing a query! Examples The symbol > represents the user input. Notice that it's not a part of the input.  

<b>Example 1:</b>  
1. Create an account 
2. Log into account 
0. Exit 

>1  

<b>Your card has been created</b> 

<b>Your card number:</b> 4000009455296122 

<b>Your card PIN:</b> 1961  

1. Create an account 
2. Log into account
0. Exit 

>1  

<b>Your card has been created</b> 

<b>Your card number:</b> 4000003305160034 

<b>Your card PIN:</b> 5639  

1. Create an account 
2. Log into account 
0. Exit 

>2  

<b>Enter your card number: </b>
>4000009455296122 

<b>Enter your PIN:</b> 
>1961  

<b>You have successfully logged in!</b>  

1. Balance 
2. Add income 
3. Do transfer 
4. Close account 
5. Log out 
0. Exit 
>2  

<b>Enter income: </b>
>10000 

<b>Income was added!</b> 

1. Balance 
2. Add income 
3. Do transfer 
4. Close account 
5. Log out 
0. Exit 
>1  

<b>Balance:</b> 10000

1. Balance 
2. Add income 
3. Do transfer 
4. Close account 
5. Log out 
0. Exit 
>3  

<b>Transfer Enter card number: </b>
>4000003305160035 

<b>Probably you made a mistake in the card number. Please try again!</b>  

1. Balance 
2. Add income 
3. Do transfer 
4. Close account 
5. Log out 
0. Exit 
>3  

<b>Transfer Enter card number: </b>
>4000003305061034 

<b>Such a card does not exist.</b> 

1. Balance 
2. Add income 
3. Do transfer 
4. Close account 
5. Log out 
0. Exit 
>3  

<b>Transfer Enter card number: </b>
>4000003305160034 

<b>Enter how much money you want to transfer:</b> 
>15000 

<b>Not enough money!</b> 

1. Balance 
2. Add income 
3. Do transfer 
4. Close account 
5. Log out 
0. Exit 
>3  

<b>Transfer Enter card number: </b>
>4000003305160034 

<b>Enter how much money you want to transfer:</b> 
>5000 

<b>Success!</b>  

1. Balance 
2. Add income 
3. Do transfer 
4. Close account 
5. Log out 
0. Exit
>1  

<b>Balance:</b> 5000 

1. Balance 
2. Add income 
3. Do transfer 
4. Close account 
5. Log out 
0. Exit  
>0 

<b> Bye!</b>
