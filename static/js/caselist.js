$(function () {
    $('body').on('click','.add-link',function () {
        $('#case-modal').show();
    })
    $('#close-modal-btn').on('click', function () {
        $('#case-modal').hide();
    })
    $('#cancel-btn').on('click', function () {
        $('#case-modal').hide();
    })

    $('#edit-close-modal-btn').on('click', function () {
        $('#edit-modal').hide();
    })
    $('#edit-cancel-btn').on('click', function () {
        $('#edit-modal').hide();
    })
    $('#edit-api-close-modal-btn').on('click', function () {
        $('#edit-api-modal').hide();
    })
    $('#edit-api-cancel-btn').on('click', function () {
        $('#edit-api-modal').hide();
    })
    $('body').on('click','#edit-api',function () {
        var id = $(this).data('id');
        var case_id = $(this).data('caseid');
        html = '<div id="edit-api-box-id" data-caseid='+ case_id +' data-apiid='+ id +'></div>'
        $('#edit-api-box').html(html);
        $('#edit-api-modal').show();
    })
    $('#edit-api-submit-btn').on('click',function () {
        var data = {'data': JSON.stringify({
            apiid: $('#edit-api-box-id').data('apiid'),
            caseid: $('#edit-api-box-id').data('caseid'),
            params: $('#case-data').val(),
            apiast: $('#api-ast').val(),
            apiastval: $('#api-ast-val').val(),
            apiout: $('#api-ast-out').val(),
            apioutval: $('#api-ast-val-out').val(),
        })};
        $.ajax({
            data:data,
            url:'/parame/add',
            type:'POST',
            dataType:'json',
            success: function (data) {
                if (data.status == 200) {
                    $('#edit-api-modal').hide();
                    // window.location.reload('/caseList');
                }
                else {
                    alert(data.message);
                }
            }
        })
    })
    $('body').on('click','.edit-link',function () {
        var data = {
            'data':JSON.stringify({
                id:$(this).data('id')
            })};
        $.ajax({
            data:data,
            url:'/apiGetName',
            type:'POST',
            dataType:'json',
            success: function (data) {
                if (data.status == 200) {
                    var html = '';
                    for(var i = 0; i < data.data.length; i++) {
                        html = html + '<div>'+
                            '<span style="display: inline-block;width: 80%;text-indent: 50px;">' + data.data[i].name + '</span><a href="#" data-id=' + data.data[i].id +  ' data-caseid=' + data.data[i].case_id +  ' id="edit-api">编辑</a>'+
                            '</div>';
                    }
                    /*$.each(data.data,function (index,item) {
                        console.log('item ',item);
                        html = html + '<div>'+
                            '<span style="display: inline-block;width: 80%;text-indent: 50px;">' + item.name + '</span><a href="#">编辑</a>'+
                            '</div>';
                    })*/
                    $('#edit-url-box').html(html);
                    $('#edit-modal').show();

                }
                else {
                    alert(data.message);
                }
            }
        })


    })
    $('#submit-btn').on('click',function () {
        var data = {'data': JSON.stringify({
            name: $('#case-name').val(),
            project: $('#select-id').val(),
            desc: $('#case-desc').val(),
            apiId1: $('#select-id1').val(),
            apiId2: $('#select-id2').val(),
            apiId3: $('#select-id3').val(),
        })};
        $.ajax({
            data:data,
            url:'/case/add',
            type:'POST',
            dataType:'json',
            success: function (data) {
                if (data.status == 200) {
                    $('.modal-wrapper').hide();
                    window.location.reload('/caseList');
                }
                else {
                    alert(data.message);
                }
            }
        })
    })
    $('.run-link').on('click',function () {
        var data = {'data':JSON.stringify({
                id:$(this).data('id')
            }
        )};
        $.ajax({
            data:data,
            url:'/case/run',
            type:'POST',
            dataType:'json',
            success: function (data) {
                if(data.status == 200 ){
                    alert(data.message)
                }
                else {
                    alert(data.message)
                }

            }
        })


    })
})
