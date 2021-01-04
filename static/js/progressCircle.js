'use strict'

let progressCircle = {
    circle: document.querySelector('.progress-circle-ring'),
    scoreDiv: document.querySelector('.progress-score'),
    init() {
        this.score = this.scoreDiv.innerHTML;
        this.radius = this.circle.r.baseVal.value;
        this.circumference = 2 * Math.PI * this.radius;
        this.circle.style.strokeDasharray = `${this.circumference} ${this.circumference}`;
        this.circle.style.strokeDashoffset = this.circumference;
        this.setProgress(this.score);
    },
    setProgress(percent) {
        const offset = this.circumference - percent / 100 * this.circumference;
        this.circle.style.strokeDashoffset = offset;
    }
}
let progressCirclePart = {
    circle1: document.querySelector('.progress-circle-part-1'),
    circle2: document.querySelector('.progress-circle-part-2'),
    circle3: document.querySelector('.progress-circle-part-3'),
    circle4: document.querySelector('.progress-circle-part-4'),
    scoreDiv: document.querySelector('.progress-score-string'),
    init() {
        this.score = this.scoreDiv.innerText;
        this.radius = this.circle1.r.baseVal.value;
        this.circumference = 2 * Math.PI * this.radius;
        this.space = this.circumference / 4 * 0.10;
        this.part = this.circumference / 4 - this.space;
        this.circle1.style.strokeDasharray = `${this.part} ${this.circumference - this.part}`;
        this.circle2.style.strokeDasharray = `${this.part} ${this.circumference - this.part}`;
        this.circle3.style.strokeDasharray = `${this.part} ${this.circumference - this.part}`;
        this.circle4.style.strokeDasharray = `${this.part} ${this.circumference - this.part}`;

        this.setProgress(this.score)
        console.log(this.score)
    },
    setProgress(percent) {
        if (percent == "Bad"){
            this.circle2.style.display = "none";
            this.circle3.style.display = "none";
            this.circle4.style.display = "none";
        }
        else if (percent == "Alright"){
            this.circle3.style.display = "none";
            this.circle4.style.display = "none";
        }
        else if (percent == "Good"){
            this.circle4.style.display = "none";
        }
        else if (percent == "Perfect"){
            ;
        }
        else{
            this.circle1.style.display = "none";
            this.circle2.style.display = "none";
            this.circle3.style.display = "none";
            this.circle4.style.display = "none";
        }
    }
}

progressCircle.init();
progressCirclePart.init();
