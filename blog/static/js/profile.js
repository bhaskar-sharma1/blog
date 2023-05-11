
$("#mobile").on('keyup paste',(e)=>{
    console.log(e)
})
$('.profile-button').on('click',(e)=>{
    e.preventDefault();
    let first_name = $('#first_name').val().trim();
    let last_name = $('#last_name').val().trim();
    let mobile = $('#mobile').val().trim();
    let email = $('#email').val().trim();
    if(email && mobile){
        console.log('form submit');
        $("#profile-form").submit();
    }
});
$('#instagram').on('keyup',(e)=>{
    e.target.value = e.target.value.trim();
})
$('#facebook').on('keyup',(e)=>{
    e.target.value = e.target.value.trim();
})
$("#change-photo").click((e)=>{
    $("#profile-photo").click();
})
$("#profile-photo").on('change',(e)=>{
    if(e.target.files.length > 0){
        let src = URL.createObjectURL(e.target.files[0]);
        $(".profile-img").attr('src',src);
    }
})