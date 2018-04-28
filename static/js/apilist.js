$(function () {
    // 全局查
    $(document).ready(function () {
        var data = JSON.stringify({
            project_id:$('#api-menu-project-id').data('id')
        });
        $.ajax({
            contentType: "application/json",
            data:data,
            url:'/apiList',
            type:'POST',
            dataType:'json',
            success:function (data) {
                if (data.status == 200){
                    var html = '';
                    for(var i = 0; i < data.data.length; i++) {
                        console.log(data.data[i].title)
                        html = html + "<tr data-id = "+data.data[i].id+">" +
                            "<td><input type='checkbox'></td>" +
                            "<td>"+data.data[i].title+"</td>" +
                            "<td>"+data.data[i].project_id+"</td>" +
                            "<td>"+data.data[i].url+"</td>" +
                            "<td>"+data.data[i].status+"</td>" +
                            "<td>"+data.data[i].last_update+"</td>" +
                            "<td><a> 编辑</a><a> 复制</a><a> 删除</a><a> 禁用</a></td>" +
                            "</tr>"
                        document.getElementById("table-tbody").innerHTML=html;
                    }
                }
            }
        })
    });
    // 局部查
    $('body').on('click','#api-apilist',function () {
        var url=$('#api-menu-project-id').data('url');
        var data = JSON.stringify({
            project_id:$('#api-menu-project-id').data('id'),
            title:document.getElementById("name").value,
            status:document.getElementById("status").value
        });
        $.ajax({
            contentType: "application/json",
            data:data,
            url:'/searchApiList',
            type:'POST',
            dataType:'json',
            success:function (data) {
                if (data.status == 200){
                    var html = '';
                    for(var i = 0; i < data.data.length; i++) {
                        console.log(data.data[i].title)
                        html = html + "<tr data-id = "+data.data[i].id+">" +
                            "<td><input type='checkbox'></td>" +
                            "<td>"+data.data[i].title+"</td>" +
                            "<td>"+data.data[i].project_id+"</td>" +
                            "<td>"+data.data[i].url+"</td>" +
                            "<td>"+data.data[i].status+"</td>" +
                            "<td>"+data.data[i].last_update+"</td>" +
                            "<td><a> 编辑</a><a> 复制</a><a> 删除</a><a> 禁用</a></td>" +
                            "</tr>"
                        document.getElementById("table-tbody").innerHTML=html;
                    }
                }
                else {
                    location.reload(url);
                };
            }
        })
    });
    // 取消弹窗
    $('#api-close-modal-btn').on('click', function () {
        $('#add-api-modal').hide();
    });
    $('#api-cancel-btn').on('click', function () {
        $('#add-api-modal').hide();
    });
    // 新增api弹窗
    $('body').on('click','#add-api-link',function () {
        var pro_name = $('h2').html();
        var pro_id = $('h2').data('id');
        // alert(pro_name+pro_id);
        $('#api-project').val(pro_name);
        $('#api-project').attr('data-id',pro_id);
        $('#add-api-modal').show();
    });
    // 提交数据
    $('#api-submit-btn').on('click',function () {
        var url=$('#api-menu-project-id').data('url');
        var data = JSON.stringify({
            api_name:$('#api-name').val(),
            api_project_id: $('#api-project').data('id'),
            api_url: $('#api-url').val(),
            api_meta: $('#api-meta').val(),
            api_status: $('#api-status').val(),
            api_desc: $('#api-desc').val()
        });
        $.ajax({
            contentType: "application/json",
            data:data,
            url:'/apiAdd',
            type:'POST',
            dataType:'json',
            success:function (data) {
                if (data.status == 200){
                    $('#add-api-modal').hide();
                    location.reload(url)
                }
                else {
                    alert(data.message);
                }
            }
        })

    });
})