let flags = {'username':false,'password':false}
$("#username").on('keyup',(e)=>{
    e.target.value=e.target.value.trim();
    let username = e.target.value.trim();
    let username_regex = /^[A-Za-z0-9_]+$/;
    if(username){
        if(username_regex.test(username)){
            flags.username = true;
            $('.username-error').html('');
            $('.username-error').hide();
            $(e.target).css({'border-color':'#4CBB17'})
        }else{
            flags.username = false;
            $('.username-error').html('Only Alphanumeric allowed');
            $('.username-error').show();
            $(e.target).css({'border-color':'#FF0000'})
        }
    }else{
        flags.username = false;
        $(e.target).css({'border-color':'#FF0000'})
        $('.username-error').html('Please enter your username')
    }
})
$("#password").on('keyup',(e)=>{
    if(e.target.value){
        flags.password = true;
        $(e.target).css({'border-color':'#4CBB17'});
        $('.password-error').html('');
    }else{
        flags.password = false;
        $(e.target).css({'border-color':'#FF0000'})
        $('.password-error').html('Please enter your password');
    }
})
// ON CLICK LOGIN BUTTON FOLLOWING EVENT WILL BE TRIGGER
document.getElementById("login-btn").addEventListener('click',(e)=>{
    e.preventDefault();
    if(flags.username && flags.password){
        document.getElementById('login-form').submit()
    }else{
        $("#password").trigger('keyup');
        $("#username").trigger('keyup');   
    }
})