
/* Habilitar a passagem de imagem pelo scroll */
document.querySelector("#item")
.addEventListener("wheel", event => {
    if(event.deltaY >0) {
        event.target.scrollBy(300, 0)
    } else {
        event.target.scrollBy(-300, 0)
    }
})