setTimeout(() => {
   document.querySelector('#msg').style.display = 'none'
}, 3000)

let inputDestino = document.getElementById('#destino')
let inputImagem = document.querySelector('#link')
let inputPreco = document.querySelector('#preco')
let descricao = document.querySelector('#descricao')
let tipoviagem = document.querySelector('#tipo_viagem')
let inputbtn = document.querySelector('#btnCadastro')
let nomeOk = false 
let emailOk = false 
let msgOk = false

btnEnviar.disabled = true




// CAMPO DO DESTINO
inputDestino.addEventListener('keydown', () => { 

    if(inputDestino.value.length < 3 ){
       inputDestino.style.borderColor = 'red' 
       DestinoOk = false
    } else {
       inputDestino.style.borderColor = 'blue' 
       DestinoOk = true
    }
 
    if(inputDestino.value == '' || inputDestino.value == undefined || inputDestino.value == null) {
       inputDestino.style.borderColor = '#ccc'
    }
 

    if (DestinoOk && descricaoOk && precoOK && imagemOK && tipoviagemok) {
       btnEnviar.disabled = false
    } else { 
       btnEnviar.disabled = true
    }
 
 })

//  CAMPO DA IMAGEM
 inputImagem.addEventListener('keydown', () => { 

    if(inputImagem.value.length < 3){
        inputImagem.style.borderColor = 'red' 
       imagemOk = false
    } else {
        inputImagem.style.borderColor = 'blue' 
       imagemOk = true
    }
 
    if(inputImagem.value == '' || inputImagem.value == undefined || inputImagem.value == null) {
        inputImagem.style.borderColor = '#ccc'
    }
 

    if (DestinoOk && descricaoOk && precoOK && imagemOK && tipoviagemok) {
      btnEnviar.disabled = false
   } else { 
      btnEnviar.disabled = true
   }

 
 })

//  CAMPO DE DESCRICAO
descricao.addEventListener('keydown', () => { 

    if(descricao.value.length < 4){
        descricao.style.borderColor = 'red' 
       descricaoOk = false
    } else {
        descricao.style.borderColor = 'blue' 
       descricaoOk = true
    }
 
    if(descricao.value == '' || descricao.value == undefined || descricao.value == null) {
        descricao.style.borderColor = '#ccc'
    }
 

    if (DestinoOk && descricaoOk && precoOK && imagemOK && tipoviagemok) {
      btnEnviar.disabled = false
   } else { 
      btnEnviar.disabled = true
   }

 
 })



// CAMPO DO PRECO
inputPreco.addEventListener('keydown', () => { 
    if(inputPreco.value.length < 4){
       inputPreco.style.borderColor = 'red'
       precoOK = false  
    } else {
       inputNome.style.borderColor = 'blue'
       precoOK = true
    }
 
    if(inputPreco.value == '' || inputPreco.value == undefined || inputPreco.value == null) {
      inputPreco.style.borderColor = '#ccc'
   }
    
    if (DestinoOk && descricaoOk && precoOK && imagemOK && tipoviagemok) {
      btnEnviar.disabled = false
   } else { 
      btnEnviar.disabled = true
   }

 
 
   })


   tipoviagem.addEventListener('keyup', ()=>{
    if(tipoviagem.value.length > 100){
       tipoviagem.style.borderColor = 'red'
       tipoviagemok = false
    } else {
       tipoviagem.style.borderColor = 'green'
       tipoviagemok = true
    }
    
    if(tipoviagem.value == '' || tipoviagem.value == undefined || tipoviagem.value == null) {
      tipoviagem.style.borderColor = '#ccc'
  }
 
 
  if (DestinoOk && descricaoOk && precoOK && imagemOK && tipoviagemok) {
   btnEnviar.disabled = false
} else { 
   btnEnviar.disabled = true
}

 
 
 
 
   })
 


