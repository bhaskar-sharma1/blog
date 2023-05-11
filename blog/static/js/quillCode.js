var toolbarOptions = [
    [{ 'size': ['small', false, 'large', 'huge'] }],  // custom dropdown
    [{ 'header': [1, 2, 3, 4, 5, 6,] }],
    [{ 'font': [] }],

    [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme

    ['image'],

    ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
    // ['blockquote', 'code-block'],

    // [{ 'header': 1 }, { 'header': 2 }],               // custom button values
    [{ 'list': 'ordered'}, { 'list': 'bullet' }],
    [{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript
    // [{ 'indent': '-1'}, { 'indent': '+1' }],          // outdent/indent
    // [{ 'direction': 'rtl' }],                         // text direction


    [{ 'align': [] }],

    ['clean']                                         // remove formatting button
];
var options = {
    // debug: 'info',
    modules: {
        toolbar: toolbarOptions,
    },
    placeholder: 'Start Writing Your Blog...',
    // readOnly: true,
    'image-tooltip': false,
    theme: 'snow'
};
var quill = new Quill('#editor',options);
