let csrf_token=$("input[name=csrfmiddlewaretoken]").val();
// let flags = {'email_flag':false,'username_flag':false,'password_flag':false}
username_valid = false;
// Register Form Save Validation using jquery validation library
$.validator.addMethod(
    "validate_username",
    function (value, element) {
      const regex = /^[A-Za-z0-9_]+$/;
      username_valid = regex.test(value) ? true : false;
      return this.optional(element) || regex.test(value)
  },
  "Invalid user name"
)
$.validator.addMethod(
    "is_username_exists",
    function (value,element){
        if(username_valid){
            $.ajax({
                headers : {
                    'X-CSRFToken' : csrf_token
                },
                type:'POST',
                url:'ajax/check-username/',
                data : {
                    username:value
                },
                dataType : 'JSON',
                success : function(response){
                    if(response.is_exists){
                        return true;
                    }else{
                        return false;
                    }
                }
            })
        }else{
            return true;
        }
    },
    "user name already exists"
)
$.validator.addMethod(
    "validate_email",
    function (value, element) {
      // According to RBI guideline account number consists 9 to 18 digits
      const regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
      return this.optional(element) || regex.test(value)
  },
  "Invalid Email"
);

let register_form = $("#register-form").validate({
    rules: {
      username: {
        required: {
          depends: function () {
            if ($("#username").val().trim()){
                return false;
            }else{
                return true
            }
          },
        },
        validate_username:"Invalid user name",
        is_username_exists:"user name already exists"
      },
      email: {
        required: {
          depends: function () {
            if ($("#email").val().trim()){
                return false;
            }else{
                return true
            }
          },
        },
        validate_email:"Invalid Email",
      },
      password: {
        required: {
          depends: function () {
            if ($("#password").val().trim()){
                return false;
            }else{
                return true
            }
          },
        },
      },
      confirm_password: {
        required: {
          depends: function () {
            if ($("#confirm-password").val().trim()){
                return false;
            }else{
                return true
            }
          },
        },
        equalTo: "#password",
      },
    },
    messages: {
        username:{
            required:"Please enter username"
        },
        email:{
            required:"Please enter email"
        },
        confirm_password:{
            equalTo:"Password did not match"
        }
    },
    errorClass: "errorClass", //apply a css class for error if you have style for valid
    validClass: "validClass", //apply a css class for error if you have style for error
  
    submitHandler: function (form) {
      if ($("#register-form").valid()) {
        form.submit();
      }
    },
  });
/******************
// FORM HANDLE 
$("#register-btn").on('click',(e)=>{
    e.preventDefault()
    if(flags.email_flag && flags.username_flag && flags.password_flag){
        $("#register-form").submit();
    }
})
// USERNAME VALIDATION
$("#username").on('keyup',(e)=>{
    e.target.value = e.target.value.trim();
    let username = e.target.value.trim();
    let username_regex = /^[A-Za-z0-9_]+$/;

    if(!username){
        $(".username-error").show();
        $(e.target).css({'border-color':'#FF0000'});
        $(".username-error").html("This field is required");
    }else{
        if(username_regex.test(username)){
            $.ajax({
                headers : {
                    'X-CSRFToken' : csrf_token
                },
                type:'POST',
                url:'ajax/check-username/',
                data : {
                    username:username
                },
                dataType : 'JSON',
                success : function(response){
                    if(response.is_exists){
                        flags.username_flag = false;
                        $(".username-error").show();
                        $(e.target).css({'border-color':'#ff0000'});
                        $(".username-error").html("username is not available please try another");
                    }else{
                        flags.username_flag = true;
                        $(".username-error").html("");
                        $(e.target).css({'border-color':'#4CBB17'});
                        $(".username-error").hide();
                    }
                }
            })
        }else{
            $(".username-error").show();
            $(e.target).css({'border-color':'#ff0000'})
            $(".username-error").html("no special character allowed");
        }
    }
})
// EMAIL VALIDATION 
$("#email").on('keyup',(e)=>{
    e.target.value=e.target.value.trim();
    let email = e.target.value.trim();
    let email_regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if(!email){
        $('.email-error').show();
        $(e.target).css({'border-color':'#FF0000'})
        $('.email-error').html('This field is required');
    }else{
        if(email_regex.test(email)){
            $.ajax({
                headers : {
                    'X-CSRFToken' : csrf_token
                },
                type:'POST',
                url:'ajax/check-email/',
                data : {
                    email:email
                },
                dataType : 'JSON',
                success : function(response){
                    if(response.is_exists){
                        flags.email_flag = false;
                        $('.email-error').show();
                        $(e.target).css({'border-color':'#FF0000'})
                        $('.email-error').html('Email already in use');
                    }else{
                        flags.email_flag = true;
                        $('.email-error').html('');
                        $(e.target).css({'border-color':'#4CBB17'})
                        $('.email-error').hide();
                    }
                }
            })
        }else{
            $('.email-error').show();
            $(e.target).css({'border-color':'#FF0000'})
            $('.email-error').html('Invalid Email');
        }
    }
})

$('#password').on('keyup',(e)=>{
    let password = e.target.value.trim();
    let confirm_password = $("#confirm-password").val().trim();
    if(!confirm_password){
        flags.password_flag = false;
        $('.confirm-password-error').html('Please confirm your password');
        $('#confirm-password').css({'border-color':'#FF0000'})
    }else{
        if(password!=confirm_password){
            flags.password_flag = false;
            $('.password-error').html('password did not match');
            $(e.target).css({'border-color':'#FF0000'})
        }else{
            hide_password_error();
        }
    }
})
$('#confirm-password').on('keyup',(e)=>{
    let password = $("#password").val().trim();
    let confirm_password = e.target.value.trim();
    if(!password){
        $('.password-error').html('Please enter your password');
        $('#password').css({'border-color':'#FF0000'})
        flags.password_flag = false;
    }else{
        if(password!=confirm_password){
            flags.password_flag = false;
            $('.confirm-password-error').html('password did not match');
            $(e.target).css({'border-color':'#FF0000'})
        }else{
            hide_password_error();
        }
    }
})
function hide_password_error(){
    flags.password_flag = true;
    $('.password-error').html('');
    $('#password').css({'border-color':'#4CBB17'})
    $('.confirm-password-error').html('');
    $('#confirm-password').css({'border-color':'#4CBB17'})
}


***********************/