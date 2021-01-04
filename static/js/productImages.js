'use strict'

let imageSwap = {
    mainImage: document.querySelector('.main-image'),
    smallImages: document.querySelectorAll('.small-image'),
    activeImage: '',
    init(){
        this.activeImage = this.smallImages[0];
        this.addEvents();
    },
    addEvents(){
        this.smallImages.forEach(image => {
            image.addEventListener('click', ()=>{
                this.makeImageMain(image);
            })
        });
    }, 
    makeImageMain(image){
        this.activeImage.classList.remove('active-product-image');
        image.classList.add('active-product-image');
        this.activeImage = image;
        this.mainImage.src = image.src;
    }
}

imageSwap.init();