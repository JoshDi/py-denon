<div id="accordion">
    <div>
        <a href="javascript:void(0);">Command</a>
        <div class="content" id="command">
            <button onclick="sendCommand('PWON', '#commandOutput');">Power On</button>
            <button onclick="sendCommand('PWSTANDBY', '#commandOutput');">Power Off</button>
            <button onclick="sendCommand('MUON', '#commandOutput');">Mute</button>
            <button onclick="sendCommand('MVUP', '#commandOutput');">VOL UP</button>
            <button onclick="sendCommand('MVDOWN', '#commandOutput');">VOL DOWN</button>
            <button onclick="sendCommand('SICD', '#commandOutput');">CD</button>
            <button onclick="sendCommand('SIATUNER', '#commandOutput');">TUNER</button>
            <button onclick="toggleBuffer();" id="bufferButton">Read Buffer: Off</button>
            <hr />
            <form onsubmit="sendCommand($('#cmd').val());return false;">
                <input type="text" name="command" id="cmd" value="MVUP" />
                <small><button type="submit" id="cmdBtn"/>Send command</button></small>
            </form>
            <div id="commandOutput"></div>
    </div>
    <div>
        <a href="#">Status</a>
        <div class="content" id="status">
            <button onclick="tmpBuffer = readBuffer;switchBuffer(1);sendCommand('PW?,MV?,SI?', '#statusOutput');switchBuffer(readBuffer);">Get status</button>
            <div id="statusOutput">
            </div>
        </div>
    </div>
    <div>
        <a href="javascript:void(0);">Macros</a>
        <div class="content" id="command">Not available yet.
        </div>
    </div>
</div>