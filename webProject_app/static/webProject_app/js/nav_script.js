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

   
  console.log('Muestro la URL actual: ' + window.location.href);

  
});



