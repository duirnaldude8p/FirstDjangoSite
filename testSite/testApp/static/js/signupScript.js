$(function(){    
    $name = $("#name");
    $usr = $("#usr");
    $num = $("#num");
    $pwd = $("#pwd");
    $addBtn = $("#add-button");
    var accInfo = document.getElementById("accInfo");
    $addBtn.on('click', function(e){
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/testApp/create/',
            dataType: 'json',
            data: {
                username: $usr.val(),
                password: $pwd.val(),
                name: $name.val(),
                phoneNumber: $num.val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                section: 'Account'
            },
            success: function(item){
                console.log("post success")
                newAcc = item.isNewAccount;
                console.log("hello acc"+newAcc);
                if(newAcc=='true'||newAcc=='True'){
                    alert('Your Account has been added');
                }else if(newAcc=='false'||newAcc=='False'){
                    alert('Account Already exists');
                }
            },
            error: function(){
                console.log('post error');
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