$(function(){    
    $logInUsr = $('#logInUsr');
    $logInPwd = $('#logInPwd');
    var accInfo = document.getElementById("accInfo");


    $('#login-button').on('click', function(e){
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/testApp/create/',
            dataType: 'json',
            data: {
                username: $logInUsr.val(),
                password: $logInPwd.val(),
                isLgdIn: 'y',
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                section: 'Log In'
            },
            success: function(item){
                console.log('data: '+$logInPwd.val()+' '+$logInUsr.val());
                console.log('it worked hooray');
                console.log('user exists: '+item.usernameExists+' '+item.passwordExists);
                usrExists = item.usernameExists;
                pwdExists = item.passwordExists;
                if(usrExists=='true'&&pwdExists=='true'){
                    $("#accInfo").attr( "href", "http://localhost:8000/testApp/accountInfo");
                    accInfo.classList.remove("disabled");
                    alert('You are now loged in');
                }else if(usrExists=='false'&&pwdExists=='false'){
                    alert('Log in information not recognized');
                }
            },
            error: function(){
                console.log('error');
            }
        });    
    });
    
     $('#logout-button').on('click', function(e){
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/testApp/create/',
            dataType: 'json',
            data: {
                isLgdIn: 'n',
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                section: 'Log Out'
            },
            success: function(item){
                console.log("hello logout: "+item.isLoggedIn);        
                var islogin = item.isLoggedIn;
                if(islogin=="loggedIn"){
                    console.log("log out failure");
                }else if(islogin=="notLoggedIn"){
                    console.log("log out success");
                    $("#accInfo").attr( "href", "");
                    accInfo.classList.add("disabled");
                }   
            },
            error: function(){
                console.log('error');
            }
        });    
    });

    $.ajax({
        type: "GET",
        url: '/testApp/download/',
        dataType: 'json',
        success: function(item){
            console.log("get success");
            var islogin = item.isLoggedIn;
            if(islogin=="loggedIn"){
                 $("#accInfo").attr( "href", "http://localhost:8000/testApp/accountInfo");
                 accInfo.classList.remove("disabled");
            }else if(islogin=="notLoggedIn"){
                $("#accInfo").attr( "href", "");
                accInfo.classList.add("disabled");
            }       
        },
        error: function(){
            console.log('get error');
        }
    });
});   