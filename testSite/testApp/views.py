from django.shortcuts import render

from django.http import JsonResponse

from django.template import loader

from django.http import HttpResponse

from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_protect

from django.core import serializers

import ast



from .models import Sport
from .models import News
from .models import Bussiness
from .models import Account
#from .models import VerifyAccount
from .models import CurrentAccount
#from .models import VerifyLogIn
import json


obj2 ={}
newdata = {}
newdata2 = {}
newdata3 = {}
newdata4 = {}
newdata5 = {}
#veriAcc = {}
#veriLogIn = {}
#currAcc = {}
logInPwdData = ''
logInUsrData = ''
accVeriData = ''
isLoggedIn = ''
def mainPage(request):
    #template = loader.get_template('testPage.html')
    page = 'testPage.html'    
    #logging.info('INFO')
    return render(request, page)
    #return HttpResponse(template.render(), request)

def sport(request):
    #template = loader.get_template('sportsPage.html')
    sportPage = 'sportsPage.html'
    return render(request, sportPage)

def bussiness(request):
    #template = loader.get_template('bizPage.html')
    bizPage = 'bizPage.html'
    return render(request, bizPage) 

def account(request):
    #template = loader.get_template('testAccountPage.html')
    accountPage = 'testAccountPage.html'
    return render(request, accountPage)

def signup(request):
    #template = loader.get_template('testsignupPage.html')
    signPage = 'testsignupPage.html'
    return render(request, signPage)

def login(request):
    #template = loader.get_template('logInPage.html')
    logPage = 'logInPage.html'
    return render(request, logPage)
def accountInfo(request):
    infoPage = 'accountInfoPage.html'
    return render(request, infoPage)
    
def newsPage(request):
    news = 'newsPage.html'
    return render(request, news)

