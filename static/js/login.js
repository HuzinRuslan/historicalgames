window.onload = () => {
    const signInButton = document.getElementById('signIn');
    const container = document.getElementById('container');

    $('#signUp').on('click', () => {
        container.classList.add("right-panel-active");
        let form = $('.reg_form')
        $.get(form.attr('action'), data => {
            $('#reg_form').html(data.form_html);
        });
        event.preventDefault();
    });

    $('#signIn').on('click', () => {
        container.classList.remove("right-panel-active");
        let form = $('.login_form')
        $.get(form.attr('action'), data => {
            $('#log_form_div').html(data.form_html);
        });
        event.preventDefault();
    });

    $('#reg_confirm').on('click', () => {
        let form = $('.reg_form')
        $.post(form.attr('action'), form.serialize(), data => {
            if (! data.form_is_valid) {
                $('#reg_form').html(data.form_html);
            }
            else{
                signInButton.click()
            };
        });
        event.preventDefault();
    });

    $('#log_confirm').on('click', () => {
        let form = $('.login_form')
        $.post(form.attr('action'), form.serialize(), data => {
            if (! data.form_is_valid) {
                $('#log_form_div').html(data.form_html);
            }
            else{
                window.location.href = data.form_html;
            };
        });
    })
};