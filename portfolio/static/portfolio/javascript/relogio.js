function relogio(){
    var dateTime = new Date();
    var hours = dateTime.getHours();
    var minutes = dateTime.getMinutes();
    var seconds = dateTime.getSeconds();
    var session = document.getElementById('horario');

    document.getElementById('horas').innerHTML = hours;
    document.getElementById('minutos').innerHTML = minutes;
    document.getElementById('segundos').innerHTML = seconds;

}

setInterval(relogio, 10);