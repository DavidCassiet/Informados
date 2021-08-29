const url = window.location.href

const cuestionarioBox = document.getElementById('cuestionario-box')
const puntajeBox = document.getElementById('puntaje-box')
const resultadoBox = document.getElementById('resultado-box')
const timerBox = document.getElementById('timer-box')
var btnsave = false;


const activarTimer = (tiempo) => {
    if (tiempo.toString().length < 2) {
        timerBox.innerHTML = `<h4>0${tiempo}:00</h4>`
    } else {
        timerBox.innerHTML = `<h4>${tiempo}:00</h4>`
    }
    
    let minutos = tiempo - 1
    let segundos = 60
    let displaySegundos
    let displayMinutos

    const timer = setInterval(()=>{
        segundos --
        if (segundos < 0) {
            segundos = 59
            minutos --
        }
        if (minutos.toString().length < 2) {
            displayMinutos = '0' + minutos
        } else {
            displayMinutos = minutos
        }
        if (segundos.toString().length < 2) {
            displaySegundos = '0' + segundos
        } else {
            displaySegundos = segundos
        }
        if (minutos === 0 && segundos === 0) {
            timerBox.innerHTML == "<h4>00:00</h4>"
            setTimeout(()=>{
                clearInterval(timer)
                alert('Tiempo terminado')
                sendData()
            }, 500)
            
        }

        //Para limpiar el timer cuando el usuario apreta Save
        if (btnsave) {
            clearInterval(timer)
        }

        timerBox.innerHTML = `<h4>${displayMinutos}:${displaySegundos}</h4>`
    }, 1000)
}

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        const data = response.data
        data.forEach(el => {
            for (const[pregunta, respuestas] of Object.entries(el)){
                cuestionarioBox.innerHTML += `
                <hr>
                <section>
                    <div clas="container">
                        <div class="row">
                            <div class="col-lg-7 mx-auto">
                                <div class="card shadow border-0 mb-2 bg-danger">
                                    <div class="card-body p-1">
                                    <ul class="list-group">
                                        <li class="list-group-item bg-dark">    
                                            <p class="h4 mb-1 text-center text-white">${pregunta}</p>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
                `
                respuestas.forEach(respuesta=>{
                    cuestionarioBox.innerHTML += `
                    <section>
                    <div clas="container">
                        <div class="row">
                            <div class="col-lg-7 mx-auto">
                                <div class="card shadow border-0 mb-2">
                                    <div class="card-body p-1">
                                        <ul class="list-group">
                                            <li class="list-group-item rounded-0 d-flex align-items-center justify-content-between">
                                                <div class="custom-control custom-radio">
                                                    <input type="radio" class="res" id="${pregunta}-${respuesta}" name="${pregunta}" value="${respuesta}">
                                                    <label class="h5 mb-1 font-italic" for="${pregunta}">${respuesta}</label>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
                    `
                })
            }
        });
        activarTimer(response.tiempo)

    },
    error: function(error){
        console.log(error)
    }
})

const cuestionarioForm = document.getElementById('cuestionario-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendData = () => {
    const elements = [...document.getElementsByClassName('res')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el=>{
        if (el.checked) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })

    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            // console.log(response)
            const resultados = response.resultados
            console.log(resultados)
            cuestionarioForm.classList.add('not-visible')

            puntajeBox.innerHTML = `<h4>${response.pasado ? 'Felicidades! ' : 'Que lástima..:( '}Tu resultado es ${response.puntaje.toFixed(2)}%</h4>`

            resultados.forEach(res=>{
                const resDiv = document.createElement("div")
                for (const [pregunta, resp] of Object.entries(res)){
                    // console.log(pregunta)
                    // console.log(resp)
                    // console.log('*****')

                    resDiv.innerHTML += pregunta
                    const cls = ['container', 'p-3', 'text-light', 'h6']
                    resDiv.classList.add(...cls)

                    if (resp=='no respondida'){
                        resDiv.innerHTML += '- no respondida'
                        resDiv.classList.add('bg-danger')
                    }
                    else {
                        const respuesta = resp['respondida']
                        const correcta = resp['respuesta_correcta']

                        if (respuesta == correcta) {
                            resDiv.classList.add('bg-success')
                            resDiv.innerHTML += ` tu respuesta: ${respuesta} `
                        } else {
                            resDiv.classList.add('bg-danger')
                            resDiv.innerHTML += ` | respuesta correcta: ${correcta} `
                            resDiv.innerHTML += ` | tu respuesta: ${respuesta} `
                        }
                    }
                }
                // const body = document.getElementsByTagName('BODY')[0]
                resultadoBox.append(resDiv)
            })
        },
        error: function(error){
            console.log(error)
        }
    })
}

cuestionarioForm.addEventListener('submit', e=>{
    e.preventDefault()
    btnsave = true
    sendData()
})