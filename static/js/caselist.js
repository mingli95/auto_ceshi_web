$(function () {
    // 展开收起
    $(document).ready(function () {
        $(document).on('change','.api-select',function () {
            var req_type=$(this).find("option:selected").data('type');
            if (req_type == undefined){
                req_type="Type"
            };
            console.log(req_type);
            $(this).next().html(req_type);
        });
        $("#quanxuan").on('click',function () {
           var xz = $(this).prop("checked");
           var ck = $('.qx').prop("checked",xz);
        });

        $("#add-case-task").on('click',function () {
            var str=[];
            // $("td input:checkbox:checked").each(function () {
            //     str.push($(this).data('id'));
            // });
            $("tr[name='case-tr']").each(function () {
                var dic = {};
                var this1=$(this);
                var id = this1.find("input:checkbox:checked").data('id');
                var title = this1.find("td[name='title']").html();
                var url = this1.find("td[name='url']").html();
                var project = this1.find("td[name='project']").html();
                if(id != undefined ){
                    dic.id=id;
                    dic.title=title;
                    dic.url=url;
                    dic.project=project;
                    str.push(dic);
                }
            });
            if(str.length ==0){
                alert('请选择用例！')
            }
            else {
                var data = JSON.stringify({
                    caselist:str
                });
                self.location="/getCaseList?caselist="+data;
            }
            console.log(str);
        });
        $.ajax({
            type:'POST',
            url:'/serverList',
            dataType: 'json',
            success:function (data) {
                var data = data.data;
                for (var i=0;i<data.length;i++){
                    $('#server-addr').append('<option data-id='+data[i].id+' >'+data[i].name+'</option>')
                }
            }
        });
        caseList();
        $(document).on('click','#api-caselist',function () {
            caseList();
        });
        function caseList(){
            var data = JSON.stringify({
                project_id:$('#case-menu-project-id').data('id'),
                title:$('#name').val()
            });
            $.ajax({
                contentType: "application/json",
                data: data,
                url: '/caseList',
                type: 'POST',
                dataType: 'json',
                success: function (data) {
                    if (data.status == 200) {
                        var html = '';
                        for (var i = 0; i < data.data.length; i++) {
                            html = html + "<tr name='case-tr'>" +
                                "<td><input type='checkbox' class='qx' data-id="+data.data[i].id+"></td>" +
                                "<td name='title'>" + data.data[i].title + "</td>" +
                                "<td name='project'>" + data.data[i].project_id + "</td>" +
                                "<td name='url'>" + data.data[i].server_id + "</td>" +
                                "<td>" + data.data[i].status + "</td>" +
                                "<td>" + data.data[i].count + "</td>" +
                                "<td><a> 编辑</a><a> 复制</a><a> 删除</a><a> 禁用</a></td>" +
                                "</tr>"
                            document.getElementById("table-tbody").innerHTML = html;
                        }
                    }
                }
            });
        };
    });
    $(document).on('click','.toggle-btn',function () {
      $(this).next().slideToggle();
    });
    // 添加断言表达式
    $(document).on('click','.add-ast',function () {
        $(this).next().find('tbody').append('<tr name="tr_assert">\
            <td><input class="form-input" name="ast_key" style="width: 400px" type="text"/></td>\
            <td><input class="form-input" name="ast_val" style="width: 400px" type="text"/></td>\
            </tr>');
    });
    // 添加出参表达式
    $(document).on('click','.add-dataPass',function () {
        $(this).next().find('tbody').append(
            '<tr name="out_param">\
            <td><input class="form-input" style="width: 400px" type="text" name="out_parm_key" /></td>\
            <td><input class="form-input" style="width: 400px" type="text" name="out_parm_val" /></td>\
            <td><select class="form-input" name="out_parm_type">\
            <option selected = selected" >Str</option>\
        <option>Int</option>\
        </select></td>\
        </tr>'
        );
    });
    // 添加Api
    var html = $('.add-api').html();
    $('.add-case-api').on('click',function () {
        $('.add-api').append(html);
    });

    $(document).on('click','#case-submit-btn',function () {
        var data = {};
        data.title = $('#case-name').val();
        data.project_id = $('#case-project').data('id');
        data.server_id = $('#server-addr').find("option:selected").data('id');
        data.status = $('#case-status').val();
        data.desc = $('#case-desc').val();
        var apiList = [];
        var i=0;
        $('.api').each(function () {
            var this1 = $(this);
            var api = {};
            api.order = i;
            api.api_id = this1.find('.api-select option:selected').data('id');
            api.request = this1.find('textarea[name="req_data"]').val();

            var assert = [];
            this1.find('tr[name="tr_assert"]').each(function () {
                var this2 = $(this);
                var ast = {
                    key:this2.find('input[name="ast_key"]').val(),
                    val:this2.find('input[name="ast_val"]').val()
                };
                assert.push(ast);
            });
            api.assert = assert;

            var out_param = [];
            this1.find('tr[name="out_param"]').each(function () {
                var this3 = $(this);
                var outParam = {
                    key:this3.find('input[name="out_parm_key"]').val(),
                    val:this3.find('input[name="out_parm_val"]').val(),
                    type:this3.find('select[name="out_parm_type"]').val()
                };
                out_param.push(outParam);
            });
            api.out_param = out_param;

            if (api.api_id != undefined){
                apiList.push(api);
            };
            i++;
        });
        data.apiList=apiList;
        data=JSON.stringify(data);
        console.log(data);
        $.ajax({
            contentType: "application/json",
            url:'/caseSubmit',
            type:'POST',
            dataType: 'json',
            data:data,
            success:function (data) {
                if (data.status == 200){
                    console.log(data.message);
                    var url_path=$('#case-title').data('url');
                    console.log(url_path)
                    self.location=url_path;
                }
                else{
                    alert(data.message);
                }
            }
        })
    });
});
