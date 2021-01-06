tags = document.querySelectorAll('.flip-icon');

tags.forEach(tag => {
    tagIcon = tag.querySelector('i');
    tagName = tag.children[1].querySelector('p');
    switch(tagName.innerText){
        case "Одиночная игра":
            tagIcon.classList.add("fa-user");
            break
        case "Мультиплеер":
            tagIcon.classList.add("fa-users");
            break
        case "Steam Cloud":
            tagIcon.classList.add("fa-cloud");
            break
        case "Достижения Steam":
            tagIcon.classList.add("fa-medal");
            break
        case "Редактор уровней":
            tagIcon.classList.add("fa-globe-europe");
            break
        case "Поддержка геймпада":
            tagIcon.classList.add("fa-gamepad");
            break
        case "Кооперативная игра":
            tagIcon.classList.add("fa-user-friends");
            break
    }
    
});