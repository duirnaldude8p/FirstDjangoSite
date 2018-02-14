class Comments(models.Model):
    comment = models.CharField(max_length=200, default="no comment", null=True)

class News(models.Model):
    title = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE)

class Sport(models.Model):  
    title = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE)

class Bussiness(models.Model):
    title = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE)

class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    newsPageLikeOrDislike = models.BooleanField(default=False)
    sportPageLikeOrDislike = models.BooleanField(default=False)
    bizPageLikeOrDislike = models.BooleanField(default=False)

'default': {
        
    }

'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.path.join(BASE_DIR, '11762'),
        'USER': 'sam',
        'PASSWORD': 'sam',
        'HOST': '127.0.0.1',
        'PORT': '5432',

'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',


        # Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    newsComments = models.CharField(max_length=5000)
    

class Sport(models.Model):  
    title = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    sportComments = models.CharField(max_length=5000)
    

class Bussiness(models.Model):
    title = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    bizComments = models.CharField(max_length=5000)
   

class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    newsPageLikeOrDislike = models.BooleanField(default=False)
    sportPageLikeOrDislike = models.BooleanField(default=False)
    bizPageLikeOrDislike = models.BooleanField(default=False)

    obj2 = {}
    newdata4 = {}
    someObj = {}

    testJson = {"key1": "vallue1","key2": "value2", "nestedTest": [{"nested1":"nestedVal1"}, {"nested2": "nestedVal2"}] }

        nestedTest =  [{"nested1":"nestedVal1"}, {"nested2": "nestedVal2"}] 
        #News.objects.all().delete()
   
          
        #Test.objects.create(
        #    key1 = testJson['key1'],
        #    key2 = testJson['key2'],
        #    nestedTest = nestedTest
        #)
        
        
        
    
        global newdata4
        global someObj
        newdata4 = {}
        someObj = {}

        print('nd %s'%newdata4)
        print('obj %s'%someObj)
        '''
        if not someObj and not newdata4:
                   
            #testObj =  Test.objects.all()


            raw_data4 = serializers.serialize('python', testObj)
            actual_data4 = raw_data4[0]['fields']
            output4 = json.dumps(actual_data4)
            newdata4 = json.loads(output4)
            someObj.update(test=newdata4)
            print('in get')
            #print('nd %s'%newdata4)
            #print('obj %s'%someObj)
            '''

            
        '''
        testJson = {"key1": "value1","key2": "value2"}
        ''' 
        '''     
        Test.objects.create(
            key1 = testJson['key1'],
            key2 = testJson['key2']
        )
        ''' 


        #print('p obj %s'%someObj)
        #theComm = nc
        #News.objects.all().delete()
        '''
        News.objects.create(
            title = theTitle,
            picture = thePic,
            text = theText,
            newsComments = nc
        )

        '''
        #print('new nc %s'%newsObj.newsComments)
        '''
        global obj2

        if News.objects.all():
            pval = News.objects.all()
            praw_data = serializers.serialize('python', pval)
            pactual_data = praw_data[0]['fields']
            poutput = json.dumps(pactual_data)
            pnewdata = json.loads(poutput)
            obj2.update(news=pnewdata)
        '''
        
           function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        <!--<p class="text1">The English city was the only interested party before the original 30 September deadline but its bid was deemed "not fully compliant".
            The Commonwealth Games Federation (CGF) now say it has received "updates" from Australia, Canada and Malaysia - but did not confirm any official bids.
          The body will offer a further update after a board meeting on 6 December.</p>
          <p class="text1">In a statement on Friday, it said: "Updates have been received from Australia, Canada, England and Malaysia.
            "The CGF wishes to thank all four countries for the interest that they have shown in hosting the Commonwealth Games."
            Kuala Lumpur and Victoria are thought to be the cities involved from Malaysia and Canada respectively.</p>
          <p class="text1">
            The bidding process has been beset with problems, with the South African city of Durban originally awarded the Games in 2015 before being stripped of the event in March because it did not meet the CGF criteria.
            After Birmingham's subsequent bid did not meet criteria, the CGF extended the deadline for bids to 30 November.
            Cllr Ian Ward, Birmingham city council leader and chair of Birmingham 2022's bid team, said: "We have had a number of productive meetings with the Commonwealth Games Federation as we demonstrate that Birmingham, being at the heart of the UK and the soul of the Commonwealth, would make the ideal host for the 2022 Games.</p>
          <p class="text1">
            "We look forward to a decision from the CGF in the near future."
          </p>-->

            #print('in post %s' %field.name)

             for d in accdata:
                print('item: %s'%d['username'])
                if d['username'] == nusername:
                    nmfound = True
                    item = d
                    break
                else:
                    nmfound = False

            if nmfound:
                item = accdata[itemIt]
                accdata.remove(item)
                newaccount = {
                    "username": nusername,
                    "password": npassword,
                    "name": newname,
                    "phoneNumber": pphoneNumber,
                    "newsPagelikeOrDislike": nnewsPage,
                    "sportPagelikeOrDislike": nsportPage,
                    "bizPagelikeOrDislike": nbizPage
                }
                accdata.append(newaccount)
                Account.objects.all().delete()
                
                Account.objects.create(
                    accountArr = accdata,
                    category = "Account"
                )