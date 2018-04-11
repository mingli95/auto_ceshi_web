$(function () {
    $('body').on('click','#add-api-link',function () {
        $('#add-api-modal').show();
    })
    $('#api-close-modal-btn').on('click', function () {
        $('#add-api-modal').hide();
    })
    $('#api-cancel-btn').on('click', function () {
        $('#add-api-modal').hide();
    })
    $('body').on('click','.delete-link',function () {
        var data = {
            'data':JSON.stringify({id: $(this).data('id')
            })};
        $.ajax({
                data:data,
                url:'/api/delete',
                type:'POST',
                dataType:'json',
                success:function (data) {
                    if(data.status == 200){
                        window.location.reload('/apiList');
                    }
                    else {
                        alert('删除失败!')
                    }
                }
            }
        )
    })
    $('#submit-btn').on('click',function () {
        var data = {'data': JSON.stringify({
            name: $('#api-name').val(),
            url: $('#api-url').val(),
            method: $('#api-method').val(),
            desc: $('#api-desc').val()
        })};
        $.ajax({
            data:data,
            url:'/api/add',
            type:'POST',
            dataType:'json',
            success: function (data) {
                if (data.status == 200) {
                    $('.modal-wrapper').hide();
                    window.location.reload('/apiList');
                }
                else {
                    alert(data.message);
                }
            }
        })

    })

})