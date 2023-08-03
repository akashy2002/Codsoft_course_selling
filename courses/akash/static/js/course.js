var player;
window.onload = () => {
    player = document.getElementById('player')
}
function mentainRatio() {
    var w = player.clientWidth
    var h = (w * 9) / 16
    player.height = h
}
window.onresize = mentainRatio