from aiogram import executor,Dispatcher,Bot,types

api_key="5738749831:AAHcNuNUdtyPospKQMLchZJkxh8sueiMgH0"
bot_obj=Bot(token=api_key)
bot=Dispatcher(bot_obj)



@bot.message_handler()
async def echo_all(message:types.Message):
    questions=[
        ["What is Blockorry About?","Blockorry - Professional team of cryptocurrency industry developers. The main advantage of the company is a unique trading bot that makes a profit at the stage of growth and market decline. Our team is ready to go above and beyond to give investor the best return on investment possible. Blockorry has also sign partnership deals with many big companies all over the world to ensure a steady profit margin to its investors."],
        ["HOW MANY ACCOUNTS CAN I OPEN?","Each user can only open and manage one account. Please follow this rule. In case of violation the company has the right to block all your accounts without a refund."],
        ["HOW MUCH DOES IT COST TO OPEN AN ACCOUNT?","Opening an account is absolutely free. We do not charge you any hidden fees or service charges. The commission on operations and additional costs is included in the company's profits from the profits from the development of cryptocurrency robots."],
        ["HOW TO BECOME AN INVESTOR?","""
        3 steps to get started with our company
        1. REGISTRATION BUTTON
        Click the Register button. Enter your details to quickly create a FREE Blockorry account.
        2. OPEN A DEPOSIT
        Deposit funds in your Blockorry account from any crypto currency exchanger. 
        3. Buy Plan
        We offer different investment plans. You need to choose a plan that suits your financial goals.
        4. START EARNING
        After you buy a plan, watch your capital grow by accumulating hourly profit in real time.
        """],
        ["How long have this company last?","Blockorry was created in June 2022, with the name Blockonics which was later rebranded to Blockorry."],
        ["HOW CAN I DOWNLOAD BLOCK ZILLER APP ON GOOGLE PLAYSTORE? ","Click link https://play.google.com/store/apps/details?id=online.blockziller.blockziller to download app from google play store. If you have iPhone, kindly click link https://blockziller.com/ to access our platform using a browser, both app and browser have the same layout."],
        ["I WILL LIKE TO KNOW MORE ABOUT BLOCKORRY TOKEN.","Kindly download our white paper on our app or browser to read more about out Block Ziller token."],
        ["HOW CAN I DOWNLOAD BLOCKORRY APP ON PLAYSTORE? ","Click link https://play.google.com/store/apps/details?id=online.blockonics.blockonics to download app from google play store. If you have iPhone, kindly click link https://www.blockorry.com/ to access our platform using a browser, both app and browser have the same layout."],
        ["CAN I MAKE MULTIPLE DEPOSITS AT THE SAME TIME?","Yes, you can have an unlimited number of deposits, and you can also invest in different tariff plans at the same time."],
        ["HOW DO I INVEST ON BLOCKORRY?","""
        -	Create an account, use the username and password you entered during registration, 
        -	log into your account. Click the "Deposit" button. 
        -	Enter the amount you plan to invest. After confirming the amount and choosing an electronic payment system, you will be redirected to the electronic payment system. Follow her instructions to pay for the transaction. 
        -	Then you will be redirected back to your Personal Account again. Funds will be credited automatically into your account balance.
        -	Click on “Investment Plants” Button
        -	Select investment plant from the drop down menu.
        -	Enter amount you want to invest.
        -	Click on “Confirm & invest” Button, check your account hourly to see your profit.
        """],
        ["ARE THERE ANY RESTRICTIONS ON THE AMOUNT OF INVESTMENT ON BLOCKORRY?","The tariff plans set the following restrictions on the minimum and maximum amount of the deposit. Minimum Amount: 20 USD, Maximum Amount: 500000 USD."],
        ["WHAT PAYMENT METHODS CAN I USE TO DEPOSIT?","We work with payment systems BitCoin, Ethereum, LiteCoin, TRON, USDT.TRC20."],
        ["WHAT ARE THE INVESTMENTS PLANS ON BLOCKORRY?","""
        They are three investment plans,
        -	Basic Plan ($20-$10,000, profit 0.11 per hour).
        -	Standard Plan ($10,001-$100,000, profit 0.13 per hour).
        -	Advanced Plan ($100,001-$500,000, profit 0.15 per hour).
        """],
        ["WHAT ARE THE CRYPTO CURRENCIES USED TO IN BUYING BLOCKORRY TOKEN?","Block Ziller token can be bought with Bitcoin and Litcoin"]
        ["HOW CAN I BUY BLOCK ZILLER TOKEN?","""
        -	Create and account on Block Ziller app or website.
        -	Log in to your account.
        -	Connect your BNB wallet address.
        -	Click on “Buy Token Now” Button.
        -	Select crypto Currency.
        -	Enter quantity of BKZ you want to buy.
        -	Click on “Make Payment” Button and follow the steps to complete payment.
        """],
        ["IS BLOCKORRY A REGISTRERED COMPANY?","Yes, we are legally binding and officially registered in the US under the company registration number #13699699."],
        ["Where is Blockorry LTD Company located?","Blockorry head office is located in Los Angeles, CA, USA"],
        ["HOW CAN I GUARRANTEE MY INVESTMENT WITH BLOCKORRY? ","Blockorry has up to 457 trading expert from Japan, USA, India, Russia and UK who are the best in their field. Also, Blockorry experts works with a high level AI which predict trades at all levels to guarantee a high level of return of investors."],
        ["WHO IS THE CEO OF THE BLOCKORRY LTD COMPANY?","Blockorry is an organization of a group of 189 cryptocurrency trading experts with high level of technology and artificial intelligence. It is not own by any individual rather it is a group of experts. "],
        ["DO I GET MY INVESTMENT CAPITAL AFTER MY PLAN EXPIRES? ","YES, the amount you invested will be refunded to your account balance after 30 days when your plan have expired. You can withdraw your invested capital or reinvest it if you want, it is entire up to you."],
        ["WHAT IS THE MINIMUM QUANTITY TO BUY A BLOCK ZILLER TOKEN?","Minimum purchase quantity will be 5BKZ."],
        ["DOES BLOCK ZILLER GIVE BONUSES ","""
        •	Purchase below 50BKZ will receive a 3% addition bonus. 
        •	Purchase above 50BKZ + will receive 5% additional bonus.
        •	Purchase above 100BKZ+ will receive a 100BKZ will have 7% additional bonus.
        •	Purchase above 1000BKZ+ will receive 10+ additional bonus.
        """],
        ["HOW CAN I CONTACT BLOCKORRY SUPPORT FOR FORTHER ASSISTANCE?","""  
        You can contact Blockorry support on telegram via 
        -	username: @Blockonics_support
        -	or click link: https://telegram.me/Blockonics_support
        """],
        ["CAN I LOSE MY FUNDS BY INVESTING IN BLOCKORRY?","Your investment, as well as your loyalty, are our core values. We will work hard to preserve your funds, reduce the risk of loss to zero, and we will do our best to multiply your funds."],
        ["21.	IS IT POSSIBLE TO INCREASE THE AMOUNT OF THE WORKING DEPOSIT?","No, you cannot increase the amount of a deposit that has already been created. However, you can create other unlimited deposits."],
        ["22.	HOW LONG DOES IT TAKE TO PROCESS A WITHDRAWAL REQUEST?","""
        Withdrawal requests will be processed instantly. 
        -  Waiting time for funds to a wallet for payment systems USDT.TRC20 is at least 3 network confirmations are required and this can take from 20 minutes to several hours and not more than 6 hours.
        """],
        ["23.	CAN I CHOOSE ANOTHER PAYMENT SYSTEM FOR WITHDRAWAL?","  No, withdrawals are made only in USDT.TRC20."],

        ["24.	WHAT ARE THE PROCEEDURE FOR WITHDRAWAL OF FUNDS TO A PERSONAL WALLET?","""Before withdrawing funds, be sure to check if you have indicated the correct address of your payment wallet to which you will be withdrawing. If you have not registered a wallet, do it by going to the "Wallets" section of your account. In the same section you can always edit your payment details.
        After you have made sure that the entered data is correct, you need to go to the 'Withdrawal' section located in your investor's personal account, select the payment system to which you want to withdraw, enter the withdrawal amount and click the withdrawal button funds.
        """],
        ["25.	WHAT IS THE MINIMUM WITHDRAWAL AMOUNT? AND IS THERE A LIMITATION ON THE NUMBER OF WITHDRAWALS OR AMOUNTS PER DAY?","The minimum withdrawal amount is: 20 USD, there are no restrictions on the number of withdrawal operations per day."],
        ["26.	DO YOU OFFER A REFERRAL PROGRAM?","We offer an affiliate program for additional income for our investors. Anyone can take part in the development of the company by inviting new members and receiving a generous reward for this."],
        ["27.	HOW DOES BLOCKORRY AFFILIATE PROGRAM WORK?","Blockorry offers a unique investment and referral program that rewards you not only for partners who came from you to the platform, but also for partners from levels 2,3 and 4. This unique affiliate program brings you passive referral income. First, you earn by inviting friends to Blockorry, and then you earn when people in your structure refer new investors to the company. Affiliate system level: 7% - 3% - 2% - 1%."],
        ["28.	DOES BLOCK ZILLER HAVE A REFERRAL PROGRAM? ","""
        -	Who Joined receives 2BKZ (if you join Block Ziller Platform and buy through a referral link).
        -	Who Referred receives 5% (if you invite a new user to buy BKZ using your referral link)
        """],
    ]

    for question in questions:
        if(question[0].lower() in message['text'] or question[0].capitalize() in message['text'] or question[0] in message['text']):
            await message.reply(question[1])
    
    
    


@bot.message_handler(content_types=[types.ContentType.NEW_CHAT_MEMBERS, types.ContentType.LEFT_CHAT_MEMBER])
async def user_joined_chat(message: types.Message):
    print(message)


executor.start_polling(bot)