def download(request):
    if request.method == "GET":
        data = open('testApp\static\js\data.json')
        dictdata = json.load(data)
       
        
        '''
        News.objects.all().delete()
        Sport.objects.all().delete()
        Bussiness.objects.all().delete()
        Account.objects.all().delete()
        CurrentAccount.objects.all().delete()
        #'''
        
    
        '''   
        News.objects.create(
            title = dictdata['news']['title'],
            picture = dictdata['news']['picture'],
            text = dictdata['news']['text'],
            newsComments = dictdata['news']['newscomments'],
            category = "News"
        )
        
    
        Sport.objects.create(
            title = dictdata['sport']['title'],
            picture = dictdata['sport']['picture'],
            text = dictdata['sport']['text'],
            sportComments = dictdata['sport']['sportcomments'],
            category = "Sport"
        )
        
        Bussiness.objects.create(
            title = dictdata['bussiness']['title'],
            picture = dictdata['bussiness']['picture'],
            text = dictdata['bussiness']['text'],
            bizComments = dictdata['bussiness']['bizcomments'],
            category = "Bussiness"
        )
    
        Account.objects.create(
            accountArr = dictdata['account'],
            category = "Account"
        )

        CurrentAccount.objects.create(
            username = "null",
            password = "null",
            name = "null",
            phoneNumber = "null",
            newsPagelikeOrDislike = False,
            sportPagelikeOrDislike = False,
            bizPagelikeOrDislike = False,
            category = "Current Account"
        )
        #'''
        
        #'''
        print('sport %s' %Sport.objects.get(category='Sport').text)
        print('news %s' %News.objects.get(category='News').text)
        print('biz %s' %Bussiness.objects.get(category='Bussiness').text)
        print('account %s' %Account.objects.get(category='Account'))
        print('current account %s' %CurrentAccount.objects.get(category='Current Account').name)
        #'''
        global obj2
        global newdata
        global newdata2
        global newdata3
        global newdata4
        global newdata5
        global logInPwdData
        global logInUsrData
        global accVeriData
        global isLoggedIn
        
        obj =  []
        #'''
        if News.objects.all():
            obj.append(News.objects.all())
        if Sport.objects.all():
            obj.append(Sport.objects.all())
        if Bussiness.objects.all():
            obj.append(Bussiness.objects.all())
        if Account.objects.all():
            obj.append(Account.objects.all())
        if CurrentAccount.objects.all():
            obj.append(CurrentAccount.objects.all())
        #'''
        
        '''
        obj2 ={}
        newdata = {}
        newdata2 = {}
        newdata3 = {}
        newdata4 = {}
        newdata5 = {}
        logInPwdData = ''
        logInUsrData = ''
        accVeriData = ''
        isLoggedIn = ''
        #'''
        

        
        
        #'''
        #this gives you a list of dicts
        if not obj2:
            if len(obj)>=1 and not newdata:
                val = obj[0]
                raw_data = serializers.serialize('python', val)
                actual_data = raw_data[0]['fields']
                output = json.dumps(actual_data)
                newdata = json.loads(output)
                obj2.update(news=newdata)

            if len(obj)>=2 and not newdata2:
                val2 = obj[1]
                raw_data2 = serializers.serialize('python', val2)
                actual_data2 = raw_data2[0]['fields']
                output2 = json.dumps(actual_data2)
                newdata2 = json.loads(output2)
                obj2.update(sport=newdata2)
        
            if len(obj)>=3 and not newdata3:
                val3 = obj[2]
                raw_data3 = serializers.serialize('python', val3)
                actual_data3 = raw_data3[0]['fields']
                output3 = json.dumps(actual_data3)
                newdata3 = json.loads(output3)
                obj2.update(bussiness=newdata3)

            if len(obj)>=4 and not newdata4:    
                val4 = obj[3]
                raw_data4 = serializers.serialize('python', val4)
                actual_data4 = raw_data4[0]['fields']
                output4 = json.dumps(actual_data4)
                newdata4 = json.loads(output4)
                obj2.update(account=newdata4)

            if len(obj)>=5 and not newdata5:    
                val5 = obj[4]
                raw_data5 = serializers.serialize('python', val5)
                actual_data5 = raw_data5[0]['fields']
                output5 = json.dumps(actual_data5)
                newdata5 = json.loads(output5)
                obj2.update(currentAccount=newdata5)

                if not accVeriData:
                    accVeriData = "empty"
                if not logInUsrData:
                    logInUsrData = "empty"
                if not logInPwdData:
                    logInPwdData = "empty"
                if not isLoggedIn:
                    isLoggedIn = "notLoggedIn"
                obj2.update(isNewAccount=accVeriData)
                obj2.update(usernameExists=logInUsrData)
                obj2.update(passwordExists=logInPwdData)
                obj2.update(isLoggedIn=isLoggedIn)

        #'''

        #print('obj2 %s'%obj2)
        #print('newdata %s'%newdata)
        #print('newdata2 %s'%newdata2)
        #print('newdata3 %s'%newdata3)
        #print('newdata4 %s'%newdata4)
        

        return JsonResponse(obj2, safe=False)
    else:
        return HttpResponse('no get', request)
        
