$(function () {
    $('#case-submit-btn').on('click',function () {
        var data={};
        var task_title = $('#task-name').val();
        var start_time = $('#start-time').val();
        var end_time = $('#end-time').val();
        if(task_title == ""){
            console.log('任务名字不能为空!')
            return
        }
        if(start_time == ""){
            console.log('开始时间不能为空!')
            return
        }
        if(end_time == ""){
            console.log('结束时间不能为空!')
            return
        }
        var interval = $("input[name='optionsRadiosInline']:checked").val();
        var task_desc = $('#task-desc').val();
        var i=0;
        var cList=[];
        $("tr[name='caselist']").each(function () {
            var caseList={};
            var title = $(this).find("td[name='title']").html();
            var project = $(this).find("td[name='project']").html();
            var url = $(this).find("td[name='url']").html();
            var id = $(this).find("td[name='title']").data('id');
            caseList.title = title;
            caseList.project = project;
            caseList.url = url;
            caseList.order=i;
            caseList.id=id;
            i +=1;
            cList.push(caseList);
        });
        data.task_title=task_title;
        data.start_time=start_time;
        data.end_time=end_time;
        data.interval=interval;
        data.task_desc=task_desc;
        data.caseList=cList;
        data=JSON.stringify(data);
        $.ajax({
            contentType: "application/json",
            data: data,
            url: '/addTask',
            type: 'POST',
            dataType: 'json',
            success:function (data) {
                if (data.status == 200){
                    console.log(data.message);
                    self.location="/task";
                }

            }
        });
        console.log(data);
    })
});