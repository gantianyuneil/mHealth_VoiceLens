const downloadLink = document.getElementById('download');
const stopButton = document.getElementById('stop');

const handleSuccess = function(stream) {
    const options = {mimeType: 'audio/webm'};
    const recordedChunks = [];
    const mediaRecorder = new MediaRecorder(stream, options);

    mediaRecorder.addEventListener('dataavailable', function(e) {
        if (e.data.size > 0) recordedChunks.push(e.data);
    });

    mediaRecorder.addEventListener('stop', function() {
        downloadLink.href = URL.createObjectURL(new Blob(recordedChunks));
        downloadLink.download = 'UserVoice.mp3';
        console.log(document.getElementById('recorder'))
        document.getElementById('recorder')
    });

    stopButton.addEventListener('click', function() {
        mediaRecorder.stop();
    });

    mediaRecorder.start();
}

function RecButton() {
    
    var elem = document.getElementById("stop");
    if (elem.innerHTML == "Rec" ) {
        navigator.mediaDevices.getUserMedia({ audio: true, video: false }).then(handleSuccess);
        elem.innerHTML = "Stop";
    }
    else {
        elem.innerHTML = "Rec"
        document.getElementById("download").innerHTML = "Download";
    };

}