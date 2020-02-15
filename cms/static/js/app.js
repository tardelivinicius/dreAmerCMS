var i = 0;
$(document).ready(function() {
    var AnimationHelper=(function(){var b=500;var a="webkitTransitionEnd transitionend oTransitionEnd MSTransitionEnd transitionend";
        return{animate:function(d,e,f,c){if(!c){c=b}if(Modernizr.csstransitions){d.css("transition","all "+c+"ms ease-in-out");d.css(e);if($.isFunction(f)){d.bind(a,function(){d.unbind(a);f()})}}else{if($.isFunction(f)){d.animate(e,{duration:c,easing:"easeInOutQuart",queue:false,complete:f})}else{d.animate(e,{duration:c,easing:"easeInOutQuart",queue:false})
        }}}}})();

        var f = 950;
        var d = 650;
        var b = 1450;

        var Landing = (function() {
            return {
                scrollToLogin: function(h) {
                    var g = [f, d, b];
                    if(h) {g = [f / 10, d / 10, b / 10];}

                    AnimationHelper.animate($(".welcome-text"), {top: "-500px"}, null, g[1]);
                    AnimationHelper.animate($(".login-position"), {top: "0"}, null, g[1]);
                },
                scrollToHome: function() {
                    AnimationHelper.animate($(".welcome-text"), {top: "0px"}, null, d);
                    AnimationHelper.animate($(".login-position"), {top: "500px"}, null, d);
                }
            }
        })();

    if(window.location.hash === "#login") {
        Landing.scrollToLogin(true);
    }

    $(window).bind("hashchange", function(){
        if(window.location.hash === "#login") {
            Landing.scrollToLogin();
        } else {
            if(window.location.hash === "#home" || window.location.hash === ""){
                Landing.scrollToHome();
            }
        }
    });

    $("#login-submit").click(function(e) {
        if (0 === $("#login-username").length || 0 == $("#login-username").length) {
            $(".alert").css({display: "block"}).html("Vergiss nicht alle Felder auszufüllen!");
        } else {
            $.ajax({
                type: "POST",
                url: "account/login",
                data: {
                    username: $("#login-username").val(),
                    password: $("#login-password").val(),
                    token: $("#token").val()
                },
                success: function(res) {
                    if (!res.data.valid) {
                        $('.alert').css({display: "block"}).html(res.data.response);
                    } else {
                        window.location.href = 'me';
                    }
                }
            });
        }
        e.preventDefault();
    });

    $(".male").click(function() {
        $(this).addClass("selected");
        $(".female").removeClass("selected");
    });

    $(".female").click(function() {
        $(this).addClass("selected");
        $(".male").removeClass("selected");
    });

    $('.news-article').each(function(index, e) {
        i++;
    });

    $('.back-news').click(function() {
        var prevSlide = currentSlide - 1;
        if(prevSlide < 1) {
            goToSlide(i);
        } else {
            goToSlide(prevSlide);
        }
    });

    $('.next-news').click(function() {
        var nextSlide = currentSlide + 1;
        if(nextSlide > i) {
            goToSlide(1);
        } else {
            goToSlide(nextSlide);
        }
    });

    startSlide();

    $(".btnset").each(function () {
        $(this).buttonset();
    });
});

var currentSlide = 1;
var interval;

function startSlide() {
    clearInterval(interval);
    interval = setInterval(function() {
        nextSlide();
    }, 6000);
}

function nextSlide() {
    if(currentSlide < i) {
        currentSlide++;
    } else {
        currentSlide = 1;
    }

    goToSlide(currentSlide);
}

function goToSlide(current) {
    clearInterval(interval);
    currentSlide = current;

    $('.news-article').stop().fadeOut(function () {
        $(this).removeClass('show').addClass('hide');
    });

    $('.news-article:nth-child(' + current + ')').stop().fadeIn(function () {
        $(this).addClass('show').removeClass('hide');
    });

    if (i > 1) {
        startSlide();
    }
}