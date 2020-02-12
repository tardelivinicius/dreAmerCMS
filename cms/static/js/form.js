$(document).ready(function() {
    $('form').on('submit', function(event) {
        event.preventDefault();
        $.ajax({
			url: 'step1',
			method: "POST",
			data: $(this).serialize(),
            dataType: 'json',
            async: false,
            success: function(result) {
                localStorage.setItem('register-email', result['register-mail']);
                localStorage.setItem('register-password', result['register-password']);
                localStorage.setItem('register-username', result['register-username']);
                window.location.href = '?step=2'
            },
            error: function() {
                alert("Ocorreu um erro ao carregar os dados.");
              }
        });
    })
})