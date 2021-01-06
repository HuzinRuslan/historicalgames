window.onload = ()=> {
    $('.show-more-catalog').on('click', ()=>{
        let target = event.target;
        gallery = document.querySelector('.gallery-products');

        if (target) {
            $.ajax({
                url:'/catalog/update/' + gallery.children.length + '/',
                success: (data) => {
                    $('.gallery-products').append(data.result);

                    if (gallery.children.length % 4 !=0){
                        $('.show-more-catalog-wrapper').remove();
                    }
                },
            });
        }
        event.preventDefault();
    });
};