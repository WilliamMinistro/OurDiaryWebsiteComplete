$(document).ready(function()
{
    let randNum;
    let djangoNum = 0;
    $('#button-addon2').click(function()
    {
        $('#subtext').text('Submitting....');
    })

    $('#Rand').click(function(){
        let num = $('#countNum').text().match(/\d+/)[0];
        randNum = Math.floor(Math.random() * (num)+1);
        $('.formData').val(randNum)
        }
    )


})