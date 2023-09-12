    // Função para abrir o modal
    function openModal() {
        var modal = document.querySelector('.modal');
        modal.style.display = 'block';
    }

    // Função para fechar o modal
    function closeModal() {
        var modal = document.querySelector('.modal');
        modal.style.display = 'none';
    }

    // Event listener para abrir o modal quando o botão "Comprar Agora" é clicado
    var buyButton = document.querySelector('.buy-button');
    buyButton.addEventListener('click', openModal);

    // Event listener para fechar o modal quando o botão "Fechar" é clicado
    var closeButton = document.querySelector('.close');
    closeButton.addEventListener('click', closeModal);

  
    var pixButton = document.getElementById('pixButton');
pixButton.addEventListener('click', function () {
    window.location.href = '/formulario'; // Redirecionar para a rota "/formulario"
});


  
var pixButton = document.getElementById('boletoCartaoButton');
pixButton.addEventListener('click', function () {
    window.location.href = 'https://elegancia-versatil.catalog.yampi.io/cinta-thin-waist-redutora-de-barriga-e-cintura-topp/p';
});



