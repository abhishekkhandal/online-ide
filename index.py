#!/usr/bin/python3

import cgi,json

print("Content-type:text/html\r\n\r\n")        
print ("""
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Platform as a Service</title>
    <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato:300,400,700">
    <link rel="stylesheet" href="assets/fonts/ionicons.min.css">
</head>

<body>
    <nav class="navbar navbar-dark navbar-expand-lg bg-white portfolio-navbar gradient">
        <div class="container"><a class="navbar-brand logo" href="#"><b>Platform as a Service</b></a><button class="navbar-toggler" data-toggle="collapse" data-target="#navbarNav"><span class="sr-only">Toggle navigation</span><span class="navbar-toggler-icon"></span></button>
            <div
                class="collapse navbar-collapse" id="navbarNav">
                <ul class="nav navbar-nav ml-auto">
                    <li class="nav-item" role="presentation"><a class="nav-link active" href="https://github.com/abhishekkhandal/online-ide.git" target="_blank">GitHub Repo</a></li>
                </ul>
        </div>
        </div>
    </nav>
    <main class="page">
        <section class="portfolio-block block-intro" style="height:100%;padding:22px;margin-bottom:20px;">
            <div class="container" style="margin-bottom:0px;">
                <div class="about-me" style="width:100%;">
                    <p>Code, Compile & Run.</p>
                    <form action="docker.py" id="form" method="POST">
                    <div class="form-group" style="margin:0px 32px 0px 32px;width:100%;">
                        <div class="table-responsive" style="height:100%;width:90%;">
                            <table class="table">
                                <thead style="height:100%;width:100%;">
                                    <tr style="background-color:rgba(136,123,130,0.08);height:100%;width:100%;">
                                        <th>
                                            <div class="form-check"><input class="form-check-input" type="radio" name="lang" value="C" id="language" style="height:18px;"><label class="form-check-label" for="language">C</label></div>
                                        </th>
                                        <th>
                                            <div class="form-check"><input class="form-check-input" type="radio" name="lang" value="CPP" id="language" checked><label class="form-check-label" for="language">C++</label></div>
                                        </th>
                                        <th style="margin:12px;padding:12px;">
                                            <div class="form-check"><input class="form-check-input" type="radio" name="lang" value="python2" disabled="" id="language"><label class="form-check-label" for="language">Python2</label></div>
                                        </th>
                                        <th>
                                            <div class="form-check"><input class="form-check-input" type="radio" name="lang" value="python3" disabled="" id="language"><label class="form-check-label" for="language">Python3</label></div>
                                        </th>
                                        <th>
                                            <div class="form-check"><input class="form-check-input" type="radio" name="lang" value="php" disabled="" id="language"><label class="form-check-label" for="language">PHP</label></div>
                                        </th>
                                        <th>
                                            <div class="form-check"><input class="form-check-input" type="radio" name="lang" value="go" disabled="" id="language"><label class="form-check-label" for="language">Go</label></div>
                                        </th>
                                        <th>
                                            <div class="form-check"><input class="form-check-input" type="radio" name="lang" value="java8" disabled="" id="language"><label class="form-check-label" for="language">Java8</label></div>
                                        </th>
                                    </tr>
                                </thead>
                            </table>
                        </div>
                        <p style="font-size:14px;">Demo: Hit the <strong><b>Go</b></strong> button below.<br> Type <strong><b>./main</b></strong> and hit Enter.</p>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <div class="gradient">
        <div class="container">
            <div class="row" style="margin:0% 0% 0% 0%;" id="iframe">
                <div class="col" style="width:100%;height:100%;margin:5% 0% 5% 0%;"><textarea id="codeArea" style="width:100%;height:500px;padding:2px 2px 0px 2px;" id="inp" ></textarea></div>
                <div class="col-md-6" style="margin:5% 0% 5% 0%;width:100%;height:100%;"><iframe id="codeOutput" name="codeOutput" src="#" style="width:100%;height:500px"></iframe></div>
            </div>
                <button class="btn btn-primary" type="submit" style="font-size:18px;margin:0% 0% 5% 45%;padding:6px 28px;width:100px;">GO</button>
        </div>
    </div>
    </form>
    <footer class="page-footer">
        <div class="container">
            <div class="links"><a href="#">About me</a><a href="#">Contact me</a><a href="#">Projects</a></div>
            <div class="social-icons"><a href="https://www.linkedin.com/in/abhishekkhandal/" target="_blank"><i class="icon ion-social-linkedin"></i></a><a href=""><i class="icon ion-social-github"></i></a><a href="mailto:akhandal69@gmail.com"><i class="icon ion-email"></i></a></div>
        </div>
    </footer>
    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
        <script>
        $("#form").submit(function(){
        var code = $('textarea#codeArea').val();
        var language = $('#language').val();
        var jsonMimeType = "application/json;charset=UTF-8";
        $.ajax({
          type: "POST",
          url: "docker.py",
          data: {"language": language, "code" : code },
          
          beforeSend: function(x) {
          if(x && x.overrideMimeType) {
           x.overrideMimeType(jsonMimeType);
          }
         },
         dataType: "json",
         success: function (d) {
                document.getElementById("codeOutput").src = d.url;
          },
          error: function(d) {
            var data = d;
            //document.getElementById("codeOutput").src = data.url;
            //console.log(d.url);
          }
        }); 
    
    return false;
    });
    </script>
    
</body>
</html>
""")