;
var account_set_ops = {
    init:function () {
        this.eventBind()
    },
    eventBind:function(){
        $('.m-t .save').click(function(){
            var btn_save = $(this);
            if (btn_save.hasClass('disabled')){
                alert('请求正在处理！请稍后再试~~~');
                return
            }

            var uid = $('.m-t input[name=uid]').val();
            console.log(uid.length)
            var nickname = $('.m-t input[name=nickname]').val();
            var mobile = $('.m-t input[name=mobile]').val();
            var email = $('.m-t input[name=email]').val();
            var login_name = $('.m-t input[name=login_name]').val();
            var login_pwd = $('.m-t input[name=login_pwd]').val();
            console.log(nickname)
            console.log(mobile)
            console.log(email)
            console.log(login_name)
            console.log(login_pwd)

            if (nickname == undefined || nickname.length < 1){
                alert('请输入符合规范的昵称');
                return
            }
            if (mobile == undefined || mobile.length < 11){
                alert('请输入符合规范的手机号');
                return
            }
            if (email == undefined || email.length < 1){
                alert('请输入符合规范的邮箱');
                return
            }
            if (login_name == undefined || login_name.length < 1){
                alert('请输入符合规范的登录昵称');
                return
            }
            if (login_pwd == undefined || login_pwd.length < 6){
                alert('请输入符合规范的密码');
                return
            }

            btn_save.addClass('disabled');
            if (uid.length >= 1){
                $.ajax({
                    url: common_ops.buildUrl('/account/set?id='+uid),
                    type: 'POST',
                    dataType: 'json',
                    data: {'nickname': nickname, 'mobile': mobile, 'email': email, 'login_name': login_name, 'login_pwd':login_pwd},
                    success: function(resp){
                        btn_save.removeClass('disabled');
                        console.log(resp);
                        alert(resp.msg)

                    },
                    error: function(error){
                        console.log(error)
                    }
                })
            }else{
                $.ajax({
                    url: common_ops.buildUrl('/account/set'),
                    type: 'POST',
                    dataType: 'json',
                    data: {'nickname': nickname, 'mobile': mobile, 'email': email, 'login_name': login_name, 'login_pwd':login_pwd},
                    success: function(resp){
                        btn_save.removeClass('disabled');
                        console.log(resp);
                        alert(resp.msg)

                    },
                    error: function(error){
                        console.log(error)
                    }
                });
            }
        })
    }
};

$(document).ready(function(){
    account_set_ops.init();
});