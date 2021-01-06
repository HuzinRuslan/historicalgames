new Vue({
    delimiters: ["[[", "]]"],
    el: '#slider_main_app',
    data:{
        sliderItems: [],
        currentSlide: 0,
    },
    created: function(){
        axios.get('api/slider/')
        .then((response)=>{
            console.log(response.data)
            this.sliderItems = response.data
        })
    },
    methods:{
        leftButton(){
            if (this.currentSlide == 0){
                this.currentSlide = this.sliderItems.length - 1;
            }
            else{
                this.currentSlide-=1;
            }
        },
        rightButton(){
            if (this.currentSlide == this.sliderItems.length - 1){
                this.currentSlide = 0;
            }
            else{
                this.currentSlide+=1;
            }
        }
    }
}
)