def create(request):
    if request.method == "POST":

        global obj2
        global newdata
        global newdata2
        global newdata3
        global newdata4
        global newdata5
        global logInPwdData
        global logInUsrData
        global accVeriData
        global isLoggedIn
      
        print('post: %s'%request.POST['section'])
        
    
        section = request.POST['section'] 
        
        #'''
        if section == 'News':
            newsObj = News.objects.get(category='News')
            theTitle = newsObj.title
            thePic = newsObj.picture
            theText = newsObj.text
            nc = newsObj.newsComments
            News.objects.all().delete()
            nc = nc.replace("'", "\"")
            nc = json.loads(nc)
            print("in news")
            print("comment: %s" %request.POST['comment'])
            nc.append({"comment": request.POST['comment']})

        
            News.objects.create(
                title = theTitle,
                picture = thePic,
                text = theText,
                newsComments = nc,
                category='News'
            )
            print('current cat %s'%newsObj.category)

        if section == 'Sport':
            sportObj = Sport.objects.get(category='Sport')
            #print('id %s'%newsObj.id)
            theTitle = sportObj.title
            thePic = sportObj.picture
            theText = sportObj.text
            snc = sportObj.sportComments
            Sport.objects.all().delete()
            snc = snc.replace("'", "\"")
            snc = json.loads(snc)
            snc.append({"comment": request.POST['comment']})

            Sport.objects.create(
                title = theTitle,
                picture = thePic,
                text = theText,
                sportComments = snc,
                category='Sport'
            )

        if section == 'Bussiness':
            bizObj = Bussiness.objects.get(category='Bussiness')
            #print('id %s'%newsObj.id)
            theTitle = bizObj.title
            thePic = bizObj.picture
            theText = bizObj.text
            bnc = bizObj.bizComments
            Bussiness.objects.all().delete()
            bnc = bnc.replace("'", "\"")
            bnc = json.loads(bnc)
            bnc.append({"comment": request.POST['comment']})
        
            Bussiness.objects.create(
                title = theTitle,
                picture = thePic,
                text = theText,
                bizComments = bnc,
                category='Bussiness'
            )
        
    
        if section == 'Account':
            found = False
            post = request.POST
            pusername = post['username']
            ppassword = post['password']
            pname = post['name']
            pphoneNumber = post['phoneNumber']
            #print('name: %s'%post['name'])
            #print('user: %s'%username)
            accObj = Account.objects.get(category='Account')
            #print('id %s'%newsObj.id)
            accData = accObj.accountArr
            accData = accData.replace("'", "\"")
            accData = json.loads(accData)
            for d in accData:
                print('item: %s'%d['username'])
                if d['username'] == pusername:
                    #print('username found')
                    found = True
                    accVeriData = "false"
                    break
                else:
                    found = False
                    accVeriData = "true"

            if not found:
                #print('add new account')
                newAccount = {
                    "username": pusername,
                    "password": ppassword,
                    "name": pname,
                    "phoneNumber": pphoneNumber,
                    "newsPagelikeOrDislike": "false",
                    "sportPagelikeOrDislike": "false",
                    "bizPagelikeOrDislike": "false"
                }
                accData.append(newAccount)
                Account.objects.all().delete()
                
                Account.objects.create(
                    accountArr = accData,
                    category = "Account"
                )


        
        
        if section == 'Log In':
            lgUsrfound = False
            lgPwdfound = False
            lgPost = request.POST
            lgUser = lgPost['username']
            lgPwd  = lgPost['password']
            lgdIn = lgPost['isLgdIn']
            #print('user log in %s'%lgUser)
            accObj2 = Account.objects.get(category='Account')
            #print('id %s'%newsObj.id)
            dictItem = {}
            accData2 = accObj2.accountArr
            accData2 = accData2.replace("'", "\"")
            accData2 = json.loads(accData2)
            if lgdIn == 'y':
                isLoggedIn = "loggedIn"
                print('is logged in')
            for d in accData2:
                #print('item: %s'%d['username'])
                #print('item2: %s'%d['password'])
                #print('lgusr: %s lgPwd %s', lgUser, lgPwd)
                if d['username'] == lgUser and d['password'] == lgPwd:
                    #print('username password found')
                    lgUsrfound = True
                    lgPwdfound = True
                    logInPwdData = 'true'
                    logInUsrData = 'true'
                    dictItem = d
                    break
                else:
                    lgUsrfound = False
                    lgPwdfound = False
                    logInPwdData = 'false'
                    logInUsrData = 'false'
                   
            if lgUsrfound and lgPwdfound:
                
                CurrentAccount.objects.all().delete()

                CurrentAccount.objects.create(
                    name = dictItem['name'],
                    phoneNumber = dictItem['phoneNumber'],
                    username = dictItem['username'],
                    password = dictItem['password'],
                    newsPagelikeOrDislike = dictItem['newsPagelikeOrDislike'],
                    sportPagelikeOrDislike = dictItem['sportPagelikeOrDislike'],
                    bizPagelikeOrDislike = dictItem['bizPagelikeOrDislike'],
                    category = 'Current Account'
                )
        
        if section == 'Log Out':
            lgPost = request.POST
            lgdIn = lgPost['isLgdIn']
            
            if lgdIn == 'n':
                isLoggedIn = "notLoggedIn"
                print('is logged in')
                
                CurrentAccount.objects.all().delete()

                CurrentAccount.objects.create(
                    name = '',
                    phoneNumber = '',
                    username = '',
                    password = '',
                    newsPagelikeOrDislike = False,
                    sportPagelikeOrDislike = False,
                    bizPagelikeOrDislike = False,
                    category = 'Current Account'
                )
       
        if section == 'New Name':
            print('in new name')
            newname = request.POST['newName']
            nmfound = False
            item = None  
            currAccObj = CurrentAccount.objects.get(category='Current Account')
            nphoneNumber = currAccObj.phoneNumber
            npassword = currAccObj.password
            nusername = currAccObj.username
            nnewsPage = currAccObj.newsPagelikeOrDislike
            nsportPage = currAccObj.sportPagelikeOrDislike
            nbizPage = currAccObj.bizPagelikeOrDislike
            accobj = Account.objects.get(category='Account')
            accdata = accobj.accountArr
            accdata = accdata.replace("'", "\"")
            accdata = json.loads(accdata)

            CurrentAccount.objects.all().delete()

            CurrentAccount.objects.create(
                    name = newname,
                    phoneNumber = nphoneNumber,
                    username = nusername,
                    password = npassword,
                    newsPagelikeOrDislike = nnewsPage,
                    sportPagelikeOrDislike = nsportPage,
                    bizPagelikeOrDislike = nbizPage,
                    category = 'Current Account'
            )

            for a in accdata:
                print('item: %s'%a['username'])
                if a['username'] == nusername:
                    nmfound = True
                    item = a
                    print('nmfound ')
                    break
                else:
                    nmfound = False

            if nmfound:
                print('in nmfound')
                accdata.remove(item)
                    
                nwaccount = {
                    "username": nusername,
                    "password": npassword,
                    "name": newname,
                    "phoneNumber": nphoneNumber,
                    "newsPagelikeOrDislike": nnewsPage,
                    "sportPagelikeOrDislike": nsportPage,
                    "bizPagelikeOrDislike": nbizPage
                }
                accdata.append(nwaccount)
                Account.objects.all().delete()
                
                Account.objects.create(
                    accountArr = accdata,
                    category = "Account"
                )

        if section == 'New Number':
            #print('in new name')
            newnumber = request.POST['newNumber']
            currAccObj2 = CurrentAccount.objects.get(category='Current Account')
            numfound = False
            item2 = None
            nuname = currAccObj2.name
            nupassword = currAccObj2.password
            nuusername = currAccObj2.username
            nunewsPage = currAccObj2.newsPagelikeOrDislike
            nusportPage = currAccObj2.sportPagelikeOrDislike
            nubizPage = currAccObj2.bizPagelikeOrDislike
            accobj2 = Account.objects.get(category='Account')
            accdata2 = accobj2.accountArr
            accdata2 = accdata2.replace("'", "\"")
            accdata2 = json.loads(accdata2)

            CurrentAccount.objects.all().delete()

            CurrentAccount.objects.create(
                    name = nuname,
                    phoneNumber = newnumber,
                    username = nuusername,
                    password = nupassword,
                    newsPagelikeOrDislike = nunewsPage,
                    sportPagelikeOrDislike = nusportPage,
                    bizPagelikeOrDislike = nubizPage,
                    category = 'Current Account'
            )
            for b in accdata2:
                print('item: %s'%b['username'])
                if b['username'] == nuusername:
                    numfound = True
                    item2 = b
                    print('numfound ')
                    break
                else:
                    numfound = False

            if numfound:
                print('in numfound')
                accdata2.remove(item2)
                    
                nwaccount2 = {
                    "username": nuusername,
                    "password": nupassword,
                    "name": nuname,
                    "phoneNumber": newnumber,
                    "newsPagelikeOrDislike": nunewsPage,
                    "sportPagelikeOrDislike": nusportPage,
                    "bizPagelikeOrDislike": nubizPage
                }
                accdata2.append(nwaccount2)
                Account.objects.all().delete()
                
                Account.objects.create(
                    accountArr = accdata2,
                    category = "Account"
                )


        if section == 'News LikeOrDislike':
            print('in newslod')
            nlod = request.POST['Lod']
            currAccObj3 = CurrentAccount.objects.get(category='Current Account')
            nu2name = currAccObj3.name
            nu2phoneNumber = currAccObj3.phoneNumber
            nu2password = currAccObj3.password
            nu2username = currAccObj3.username
            #nu2newsPage = currAccObj3.newsPagelikeOrDislike
            nu2sportPage = currAccObj3.sportPagelikeOrDislike
            nu2bizPage = currAccObj3.bizPagelikeOrDislike
            nlodfound = False
            item3 = None
            accobj3 = Account.objects.get(category='Account')
            accdata3 = accobj3.accountArr
            accdata3 = accdata3.replace("'", "\"")
            accdata3 = json.loads(accdata3)

            CurrentAccount.objects.all().delete()

            CurrentAccount.objects.create(
                    name = nu2name,
                    phoneNumber = nu2phoneNumber,
                    username = nu2username,
                    password = nu2password,
                    newsPagelikeOrDislike = nlod,
                    sportPagelikeOrDislike = nu2sportPage,
                    bizPagelikeOrDislike = nu2bizPage,
                    category = 'Current Account'
            )

            for m in accdata3:
                if m['username'] == nu2username:
                    nlodfound = True
                    item3 = m
                    #print('numfound ')
                    break
                else:
                    nlodfound = False

            if nlodfound:
                #print('in numfound')
                accdata3.remove(item3)
                    
                nwaccount3 = {
                    "username": nu2username,
                    "password": nu2password,
                    "name": nu2name,
                    "phoneNumber": nu2phoneNumber,
                    "newsPagelikeOrDislike": nlod,
                    "sportPagelikeOrDislike": nu2sportPage,
                    "bizPagelikeOrDislike": nu2bizPage
                }
                
                accdata3.append(nwaccount3)
                Account.objects.all().delete()
                Account.objects.create(
                    accountArr = accdata3,
                    category = "Account"
                )

        if section == 'Sport LikeOrDislike':
            print('in sportlod: %s'%request.POST['Lod'])
            #print('in newslod')
            slod = request.POST['Lod']
            currAccObj4 = CurrentAccount.objects.get(category='Current Account')
            nu3name = currAccObj4.name
            nu3phoneNumber = currAccObj4.phoneNumber
            nu3password = currAccObj4.password
            nu3username = currAccObj4.username
            nu3newsPage = currAccObj4.newsPagelikeOrDislike
            #nu2sportPage = currAccObj4.sportPagelikeOrDislike
            nu3bizPage = currAccObj4.bizPagelikeOrDislike
            slodfound = False
            item4 = None
            accobj4 = Account.objects.get(category='Account')
            accdata4 = accobj4.accountArr
            accdata4 = accdata4.replace("'", "\"")
            accdata4 = json.loads(accdata4)


            CurrentAccount.objects.all().delete()

            CurrentAccount.objects.create(
                    name = nu3name,
                    phoneNumber = nu3phoneNumber,
                    username = nu3username,
                    password = nu3password,
                    newsPagelikeOrDislike = nu3newsPage,
                    sportPagelikeOrDislike = slod,
                    bizPagelikeOrDislike = nu3bizPage,
                    category = 'Current Account'
            )

            for s in accdata4:
                if s['username'] == nu3username:
                    slodfound = True
                    item4 = s
                    #print('numfound ')
                    break
                else:
                    slodfound = False

            if slodfound:
                #print('in numfound')
                accdata4.remove(item4)
                    
                nwaccount4 = {
                    "username": nu3username,
                    "password": nu3password,
                    "name": nu3name,
                    "phoneNumber": nu3phoneNumber,
                    "newsPagelikeOrDislike": nu3newsPage,
                    "sportPagelikeOrDislike": slod,
                    "bizPagelikeOrDislike": nu3bizPage
                }
                
                accdata4.append(nwaccount4)
                Account.objects.all().delete()
                Account.objects.create(
                    accountArr = accdata4,
                    category = "Account"
                )

        if section == 'Biz LikeOrDislike':
            #print('in bizlod:- %s'%request.POST['Lod'])
            #print('in sportlod')
            #print('in newslod')
            blod = request.POST['Lod']
        
            currAccObj5 = CurrentAccount.objects.get(category='Current Account')
            nu4name = currAccObj5.name
            nu4phoneNumber = currAccObj5.phoneNumber
            nu4password = currAccObj5.password
            nu4username = currAccObj5.username
            nu4newsPage = currAccObj5.newsPagelikeOrDislike
            nu4sportPage = currAccObj5.sportPagelikeOrDislike
            #nu4bizPage = currAccObj4.bizPagelikeOrDislike
            blodfound = False
            item5 = None
            accobj5 = Account.objects.get(category='Account')
            accdata5 = accobj5.accountArr
            accdata5 = accdata5.replace("'", "\"")
            accdata5 = json.loads(accdata5)


            CurrentAccount.objects.all().delete()

            CurrentAccount.objects.create(
                    name = nu4name,
                    phoneNumber = nu4phoneNumber,
                    username = nu4username,
                    password = nu4password,
                    newsPagelikeOrDislike = nu4newsPage,
                    sportPagelikeOrDislike = nu4sportPage,
                    bizPagelikeOrDislike = blod,
                    category = 'Current Account'
            )
        
            for i in accdata5:
                if i['username'] == nu4username:
                    blodfound = True
                    item5 = i
                    #print('numfound ')
                    break
                else:
                    blodfound = False

            if blodfound:
                #print('in numfound')
                accdata5.remove(item5)
                    
                nwaccount5 = {
                    "username": nu4username,
                    "password": nu4password,
                    "name": nu4name,
                    "phoneNumber": nu4phoneNumber,
                    "newsPagelikeOrDislike": nu4newsPage,
                    "sportPagelikeOrDislike": nu4sportPage,
                    "bizPagelikeOrDislike": blod
                }
                
                accdata5.append(nwaccount5)
                Account.objects.all().delete()
                Account.objects.create(
                    accountArr = accdata5,
                    category = "Account"
                ) 
    
        
        obj =  []
    
        if News.objects.all():
            obj.append(News.objects.all())
        if Sport.objects.all():
            obj.append(Sport.objects.all())
        if Bussiness.objects.all():
            obj.append(Bussiness.objects.all())
        if Account.objects.all():
            obj.append(Account.objects.all())
        if CurrentAccount.objects.all():
            obj.append(CurrentAccount.objects.all())
    
        
        if len(obj)>=1:
            val = obj[0]
            raw_data = serializers.serialize('python', val)
            actual_data = raw_data[0]['fields']
            output = json.dumps(actual_data)
            newdata = json.loads(output)
            obj2.update(news=newdata)

        if len(obj)>=2:
            val2 = obj[1]
            raw_data2 = serializers.serialize('python', val2)
            actual_data2 = raw_data2[0]['fields']
            output2 = json.dumps(actual_data2)
            newdata2 = json.loads(output2)
            obj2.update(sport=newdata2)
        
        if len(obj)>=3:
            val3 = obj[2]
            raw_data3 = serializers.serialize('python', val3)
            actual_data3 = raw_data3[0]['fields']
            output3 = json.dumps(actual_data3)
            newdata3 = json.loads(output3)
            obj2.update(bussiness=newdata3)

        if len(obj)>=4:    
            val4 = obj[3]
            raw_data4 = serializers.serialize('python', val4)
            actual_data4 = raw_data4[0]['fields']
            output4 = json.dumps(actual_data4)
            newdata4 = json.loads(output4)
            obj2.update(account=newdata4)

        if len(obj)>=5:    
            val5 = obj[4]
            raw_data5 = serializers.serialize('python', val5)
            actual_data5 = raw_data5[0]['fields']
            output5 = json.dumps(actual_data5)
            newdata5 = json.loads(output5)
            obj2.update(currentAccount=newdata5)

            obj2.update(isNewAccount=accVeriData)
            obj2.update(usernameExists=logInUsrData)
            obj2.update(passwordExists=logInPwdData)
            obj2.update(isLoggedIn=isLoggedIn)
        #'''        

        #print('p obj2 %s'%obj2)
        #print('p newdata %s'%newdata)
        #print('p newdata2 %s'%newdata2)
        #print('p newdata3 %s'%newdata3)
        #print('p newdata4 %s'%newdata4)
 
    
        
        return HttpResponseRedirect('/testApp/download/')
    else:
        return HttpResponse('no create', request)


