;
var user_reset_pwd = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $('#save').click(function(){
            var save_btn = $(this);
            if(save_btn.hasClass('disabled')){
                alert('请求正在处理！请稍后再试');
                return;
            }

            var old_pwd = $('#old_password').val();
            var new_pwd = $('#new_password').val();

            // 前段校验
            if (old_pwd == undefined || old_pwd.length < 1){
                alert('请输入原密码！');
                return
            }
            if (new_pwd == undefined || new_pwd.length < 1){
                alert('请输入新密码！');
                return
            }
            if (new_pwd.length < 6){
                alert('密码长度不得小于6位');
                return
            }
            if(old_pwd == new_pwd){
                console.log(old_pwd);
                console.log(new_pwd);
                alert('两次密码不能相同 ^！^');
                return
            }
            save_btn.addClass('disabled');
            $.ajax({
                url: common_ops.buildUrl('/user/reset-pwd'),
                type: 'POST',
                data: {'old_pwd': old_pwd, 'new_pwd': new_pwd},
                dataType: 'json',
                success:function(resp){
                    console.log('这里执行了');
                    save_btn.removeClass('disabled');
                    console.log(resp);
                    alert(resp.msg)
                },
                error:function(error){
                    console.log(error)
                }

            })
        })
    }
};


$(document).ready(function(){
    user_reset_pwd.init();
});