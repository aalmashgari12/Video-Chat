// var - Changes with time
// let - changes very fast
// const - constant variable

const cam = document.getElementById('cam');
const mic = document.getElementById('mic');
const smile = document.getElementById('smile');
const end = document.getElementById('end');

var camClicked = false;

 
cam.addEventListener('click', function (){
//    alert("Cam clicked");
    
    if (camClicked == false){
        cam.style.color = 'red';
        camClicked = true;

    }
    else{
        cam.style.color = 'white';
        camClicked = false;

    }
    
});

var micClicked = false;

 
mic.addEventListener('click', function (){
//    alert("Cam clicked");
    
    if (micClicked == false){
        mic.style.color = 'red';
        micClicked = true;

    }
    else{
        mic.style.color = 'white';
        micClicked = false;

    }
    
});

var smileClicked = false;

 
smile.addEventListener('click', function (){
   alert("Reaction clicked");
    
});

var endClicked = false;

 
end.addEventListener('click', function (){
   alert("End Call clicked");
    
});
