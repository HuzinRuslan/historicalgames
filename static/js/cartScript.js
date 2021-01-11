window.onload = ()=> {
    $('.cart-wrapper').on('click', 'input[type="number"]', ()=>{
        let target_href = event.target;

        if (target_href) {
            $.ajax({
                url:'/cart/cart_edit/' + target_href.name + '/' + target_href.value+ '/',
                success: (data) => {
                    $('.cart-wrapper').html(data.result);
                },
            });
        }
        event.preventDefault();
    });
};