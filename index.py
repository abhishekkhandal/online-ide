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
                    <li class="nav-item" role="presentation"><a class="nav-link active" href="https://localhost:12345" target="_blank">Geek Stats</a></li>
                    <li class="nav-item" role="presentation"><a class="nav-link active" href="https://github.com/abhishekkhandal/online-ide.git" target="_blank">GitHub Repo</a></li>
                </ul>
        </div>
        </div>
    </nav>
    <main class="page">
        <section class="portfolio-block block-intro" style="height:100%;padding:16px;margin-bottom:12px;">
            <div class="container" style="display: flex; justify-content: center;">
                <div class="about-me" style="width:100%;">
                    <p>Code, Compile & Run.</p>
                    <form action="docker.py" id="form" method="POST">
                    <div class="btn-group btn-group-toggle" data-toggle="buttons"" style="margin:0px 32px 0px 32px;width:100%;">
                        <div class="btn-group btn-group-toggle" data-toggle="buttons">
                          <label class="btn btn-outline-primary active">
                            <input type="radio" name="options" id="option1" autocomplete="off" checked> C
                          </label>
                          <label class="btn btn-outline-primary">
                            <input type="radio" name="options" id="option2" autocomplete="off"> C++
                          </label>
                          <label class="btn btn-outline-primary">
                            <input type="radio" name="options" id="option2" autocomplete="off"> Python 2/3
                          </label>
                          <label class="btn btn-outline-primary">
                            <input type="radio" name="options" id="option2" autocomplete="off"> Fortran
                          </label>
                          <label class="btn btn-outline-primary">
                            <input type="radio" name="options" id="option2" autocomplete="off"> Go
                          </label>
                          <label class="btn btn-outline-primary">
                            <input type="radio" name="options" id="option2" autocomplete="off"> Java
                          </label>
                          <label class="btn btn-outline-primary">
                            <input type="radio" name="options" id="option3" autocomplete="off"> Radio
                          </label>
                        </div>


                        
                        
                    </div>
                    <p style="font-size:14px;"><u>Help:</u> Hit the <strong><b>Go</b></strong> button below.<br> Use <strong><b>howto</b></strong> command to display instructions.</p>
                </div>
            </div>
        </section>
    </main>
    <div class="gradient">
        <div class="container">
        <div class="row" style=" align-items: center; justify-content: center;">
                <div class="col">
                    <div class="table-responsive">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Total Characters</th>
                                    <th>Total Word</th>
                                    <th>Total Lines</th>
                                    <th>Size</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td id="char_count">0</td>
                                    <td id="word_count">0</td>
                                    <td id="line_count">0</td>
                                    <td id="byte_count">0</td>
                                </tr>
                                <tr></tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="col">
                <button class="btn btn-primary" type="submit">GO</button>
            </div>
                </div>
            </div>
            <div class="row" style="display: flex; align-items: center; justify-content: center;">
                <div class="col" style="width:100%;height:100%;margin:5% 0% 5% 0%;"><textarea id="codeArea" wrap="physical" onFocus="window.scrollTo(0, 0);" placeholder="#include <iostream>
using namespace std;

int main() 
{
    cout << 'Hello, World!';
    return 0;
}" style="width:100%;height:500px;padding:2px 2px 0px 2px;" style="width:100%;height:500px;padding:2px 2px 0px 2px;" autofocus></textarea></div>
                <div class="col" style="height:500px;"><iframe id="codeOutput" name="codeOutput" src="matrix.html" style="width:100%;height:100%"></iframe></div>
            </div>
            
        </div>

    </div>
    </form>
    <footer class="page-footer">
        <div class="container">
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

    $('#codeArea').keyup(function() {
      // count total chars
      var text = $(this).val()
      var length = text.length;
      $('#char_count').text(length);
      
      // count total words
      var words = $.trim(this.value).length ? this.value.match(/\S+/g).length : 0;
      $('#word_count').text(words);
      
      // count total lines
      var lines = $("#codeArea").val().split(/\\r|\\r\\n|\\n/);
      var count_lines = lines.length;
      $('#line_count').text(count_lines);

      // count total bytes, UTF-16
      var bytes = 0,
      chars = (text.match(/[\\uD800-\\uDBFF][\\uDC00-\\uDFFF]|[^]/g)||[]).length,
      bytes = text.length * 2;
    $('#byte_count').text(bytes + " B");
      
    });


function getUTF8Length(s) {
  var len = 0;
  for (var i = 0; i < s.length; i++) {
    var code = s.charCodeAt(i);
    if (code <= 0x7f) {
      len += 1;
    } else if (code <= 0x7ff) {
      len += 2;
    } else if (code >= 0xd800 && code <= 0xdfff) {
      // Surrogate pair: These take 4 bytes in UTF-8 and 2 chars in UCS-2
      // (Assume next char is the other [valid] half and just skip it)
      len += 4; i++;
    } else if (code < 0xffff) {
      len += 3;
    } else {
      len += 4;
    }
  }
  return len;
}

    </script>
    
</body>
</html>
""")