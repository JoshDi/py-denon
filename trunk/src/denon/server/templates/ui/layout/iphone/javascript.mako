<script type="text/javascript" src="/static/js/jquery.js"></script>
<script type="text/javascript" src="/static/js/jquery-ui.js"></script>
<script type="text/javascript">
    var readBuffer = 0;
    var bufferButton = '#bufferButton';

    function toggleBuffer(){
        onTxt = "Read Buffer: ON";
        offTxt = "Read Buffer: OFF";
        if (readBuffer == 0){
            readBuffer = 1;
            $(bufferButton).text(onTxt);
        }else{
            readBuffer = 0;
            $(bufferButton).text(offTxt);
        }
        return readBuffer
    }

    function switchBuffer(onOff){
        onTxt = "Read Buffer: ON";
        offTxt = "Read Buffer: OFF";
        if (onOff == 0){
            readBuffer = 0;
            $(bufferButton).text(offTxt);
        }else{
            readBuffer = 1;
            $(bufferButton).text(onTxt);
        }
        return readBuffer
    }

    function sendCommand(cmd, outDiv){
        var cmd;
        $('#command button').attr("disabled","disabled");	
         $.ajax({
            url: "/ajax/",
            async: false,
            processData: false,
            data: 'readbuffer=' + readBuffer + '&command=' + cmd,
            dataType: 'json',
            success: function(json){
                var out = null;

                if(json['status'] != 'success'){
                    $(outDiv).html('<b>Error:</b> ' + json['message']);
                    return false;
                }
            
                out = "Command sent: " + cmd;
                if(readBuffer){
                    out += "<br/>Received: ";
                }
                for (buf in json['buffer']){
                    out += " " + json['buffer'][buf];
                }

                $(outDiv).html(out);
                return true;
            },
            error: function(e, f){
                return false;
            }
         });
        $('#command button').attr("disabled","");
    }
</script>