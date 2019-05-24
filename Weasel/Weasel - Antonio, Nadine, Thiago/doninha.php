<?php

$target = $_POST["target"];
$geracao = $_POST["geracao"];
$mutacao = $_POST["mutacao"];

$alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ";

function randomChr() {
    $alphabet = $GLOBALS['alphabet'];
    return $alphabet[rand(0,26)];
}

function randomStr() {
    $target = $GLOBALS['target'];
    $randomStr = '';
    for ($i=0; $i < strlen($target); $i++) {
        $randomStr = $randomStr . randomChr();
    }
    return $randomStr;
}

function compareStr($randomStr){
    $target = $GLOBALS['target'];
    $randomStrIndex = 0;
    for ($i=0; $i < strlen($target); $i++) {
        if($target[$i] == $randomStr[$i]){
            $randomStrIndex++;
        }
    }
    return $randomStrIndex;
}

function modRandomStr($randomStr){
    $target = $GLOBALS['target'];
    $newRandomStr = $randomStr;
    for ($i=0; $i < strlen($target); $i++) {
        $randomInt = rand(1,100);
        $mutacao = $GLOBALS['mutacao'];
        if($randomInt <= $mutacao){
            $newRandomStr = substr($newRandomStr, 0, $i) . randomChr() . substr($newRandomStr, ($i + 1));
        }
    }
    return $newRandomStr;
}

function getIndex($indexList, $maxIndex){
    $index = 0;
    for ($i=0; $i < count($indexList); $i++) {
        // code...
        if ($indexList[$i] == $maxIndex) {
            $index = $i;
        }
    }
    return $index;
}

$loopNumber = 0;
$strFound = false;
$randStr = randomStr();
$loopNumberList=[];
$randomStrList=[''];
$maxIndexList=[];
while(!$strFound){
    $strList = [];
    $indexList = [];
    $geracao = $GLOBALS['geracao'];
    for ($i=0; $i < $geracao; $i++) {
        // code...
        $strList[$i] = '';
        $indexList[$i] = NULL;
    }
    for ($i=0; $i < $geracao; $i++) {
        $strList[$i] = modRandomStr($randStr);
        $indexList[$i] = compareStr($strList[$i]);
    }
    $maxIndex = max($indexList);
    if($maxIndex == strlen($target)){
        $strFound = true;
    }
    $index = getIndex($indexList, $maxIndex);
    $randStr = $strList[$index];

    $loopNumberList[$loopNumber] = $loopNumber;
    $randomStrList[$loopNumber] = $randStr;
    $maxIndexList[$loopNumber] = $maxIndex;
    $loopNumber++;
}
 ?>

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

   <!--     Fontes do projeto -->
   <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
   <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
   <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css">

   <!-- Plugin CSS -->
   <link href="vendor/magnific-popup/magnific-popup.css" rel="stylesheet" type="text/css">

   <!-- Folha de estilos -->
   <link href="css/freelancer.min.css" rel="stylesheet">


 </head>

 <body id="page-top">

   <!-- Navegação -->
   <nav class="navbar navbar-expand-lg bg-secondary fixed-top text-uppercase" id="mainNav">
     <div class="container">
       <a class="navbar-brand js-scroll-trigger" href="index.php">Weasel program</a>
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

   <!--         O programa -->
   <section class="portfolio" id="portfolio">
       <div align="center" class="container">
           <div class="row">
               <div class="col-sm">
                   <h1 class="h5 font-weight-light mb-0">Geração</h1>
                   <?php
                   for ($i=0; $i < sizeof($loopNumberList); $i++) {
                       // code...
                       echo "<p class='mb-0'>".$loopNumberList[$i]. "</p>";
                   } ?>
               </div>
               <div class="col-XL-10">
                   <h1 class="h5 font-weight-light mb-0">Texto da Geração</h1>
                   <?php
                   for ($i=0; $i < sizeof($randomStrList); $i++) {
                       // code...
                       echo "<p class='mb-0'>".$randomStrList[$i]. "</p>";
                   } ?>
               </div>
               <div class="col-sm">
                   <h1 class="h5 font-weight-light mb-0">Score</h1>
                   <?php
                   for ($i=0; $i < sizeof($maxIndexList); $i++) {
                       // code...
                       echo "<p class='mb-0'>".$maxIndexList[$i]. "</p>";
                   } ?>
               </div>
           </div>
       </div>
   </section>

   <!-- Sobre -->
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


   <!-- Footer -->
   <footer class="footer text-center">
     <div class="container">
       <div class="row">
         <div class="col-md-4 mb-5 mb-lg-0">
           <h4 class="text-uppercase mb-4">Localização</h4>
           <p class="lead mb-0">UEA - UNIVERSIDADE DO ESTADO DO AMAZONAS
             <br>MANAUS, AMAZONAS</p>
         </div>
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

   <!-- Contato Js -->
   <script src="js/jqBootstrapValidation.js"></script>
   <script src="js/contact_me.js"></script>

   <!--Scripts customizadas -->
   <script src="js/freelancer.min.js"></script>
   <script src="java.js"></script>


 </body>

 </html>
