

$(function(){
    $title = $("#title");
    $image = $("#image");
    $comment = $("#comment");
    $comments = $("#comments");
    $commentInput = $("#comment-input");
    $like = $("#like");
    var likeIconLike = document.getElementById("like-icon-like");
    var likeIconDislike = document.getElementById("like-icon-dislike");
    $text = $("#text");
    var islike = false;
    var currlod = '';
    var accInfo = document.getElementById("accInfo");
    $.ajax({
        type: 'GET',
        dataType: 'json',
        url: '/testApp/download/',
        success: function(value){
            console.log("get sucess");
            $title.text(value.sport.title);
            $image.attr("src", value.sport.picture);
            $text.text(value.sport.text);
            var ncomments = value.sport.sportComments;
            ncomments = ncomments.replace(/'/g, '"');
            var ncomments2 = JSON.parse(ncomments);
            $.each(ncomments2, function(i, item){
                $comments.append('<li id="comments-block">'+"  "+item.comment+'</li>');
            });
            currlod = value.currentAccount.sportPagelikeOrDislike;
            if(currlod=="False"||currlod=="false"){
                likeIconLike.style.background = "#ffffff";
                likeIconDislike.style.background = "#6495ED";
            }else if(currlod=="True"||currlod=="true"){
                likeIconLike.style.background = "#6495ED";
                likeIconDislike.style.background = "#ffffff";
            }
            var islogin = value.isLoggedIn;
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
    $("#add-button").on('click', function(e){
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/testApp/create/',
            dataType: 'json',
            data: {
                comment: $commentInput.val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                section: 'Sport'
            },
            success: function(item){
                $comments.append('<li id="comments-block">'+"  "+$commentInput.val()+'</li>');
                console.log('comment post success: '+$commentInput.val());
            },
            error: function(){
                console.log('comment post error');
            }         
        });  
    });
    $('#like-icon').on('click', function(e){
        e.preventDefault();
        if(currlod=='true'){
            currlod = 'false';
        }else if(currlod=='false'){
            currlod = 'true';
        }
        $.ajax({
            type: 'POST',
            url: '/testApp/create/',
            dataType: 'json',
            data: {
                Lod: currlod,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                section: 'Sport LikeOrDislike'
            },
            success: function(item){               
                console.log("like post success");
                if(currlod=="False"||currlod=="false"){
                    likeIconLike.style.background = "#ffffff";
                    likeIconDislike.style.background = "#6495ED";
                }else if(currlod=="True"||currlod=="true"){
                    likeIconLike.style.background = "#6495ED";
                    likeIconDislike.style.background = "#ffffff";
                }
            },
            error: function(){
                console.log('like post error');
            }
        });
    
    });        
})