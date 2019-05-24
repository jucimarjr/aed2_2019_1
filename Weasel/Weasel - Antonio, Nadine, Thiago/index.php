<!DOCTYPE html>
<html lang="pt">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Programa Doninha - Weaslel</title>



  <!-- Bootstrap core CSS -->
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!--  Fontes customizadas -->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css">

  <!-- Plugin CSS -->
  <link href="vendor/magnific-popup/magnific-popup.css" rel="stylesheet" type="text/css">

  <!-- Folha de estilos -->
  <link href="css/freelancer.min.css" rel="stylesheet">

</head>

<body id="page-top">

  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg bg-secondary fixed-top text-uppercase" id="mainNav">
    <div class="container">
      <a class="navbar-brand js-scroll-trigger" href="#page-top">Weasel program</a>
      <button class="navbar-toggler navbar-toggler-right text-uppercase bg-primary text-white rounded" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        Menu
        <i class="fas fa-bars"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item mx-0 mx-lg-1">
            <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#portfolio">O Programa</a>
          </li>
          <li class="nav-item mx-0 mx-lg-1">
            <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#about">Sobre</a>
          </li>

        </ul>
      </div>
    </div>
  </nav>

  <!-- Header -->
  <header class="masthead bg-primary text-white text-center">
    <div class="container">
      <img class="img-fluid mb-5 d-block mx-auto" src="img/weasel.jpg" alt="">
      <h1 class="text-uppercase mb-0">Weasel Program</h1>
      <hr class="star-light">
      <h2 class="font-weight-light mb-0">O programa de doninhas ou a doninha Dawkins é um experimento mental e uma variedade de simulações de computador que o ilustram. Seu objetivo é demonstrar que o processo que conduz os sistemas evolutivos - variação aleatória combinada com seleção cumulativa não aleatória - é diferente do puro acaso.</h2>
    </div>
  </header>

  <!-- Portfolio Grid Section -->
  <section class="portfolio" id="portfolio">
    <h2 align="center" class="titulo"> Insira os dados no Programa</h2>
    <div align="center" class="container">
                <form class="form-sign" action="doninha.php" method="post">
                    <input type="text" name="target" class="form-control mb-0" placeholder="Insira Target" onkeyup="return AlteraMinusculas(this);">
                    <div class="row">
                      <div class="col-sm">
                        <input type="number" name="geracao" class="form-control mb-0" placeholder="Insira Tamanho de Cada Geração">
                      </div>
                      <div class="col-sm">
                        <input type="number" name="mutacao" class="mb-0 form-control" placeholder="Insira Taxa de Mutação">
                      </div>
                    </div>
                    <input type="submit" class="btn btn-primary" value="Enviar">
                </form>
            </div>
  </section>

  <!-- About Section -->
  <section class="bg-primary text-white mb-0" id="about">
    <div class="container">
      <h2 class="text-center text-uppercase text-white">SOBRE</h2>
      <hr class="star-light mb-5">

      <div class="text-justify mt-5">

          <h5 style="line-height: 1.5" >O programa visa demonstrar que a preservação de pequenas mudanças em uma cadeia de caracteres (ou genes) em evolução pode produzir combinações significativas em um tempo relativamente curto, desde que haja algum mecanismo para selecionar mudanças cumulativas, seja uma pessoa identificando quais características são desejáveis ​​(no caso de seleção artificial) ou um critério de sobrevivência ("fitness") imposto pelo ambiente (no caso da seleção natural). Sistemas de reprodução tendem a preservar traços através das gerações, porque os descendentes herdam uma cópia dos traços dos pais. São as diferenças entre os descendentes, as variações na cópia, que se tornam a base para a seleção, permitindo que frases mais próximas do alvo sobrevivam, e as variantes restantes "morram".</h5></br>

          <h5>Embora Dawkins não fornecesse o código-fonte de seu programa, um algoritmo de estilo "Weasel" poderia ser executado da seguinte maneira.</h5></br>

          <h5>1 - Comece com uma sequência aleatória de 28 caracteres.</h5>

          <h5>2 - Faça 100 cópias desta string, com 5% de chance por personagem daquele personagem sendo substituído por um caractere aleatório.</h5>

          <h5>3 - Compare cada nova string com o alvo "METHINKS IT IS LIKE A WEASEL", e dê a cada uma pontuação (o número de letras na string que estão corretas e na posição correta).</h5>

          <h5>4 - Se alguma das novas strings tiver uma pontuação perfeita (28), pare. Caso contrário, pegue a sequência de pontuação mais alta e vá para a etapa 2.</h5></br>

          <h5 style="line-height: 1.5">Para esses propósitos, um "caractere" é qualquer letra maiúscula ou um espaço. O número de cópias por geração e a chance de mutação por letra não são especificadas no livro de Dawkins; 100 cópias e uma taxa de mutação de 5% são exemplos. Letras corretas não estão "bloqueadas". Cada letra correta pode se tornar incorreta nas gerações subseqüentes. Os termos do programa e a existência da frase alvo, no entanto, significam que tais 'mutações negativas' serão rapidamente 'corrigidas'.</h5>


      </div>
    </div>
  </section>

  <!--
  <section id="contact">
    <div class="container">
      <h2 class="text-center text-uppercase text-secondary mb-0">Dúvidas?</br>Entre em Contato</h2>
      <hr class="star-dark mb-5">
      <div class="row">
        <div class="col-lg-8 mx-auto">
           To configure the contact form email address, go to mail/contact_me.php and update the email address in the PHP file on line 19. -->
          <!-- The form should work on most web servers, but if the form is not working you may need to configure your web server differently.
          <form name="sentMessage" id="contactForm" novalidate="novalidate">
            <div class="control-group">
              <div class="form-group floating-label-form-group controls mb-0 pb-2">
                <label>Nome</label>
                <input class="form-control" id="name" type="text" placeholder="Nome" required="required" data-validation-required-message="Please enter your name.">
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <div class="control-group">
              <div class="form-group floating-label-form-group controls mb-0 pb-2">
                <label>Email</label>
                <input class="form-control" id="email" type="email" placeholder="Email" required="required" data-validation-required-message="Please enter your email address.">
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <div class="control-group">
              <div class="form-group floating-label-form-group controls mb-0 pb-2">
                <label>Número do Telefone</label>
                <input class="form-control" id="phone" type="tel" placeholder="Telefone" required="required" data-validation-required-message="Please enter your phone number.">
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <div class="control-group">
              <div class="form-group floating-label-form-group controls mb-0 pb-2">
                <label>Mensagem</label>
                <textarea class="form-control" id="message" rows="5" placeholder="Mensagem" required="required" data-validation-required-message="Please enter a message."></textarea>
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <br>
            <div id="success"></div>
            <div class="form-group">
              <button type="submit" class="btn btn-primary btn-xl" id="sendMessageButton">Enviar</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
  -->

  <!-- Footer -->
  <footer class="footer text-center">
    <div class="container">
      <div class="row">
        <div class="col-md-4 mb-5 mb-lg-0">
          <h4 class="text-uppercase mb-4">Localização</h4>
          <p class="lead mb-0">UEA - UNIVERSIDADE DO ESTADO DO AMAZONAS
            <br>MANAUS, AMAZONAS</p>
        </div>
        <!--
        <div class="col-md-4 mb-5 mb-lg-0">
          <h4 class="text-uppercase mb-4">Around the Web</h4>
          <ul class="list-inline mb-0">
            <li class="list-inline-item">
              <a class="btn btn-outline-light btn-social text-center rounded-circle" href="#">
                <i class="fab fa-fw fa-facebook-f"></i>
              </a>
            </li>
            <li class="list-inline-item">
              <a class="btn btn-outline-light btn-social text-center rounded-circle" href="#">
                <i class="fab fa-fw fa-google-plus-g"></i>
              </a>
            </li>
            <li class="list-inline-item">
              <a class="btn btn-outline-light btn-social text-center rounded-circle" href="#">
                <i class="fab fa-fw fa-twitter"></i>
              </a>
            </li>
            <li class="list-inline-item">
              <a class="btn btn-outline-light btn-social text-center rounded-circle" href="#">
                <i class="fab fa-fw fa-linkedin-in"></i>
              </a>
            </li>
            <li class="list-inline-item">
              <a class="btn btn-outline-light btn-social text-center rounded-circle" href="#">
                <i class="fab fa-fw fa-dribbble"></i>
              </a>
            </li>
          </ul>
        </div>
        -->

        <div class="col-md-4 mb-5 mb-lg-0">

        </div>


        <div class="col-md-4">
          <h4 class="text-uppercase mb-4">Equipe</h4>
          <p class="lead mb-0">Antonio Rodrigues de Souza Neto </br> Thiago Santos Borges </br> Nadine Cunha Brito </p>
        </div>
      </div>
    </div>



  </footer>

  <div class="copyright py-4 text-center text-white">
    <div class="container">
      <small>Copyright &copy;  2019</small>
    </div>
  </div>

  <!-- Scroll to Top Button (Only visible on small and extra-small screen sizes) -->
  <div class="scroll-to-top d-lg-none position-fixed ">
    <a class="js-scroll-trigger d-block text-center text-white rounded" href="#page-top">
      <i class="fa fa-chevron-up"></i>
    </a>
  </div>


  <!-- Bootstrap core JavaScript -->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Plugin JavaScript -->
  <script src="vendor/jquery-easing/jquery.easing.min.js"></script>
  <script src="vendor/magnific-popup/jquery.magnific-popup.min.js"></script>

  <!-- Form contato js -->
  <script src="js/jqBootstrapValidation.js"></script>
  <script src="js/contact_me.js"></script>

  <!--Scripts customizadas  -->
  <script src="js/freelancer.min.js"></script>
  <script src="java.js"></script>


</body>

</html>
