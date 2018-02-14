$(function(){
    $usrnm = $('#usrnm');
    $name = $('#name');
    $num = $('#num');
    $newname = $('#newname');
    $newnumber = $('#newnumber');
    $namebtn = $('#name-button');
    $numberbtn = $('#number-button');


    
    $.ajax({
        type: 'GET',
        dataType: 'json',
        url: '/testApp/download/',
        success: function(value){
            console.log("get success");
            $usrnm.text(value.currentAccount.username);
            $name.text(value.currentAccount.name);
            $num.text(value.currentAccount.phoneNumber);    
        },
        error: function(){
            console.log('get error');
        }
    });
    

    $namebtn.on('click', function(e){
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/testApp/create/',
            dataType: 'json',
            data: {
                newName: $newname.val(), 
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                section: 'New Name'
            },
            success: function(item){
                $name.text(item.currentAccount.name);
                console.log("post success");
            },
            error: function(){
                console.log('post error');
            }
        });
    }); 

    $numberbtn.on('click', function(e){
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/testApp/create/',
            dataType: 'json',
            data: {
                newNumber: $newnumber.val(), 
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                section: 'New Number'
            },
            success: function(item){
                $num.text(item.currentAccount.phoneNumber);
                console.log("post success");
            },
            error: function(){
                console.log('post error');
            }
        });
    });    
});
