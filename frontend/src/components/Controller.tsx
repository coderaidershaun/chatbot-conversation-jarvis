import { useState } from "react";
import { ReactMediaRecorder } from "react-media-recorder";
import axios from "axios";

const Controller = () => {
  const [mediaBlobUrl, setMediaBlobUrl] = useState<string | null>(null);
  const [audio, setAudio] = useState<string | null>(null);

  function createBlobURL(data: any) {
    const blob = new Blob([data], { type: "audio/mpeg" });
    const url = window.URL.createObjectURL(blob);
    return url;
  }

  const handleStop = async (blobUrl: string) => {
    setMediaBlobUrl(blobUrl);
    setAudio(null);
    // convert blob url to blob object
    fetch(blobUrl)
      .then((res) => res.blob())
      .then(async (blob) => {
        // create form data with blob object
        const formData = new FormData();
        // formData.append("file", blob);
        formData.append("file", blob, "myFile.wav");
        // send form data to api endpoint
        await axios
          .post("http://localhost:8000/post-audio", formData, {
            headers: {
              "Content-Type": "audio/mpeg",
            },
            responseType: "arraybuffer", // Set the response type to handle binary data
          })
          .then((res: any) => {
            const blob = res.data;
            const audio = new Audio();
            audio.src = createBlobURL(res.data);
            // Play the audio file
            // audio.play();

            // Store the audio file
            setAudio(audio.src);
          })
          .catch((err: any) => console.error(err));
      });
  };

  return (
    <ReactMediaRecorder
      audio
      onStop={handleStop}
      render={({ status, startRecording, stopRecording }) => (
        <div>
          <p>{status}</p>
          <button
            className="bg-sky-500 text-white p-2"
            onClick={startRecording}
          >
            Start Recording
          </button>
          <button className="bg-sky-500 text-white p-2" onClick={stopRecording}>
            Stop Recording
          </button>
          {mediaBlobUrl && <audio src={mediaBlobUrl} controls />}
          {audio && <audio src={audio} controls />}
        </div>
      )}
    />
  );
};

export default Controller;
