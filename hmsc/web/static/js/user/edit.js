;
var user_edit_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        // 获取保存按钮
        $('.user_edit_wrap .save').click(function(){

            // console.log('edit');
            var btn_save = $(this);
            if (btn_save.hasClass('disabled')){
                alert('请求正在处理，请稍后再试~~~');
                return
            }
            var nickname = $('.user_edit_wrap input[name=nickname]').val();
            var email = $('.user_edit_wrap input[name=email]').val();

            if (nickname==undefined || nickname.length < 1){
                alert('请输入规范的昵称');
                return false
            }
            if (email==undefined || email.length < 1){
                alert('请输入规范的邮箱');
                return false
            }
            btn_save.addClass('disabled');
            $.ajax({
                url: common_ops.buildUrl('/user/edit'),
                type: 'POST',
                dataType: 'json',
                data: {'nickname': nickname, 'email': email},
                success:function(resp){

                    btn_save.removeClass('disabled');
                    console.log(resp);
                    alert(resp.msg);

                },
                error:function(error){
                    console.log(error)
                }
            })
        })
    }
};

$(document).ready(function(){
    user_edit_ops.init();
});