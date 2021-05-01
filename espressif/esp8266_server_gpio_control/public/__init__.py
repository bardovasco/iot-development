"""
Module to preload the
public html file.
"""
# with open('index.html') as template:
    # webpage = template.read()

def template():
    return """<!DOCTYPE html>
<html>
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arun carrito</title>
    <!--Bootstrap CSS-->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <style>

      .navbar-inverse {
        background: rgba(62, 195, 246, 0);
        border-bottom: none;
      }

      .navbar-inverse .navbar-toggle {
        border: 1px solid #333;
        border-color: rgba(255, 255, 255, 0.7);
      }

      .navbar-inverse .navbar-collapse, .navbar-inverse .navbar-form {
        border-color: transparent;
      }
      @media (max-width: 767px) {
        .navbar-inverse .navbar-collapse, .navbar-inverse .navbar-form {
          background: rgba(255, 255, 255, 0.75);
        }
      }

      .navbar-inverse .navbar-nav > li > a {
        color: black;
      }

      .navbar-inverse .navbar-nav > li > a:hover, .navbar-inverse .navbar-nav > li > a:focus {
        color: #22F;
      }

      /* *********************************
                 Toolbar Logo
        ********************************** */
      .small-logo-container {
        padding-top: 50px;
        height: 50px;
        overflow: hidden;
        position: absolute;
      }

      .small-logo {
        color: white;
        font-size: 2.5em;
        padding-bottom: 2px;
      }

      /* *********************************
                 Big Logo
        ********************************** */
      .big-logo-row {
        background: gold;
      }
      .big-logo-row .big-logo-container {
        padding-top: 50px;
      }
      .big-logo-row h1 {
        font-size: 4em;
        margin: 0;
        padding: 0 0 15px 0;
      }
      @media (min-width: 400px) {
        .big-logo-row h1 {
          font-size: 4.5em;
        }
      }
      @media (min-width: 440px) {
        .big-logo-row h1 {
          font-size: 5.5em;
        }
      }
      @media (min-width: 500px) {
        .big-logo-row h1 {
          font-size: 6.5em;
        }
      }
      @media (min-width: 630px) {
        .big-logo-row h1 {
          font-size: 7.5em;
        }
      }
      @media (min-width: 768px) {
        .big-logo-row h1 {
          font-size: 9em;
          padding-bottom: 30px;
        }
      }
      @media (min-width: 1200px) {
        .big-logo-row h1 {
          font-size: 12em;
        }
      }
    </style>
  </head>
  <body>

   <!-- Fixed navbar -->
    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <div class="small-logo-container">
            <a class="small-logo" href="#">↥Small Logo</a>
          </div>
        </div>
        <div class="navbar-collapse collapse">

          <ul class="nav navbar-nav navbar-right">
            <li class="active"><a href="#">Active</a></li>
            <li><a href="#">Link</a></li>
            <li><a href="#">Link</a></li>
            <li><a href="#">Link</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

    <div class="container-fluid big-logo-row">
      <div class="container">
        <div class="row">
          <div class="col-xs-12 big-logo-container">
            <h1 class="big-logo">↧Arun↧</h1>
          </div><!--/.col-xs-12 -->
        </div><!--/.row -->
      </div><!--/.container -->
    </div><!--/.container-fluid -->

    <div class="container">
      <div class="row">
        <div class="col-sm-12 col-md-4">
          <div class="card" style="width: 18rem;">
            <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fae01.alicdn.com%2Fkf%2FHTB1HkaPOXXXXXbCXVXXq6xXFXXXE%2FMolang-rabbit-Throw-Pillow-Cover-Decorative-Cotton-Linen-Pillow-Slip-Diy-Cushion-Case-Home-Sofa-Car.jpg&f=1&nofb=1" alt="Molang image" class="card-img-top" width="500" height="300">
            <div class="card-body">
              <h5 class="card-title">Carrito</h5>
              <a href="/control=fwd" class="btn btn-success">- Arriba -</a>
              <br />
              <a href="/control=bwd" class="btn btn-info">- Abajo -</a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Optional Javascript -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  </body>
</html>
"""

