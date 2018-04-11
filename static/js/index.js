$(function () {
    $(document).ready(function(){
        $.ajax({
            data:data,
            url:'/menuList',
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
        });
    });
})