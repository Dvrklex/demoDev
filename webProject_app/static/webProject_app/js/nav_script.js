// Obtener todos los elementos "li" en la barra de navegación
const navItems = document.querySelectorAll('.list');

// Obtener el índice del elemento activo del localStorage
const activeItemIndex = localStorage.getItem('activeNavItem');

// Variable de estado para verificar si el elemento "active" ya se ha establecido
let activeSet = false;

// Función para manejar el comportamiento de hacer clic en un elemento "li"
function handleClick(item, index) {
  if (!activeSet) {
    event.preventDefault(); // detener la acción predeterminada del enlace solo si el "active" aún no se ha establecido
  }
  if (!item.classList.contains('active')) {
    navItems.forEach(item => {
      item.classList.remove('active');
    });
    item.classList.add('active');
    activeSet = true; // establecer la variable de estado como verdadera una vez que se establece el "active"
    localStorage.setItem('activeNavItem', index); // guardar el índice del elemento activo en localStorage
    setTimeout(() => {
      window.location.href = item.getAttribute('data-url'); // redirigir a la URL después de que se establece el atributo "active"
    }, 500);
  }
}

// Agregar un controlador de eventos de clic a cada elemento "li"
navItems.forEach((item, index) => {
  item.addEventListener('click', (event) => {
    handleClick(item, index);
  });

  // Restaurar el estado del elemento activo al cargar la página
  // if (activeItemIndex && index === Number(activeItemIndex)) {
  //   item.classList.add('active');
  // }
  // Comentando la linea de codigo de arriba lo resuelve, no agrega active al cambiar la url manualmente, 
  // pero no deja activo el elemento <li> anterior al cambiar la url manualmente.
  console.log('Muestro la URL actual: ' + window.location.href);

  // Muestro la url si se cambia manualmente
});

// Función para verificar si la URL ha sido cambiada manualmente
// function checkUrlChange() {
//   const currentUrl = window.location.href;
//   const storedUrl = localStorage.getItem('storedUrl');

//   if (currentUrl !== storedUrl) {
//     console.log('La URL ha sido cambiada manualmente');
//   }

//   // Actualizar la URL almacenada en el localStorage
//   localStorage.setItem('storedUrl', currentUrl);
// }

// // Llamar a la función al cargar la página
// checkUrlChange();


//Resuelve el problema de que el elemento "active" no se establece al cambiar la url manualmente, pero 
//afecta a la fluidez de la pagina y la animacion del active.
// // Función para establecer el elemento "active" en base a la URL actual
// function setActiveNavItem() {
//   const currentPath = window.location.pathname;
//   navItems.forEach(item => {
//     if (item.getAttribute('data-url') === currentPath) {
//       item.classList.add('active');
//       activeSet = true;
//     } else {
//       item.classList.remove('active');
//     }
//   });
// }
 

 
//Resuelve el problema de que el elemento "active" no se establece al cambiar la url manualmente, pero 
//afecta a la fluidez de la pagina y la animacion del active.
// // Función para establecer el elemento "active" en base a la URL actual
// function setActiveNavItem() {
//   const currentPath = window.location.pathname;
//   navItems.forEach(item => {
//     if (item.getAttribute('data-url') === currentPath) {
//       item.classList.add('active');
//       activeSet = true;
//     } else {
//       item.classList.remove('active');
//     }
//   });
// }
 
//posible solucion, pero afecta a la fluidez de la pagina y la animacion del active.
// if (activeItemIndex && index === Number(activeItemIndex)) {
//   if (item.getAttribute('data-url') === currentPath) {
//     item.classList.add('active');
//     activeSet = true; // establecer la variable de estado como verdadera una vez que se establece el "active"
//     localStorage.setItem('activeNavItem', index); // guardar el índice del elemento activo en localStorage
//     setTimeout(() => {
//       window.location.href = item.getAttribute('data-url'); // redirigir a la URL después de que se establece el atributo "active"
//     }, 500);
//     console.log('Muestro el nombre del elemento activo: ' + item.getAttribute('data-url'));
// }
// else {
//         item.classList.remove('active');
//       }
//     }