const modalBtns = [...document.getElementsByClassName("btn btn-outline-success")]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const nombre = modalBtn.getAttribute('data-cuestionario')
    const numPreguntas = modalBtn.getAttribute('data-preguntas')
    const categorias = modalBtn.getAttribute('data-categorias')
    const puntajeRequerido = modalBtn.getAttribute('data-pass')
    const tiempo = modalBtn.getAttribute('data-tiempo')
    
    modalBody.innerHTML = `
        <div class="h5 mb-3">¿Estas seguro que queres empezar "<b>${nombre}</b>"?</div>
        <div class=text-muted
            <ul>
                <li>Categoria: <b>${categorias}</b></li>
                <li>Cantidad de preguntas: <b>${numPreguntas}</b></li>
                <li>Puntaje requerido: <b>${puntajeRequerido}%</b></li>
                <li>Tiempo: <b>${tiempo} min</b></li>
            </ul>
        </div>
    `

    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
}))