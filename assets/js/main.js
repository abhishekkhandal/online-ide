$("#form").submit(function() {
 var code = $('textarea#codeArea').val();
 var language = $('#language').val();
 var jsonMimeType = "application/json;charset=UTF-8";
 $.ajax({
  type: "POST",
  url: "docker.py",
  data: {
   "language": language,
   "code": code
  },

  beforeSend: function(x) {
   if (x && x.overrideMimeType) {
    x.overrideMimeType(jsonMimeType);
   }
  },
  dataType: "json",
  success: function(d) {
   document.getElementById("codeOutput").src = d.url;
  },
  error: function(d) {
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
  chars = (text.match(/[\\uD800-\\uDBFF][\\uDC00-\\uDFFF]|[^]/g) || []).length,
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
   len += 4;
   i++;
  } else if (code < 0xffff) {
   len += 3;
  } else {
   len += 4;
  }
 }
 return len;
}

