var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/accounts/login/',
    '/galeria/',
    '/static/core/css/estilos.css',
    '/static/core/imagenes/apolo.jpg',
    '/static/core/imagenes/logo.png',
    '/static/core/imagenes/perro.png',
    '/static/core/imagenes/Tom.jpg',
    '/static/core/imagenes/Apolo.jpg',
    '/static/core/imagenes/Duque.jpg',
    '/static/core/imagenes/social-inst.png',
    '/static/core/imagenes/social-twitter.png',
    '/static/core/imagenes/socialfacebook.png',
    '/static/core/imagenes/socialplus.png',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css',
    'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js',
    '/static/core/js/inicializacion.js',

];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response) {
            if(response) {
                return response;
            }

            return fetch(event.request);
        })
    );
});


importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var config = {
    apiKey: "AIzaSyDPpQu9InV_jyw4LftseVL1evoDknTjbUo",
    authDomain: "misperris-da466.firebaseapp.com",
    databaseURL: "https://misperris-da466.firebaseio.com",
    projectId: "misperris-da466",
    storageBucket: "misperris-da466.appspot.com",
    messagingSenderId: "490679709632"
   };
   firebase.initializeApp(config);

const messaging = firebase.messaging();

//programamos una funcion que estara escuchando cuando llegue una notificacion desde firebase

messaging.setBackgroundMessageHandler(function(payload){
    //el payload contendra el mensaje destinado al usuario
    var title = "Notificacion"
    var options = {
        body : "Este es el cuerpo del mensaje"
    }

    //mostramos la notificacion al usuario
    return self.registration.showNotification(title,options);


})

