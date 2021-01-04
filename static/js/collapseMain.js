'use strict'

let collapse = {
    currentText: document.querySelector('.collapse-item-text'),
    headers: [],
    init() {
        this.headers = document.querySelectorAll('.collapse-item-header')
        this.addEvents()
    },
    addEvents() {
        this.headers.forEach(header => {
            header.addEventListener('click', () => {
                this.hideCurrentText()
                this.openText(header)
            })
        });
    },
    hideCurrentText() {
        this.currentText.classList.add('inactive');

        /* Для того, чтобы не писать this.currentText.parentElement.children[0].children[0].children[0].children[0].innerText = '+', проходимся рекурсией */
        let el = this.findSign(this.currentText.parentElement, '-')
        el.innerText = '+'
    },
    openText(header) {
        /* Для того, чтобы не писать this.currentText.parentElement.children[0].children[0].children[0].children[0].innerText = '+', проходимся рекурсией */
        let el = this.findSign(header, '+')
        el.innerText = '-'

        header = header.parentElement.children[1]
        this.currentText = header
        header.classList.remove('inactive')
    },
    findSign(el, sign) {
        if (el.innerText == sign) {
            return el
        } else {
            return this.findSign(el.children[0], sign)
        }
    }
}

window.addEventListener('load', () => {
    collapse.init();
})