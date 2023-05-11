$("#cover_image").on('change',(e)=>{
    if(e.target.files.length > 0){
        let src = URL.createObjectURL(e.target.files[0]);
        $(".profile-img").attr('src',src);
        $(".cover-image-box").html(`<img src="${src}" />`)
        $('.cover-image-error').html('');
    }
})
$("#category").on('keyup',(e)=>{
    if(e.target.value.trim()!=''){
        $('.category-error').html('');
    }
})
$("#title").on('keyup',(e)=>{
    if(e.target.value.trim()!=''){
        $('.title-error').html('');
    }
})
$("#about").on('keyup',(e)=>{
    if(e.target.value.trim()!=''){
        $('.about-error').html('');
    }
})
$("#category").on('change',(e)=>{
    if(e.target.value!=-1){
        $('.category-error').html('');
    }
})

quill.root.addEventListener('keyup', function(event) {
    if(quill.getText().trim()){
        $('.description-error').html('');
    }
});

$('#category-save-btn').on('click',(e)=>{
    e.preventDefault();
    let category = $("#category").val().trim();
    let title = $("#title").val().trim();
    let about = $("#about").val().trim();
    let cover_image = $("#cover_image").val().trim();
    let description = quill.getText().trim().length;
    if(!title){
        $('.title-error').html('Please enter title');
    }
    if(category==-1){
        $('.category-error').html('Please select category');
    }
    if(!about){
        $('.about-error').html('Please enter about your blog');
    }
    if(!cover_image){
        $('.cover-image-error').html('Please select cover image');
    }
    if(!description){
        $('.description-error').html('Please enter description')
    }
    if(title && about && cover_image && description && category){
        $("#description").html($("#editor").html());
        $("#category-form").submit();    
    }
})